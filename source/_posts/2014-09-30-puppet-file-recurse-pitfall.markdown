---
layout: post
title: "Puppet file recurse pitfall"
date: 2014-09-30 20:44:13 -0600
comments: true
github_issue_id: 24
categories: puppet sysadmin
---

[Puppet][] has become my go to system management tool in no small part because
it is the tool that the operations group at [$DAYJOB][] has standardized on
for our production infrastructure management. It took quite a while for me to
get the hang of how Puppet does what it does, but today I'd say I'm a fairly
decent Puppet programmer. Every once in a while however I stumble on something
new and surprising.

A couple of weeks ago I got an interesting bug report from a user about
a collection of Puppet manifests I help manage. The bug was that his testing
server was pegged at 99% CPU utilization for multiple minutes during each
`puppet agent` run. The bug reporter did a great job of investigating and had
also found that `strace` showed a repetitive stream of `stat()` calls while
the process was hogging the CPU.

This also turned out to the be the great kind of bug that was reproducible.
The first testing server I tried the steps from the bug report on showed the
exact same symptoms. I grabbed some very verbose logs by turning on the
`--debug` logging in `puppet agent` and logging all of the system calls with
`strace` at the same time:

``` sh
$ TZ=UTC strace /usr/bin/ruby /usr/bin/puppet agent --onetime --verbose \
   --no-daemonize --no-splay --debug 2>&1 |
   tee /tmp/loud-puppet-strace.log
```

<!-- MORE -->

Looking at the `strace` messages there was clearly a pattern of `stat()` calls
for `.rb` files in unexpected numbers. Puppet was pretty obviously searching
for ruby files that were related to several [defined types][] implemented in
our manifests. The log was full of lines like
`stat("/var/lib/puppet/lib/puppet/type/git::clone.rb")`. A little
searching led me to [PUP-2924][] which explained that Puppet was checking to
see if the type had been implemented as a [custom type][] in Ruby code first
before looking for a defined type in the Puppet manifests. In our case, there
were 17 possible paths for a Ruby class to be loaded from which led to 17
failed stat calls for each defined type in the manifest.

What this did not explain however what why there were so many checks for our
`git::clone` resource. Two million, two hundred ninety three thousand, six
hundred and seventy seven calls to `stat()` for the same collection of files
in this one puppet run. Insanity!

``` sh
$ grep stat\( loud-puppet-strace.log | grep git::clone | wc -l
2293677
```

So now I knew what was happening, but I needed to dig deeper to try and figure
out why it was happening. For this I wanted even more verbose `puppet agent`
output.

``` sh
$ TZ=UTC /usr/bin/ruby /usr/bin/puppet agent --onetime --verbose \
     --no-daemonize --no-splay --debug --trace --evaltrace --noop 2>&1 |
     tee /tmp/puppet-noop.log
```

I watched this run happen in real time and took note of what was logged just
before the long pause in logging which accompanied each CPU utilization spike
that I now knew correlated to the outrageous number of `stat()` calls.

```
Info: Git::Clone[vagrant]: Starting to evaluate the resource
Info: Git::Clone[vagrant]: Evaluated in 0.01 seconds
[... long pause here ...]
Info: /Stage[main]/Labs_vagrant/File[/srv/vagrant]: Starting to evaluate the resource
Info: /Stage[main]/Labs_vagrant/File[/srv/vagrant]: Evaluated in 0.00 seconds
```

This led to my ah ha moment and an eventual fix. The `File[/srv/vagrant]`
resource had a definition that looked something like this:

``` puppet
file { '/srv/vagrant':
    recurse => true,
    owner   => 'vagrant',
    group   => 'www-data',
    require => Git::Clone['vagrant'],
}
```

The intent of this was to recursively manage the ownership of files in the
/srv/vagrant directory. Seems pretty simple right? `chown -R vagrant:www-data
/srv/vagrant` would do the same thing at a command prompt.

It turns out however that what Puppet does under the hood is more complicated.
The `recurse => true` flag makes Puppet do the equivalent of a `find` command
on the /srv/vagrant directory and then create a new File resource for each file
and directory found that replicates the other settings of the parent type.

``` puppet
file { '/srv/vagrant/file1':
    owner   => 'vagrant',
    group   => 'www-data',
    require => Git::Clone['vagrant'],
}
file { '/srv/vagrant/file2':
    owner   => 'vagrant',
    group   => 'www-data',
    require => Git::Clone['vagrant'],
}
# ... Lots and lots more file resources here ...
file { '/srv/vagrant/subdir/subdir/subdir/fileN':
    owner   => 'vagrant',
    group   => 'www-data',
    require => Git::Clone['vagrant'],
}
```

All of these resources are added to the internal DAG (Directed Acyclic Graph)
and then evaluated one by one. Our /srv/vagrant directory can have a lot of
files beneath it. In my testing server there turned out to be about 135,000
files. So Puppet added 135,000 extra nodes to the DAG and as it placed each
one it called `stat()` 17 times to see if there was a Ruby class providing the
`git::clone` resource that Puppet wanted to ensure that the new File resource
followed.

***YIKES!***

I think there are probably several opportunities here for optimizations in the
Puppet implementation itself. Caching the implementation of the `git::clone`
resource would be one that comes to mind pretty quickly. Making recursive File
resources operate based on one node rather than N would be another. There is
probably some kind of graph insertion change that could be made as well. If
I was more comfortable with Ruby I might take a stab at one or more of these
myself.

To fix the bug at hand however I looked around and found that we really didn't
need to bother with the recursive `chown` at all, so I was able to remove the
whole `File[/srv/vagrant]` resource from the manifest and let our `git::clone`
implementation create the directory when it performed the initial git
repository clone operation.


[Puppet]: http://puppetlabs.com/
[$DAYJOB]: https://wikimediafoundation.org/wiki/Home
[defined types]: https://docs.puppetlabs.com/learning/definedtypes.html
[PUP-2924]: https://tickets.puppetlabs.com/browse/PUP-2924
[custom type]: https://docs.puppetlabs.com/guides/custom_types.html
