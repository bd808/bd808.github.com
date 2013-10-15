---
layout: post
title: "Managing my laptop with Boxen"
date: 2013-10-14 22:11
comments: true
github_issue_id: 17
categories: 
---

[Boxen][] is a framework and collection of libraries created by the fine folks
at [GitHub][] to make setting up and managing Mac OS X computers easy and
repeatable. Rather than a simple set of shell scripts or other provisioning
tools, Boxen uses [Puppet][] to automate installing and configuring software.
I don't have the time or space to explain how great Puppet is a configuration
management is, so you'll have to trust me or go do your own research.

Anybody could take a stab at rolling their own collection of Puppet manifests
to manage their laptop or their corporate install base. That's actually
exactly what GitHub did to create Boxen. Having tried (and failed) at doing
just that before I was pretty impressed when I gave Boxen a test drive. GitHub
has not only provided a system that "works for them"; they have also managed
to engineer a reasonably extensible solution for a very complex problem.

You can use your favorite search engine to find folks who can wax poetic about
the magnitude of this accomplishment. Let's get on with a description of what
I've been able to do with it.

<!-- more -->

I'm using Boxen to manage my `$DAYJOB` laptop. This was a great place to start
because I had a brand new laptop that needed to be setup and a brand new tool
to use to do it. I started by following the [bootstrapping instructions][] to
create [my own copy of the template project][]. I made a few changes to the
[site manifest][] and then started working on a [manifest for myself][].

Along the way I decided I didn't like a few of the decisions that the Boxen
architects had made. As I pointed out earlier, the team behind Boxen
anticipated this and changing most things is as easy as forking a repo, making
your change and updating the [Puppetfile][] in your Boxen project.

At the moment I have customized or created these repositories:

- [my-boxen](https://github.com/bd808/my-boxen): My fork of [boxen/our-boxen](https://github.com/boxen/our-boxen).
- [puppet-boxen](https://github.com/bd808/puppet-boxen): Fork of the core
  [boxen/puppet-boxen](https://github.com/boxen/puppet-boxen) modules that
  installs [Homebrew](http://brew.sh/) in `/usr/local` instead of under
  `/opt/boxen`.
- [puppet-dnsmasq](https://github.com/bd808/puppet-dnsmasq): Fork of
  [boxen/dnsmasq](https://github.com/boxen/puppet-dnsmasq) that uses the stock
  Homebrew `dnsmasq` install and provides `dnsmasq::address` to configure new
  address mappings.
- [puppet-geektool](https://github.com/bd808/puppet-geektool): Original
  module to install [GeekTool](http://projects.tynsoe.org/en/geektool/).
- [puppet-git](https://github.com/bd808/puppet-git): Fork of
  [boxen/puppet-git](https://github.com/boxen/puppet-git) to use the stock
  Homebrew version of [git](http://git-scm.com/).
- [puppet-growl](https://github.com/bd808/puppet-growl): Fork of
  [petems/puppet-growl](https://github.com/petems/puppet-growl) that installs
  an aging version of [Growl](http://growl.info/). I've since abandoned this
  in favor a [self-compiled version](http://growl.info/documentation/developer/growl-source-install.php) which I should figure out how to Puppetize.
- [puppet-homebrew](https://github.com/bd808/puppet-homebrew): Fork of
  [nybblr/puppet-homebrew](https://github.com/nybblr/puppet-homebrew) that
  adds support for installing in `/usr/local` and using custom Homebrew
  [taps](https://github.com/mxcl/homebrew/wiki/brew-tap).
- [puppet-monolingual](https://github.com/bd808/puppet-monolingual): Original
  module to install [Monolingual](http://monolingual.sourceforge.net/).
- [puppet-osx](https://github.com/bd808/puppet-osx): Fork of
  [codec/puppet-osx](https://github.com/codec/puppet-osx) that pulls in
  patches from [joebadmo/puppet-osx](https://github.com/joebadmo/puppet-osx)
  and adds a few system settings of my own.
- [puppet-slimbatterymonitor](https://github.com/bd808/puppet-slimbatterymonitor): Original module to install [SlimBatteryMonitor](http://www.orange-carb.org/SBM/).

The one thing I most wish someone would figure out how to do with Boxen/Puppet
is install apps from the [Mac App Store](https://www.apple.com/osx/apps/app-store.html).

[Boxen]: https://boxen.github.com/
[GitHub]: https://github.com/
[Puppet]: https://puppetlabs.com/
[bootstrapping instructions]: https://github.com/boxen/our-boxen
[my own copy of the template project]: https://github.com/bd808/my-boxen
[site manifest]: https://github.com/bd808/my-boxen/blob/master/manifests/site.pp
[manifest for myself]: https://github.com/bd808/my-boxen/blob/master/modules/people/manifests/bd808.pp
[Puppetfile]: https://github.com/bd808/my-boxen/blob/master/Puppetfile
