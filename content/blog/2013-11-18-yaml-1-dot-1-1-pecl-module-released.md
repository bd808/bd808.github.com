Layout: post
Title: Yaml 1.1.1 PECL Module Released
Date: 2013-11-18 22:20:43 -0700
Comments: true
Github_issue_id: 20
Tags: pecl, yaml, php

I'm glad to announce that I finally got around to releasing the bug fix
version of the [YAML PECL module](http://pecl.php.net/package/yaml) that
I announced on 2013-04-23. Version 1.1.1 fixes several long standing bugs:

- [#61770](https://bugs.php.net/bug.php?id=61770) Crash on nonunicode character
- [#61923](https://bugs.php.net/bug.php?id=61923) Detect_scalar_type() is not aware of base 60 representation
- [#63086](https://bugs.php.net/bug.php?id=63086) Compiling PHP with YAML as static extension fails
- [#64019](https://bugs.php.net/bug.php?id=64019) Segmentation fault if yaml anchor ends with a colon
- [#64694](https://bugs.php.net/bug.php?id=64694) Segfault when array used as mapping key

<!-- more -->

It also includes a small but important patch from a community member who
discovered that I had left the `yaml_emit_file()` method marked as
unimplemented when it actually was fully functional.

I hope the users of this extension will find the changes to be useful. I also
welcome bug reports, feature requests and patches from the community. I would
especially appreciate it if someone found the time become the maintainer of
a Debian package for the project to make it a little easier for some users to
install.
