---
layout: post
title: "Hacking GitHub Contributions Calendar"
date: 2013-04-17 21:06
comments: true
github_issue_id: 13
categories: 
---

GitHub profile pages include a neat visualization of commit history that they
call the "[contributions calendar][]". This 53x7 grid shows the number of
commits and other GitHub interactions that the user performed on each day for
the last year.

![Example graph](/images/blog/timeline.png)

Each cell in the graph is shaded with one of 5 possible colors. These colors
correspond to the [quartiles][] of the [normal distribution][] over the range
`[0, max(v)]` where `v` is the sum of issues opened, pull requests proposed and commits authored per day.

If your all time high for the last year was 100 contributions in a single day,
the cells would color like this:

| Contributions   | Color                                             |
| :-------------- | :-----------------------------------------------: |
| 0               | ![gray](/images/blog/eeeeee.png "#eeeeee")        |
| 1  - 24         | ![pale green](/images/blog/d6e685.png "#d6e685")  |
| 25 - 49         | ![light green](/images/blog/8cc665.png "#8cc665") |
| 50 - 74         | ![green](/images/blog/44a340.png "#44a340")       |
| 75+             | ![dark green](/images/blog/1e6823.png "#1e6823")  |


A tweet got me interested in the possibility of gaming the interaction data to
control the display:

<blockquote class="twitter-tweet"><p>GitHub users might find this guy's contribution graph interesting/funny: <a href="https://t.co/xOFjLbqUK2" title="https://github.com/will">github.com/will</a></p>&mdash; Peter Cooper (@peterc) <a href="https://twitter.com/peterc/status/322636613018607617">April 12, 2013</a></blockquote><script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

[@will][] has done something to make his calendar spell "WILL" over and over.
Looking at his contribution activity list it was pretty obvious that this
trick had something to do with the [will/githubprofilecheat][] and/or
[will/githubprofilecheat2][] repositories.

I did some digging in the [git documentation][] to see how hard it is to fake
the date on a commit. It turns out that it's as easy as setting an environment
variable. The `GIT_AUTHOR_DATE` and `GIT_COMMITTER_DATE` environment variables
can be used to provide [git-commit-tree][] with dates for the author and
commit dates that are attached to each commit object.

Armed with this bit of trivia I decided that I would try to do something
interesting with my contributions graph. I didn't just want to copy [@will][]
and write my name in the graph. I decided that I would pay homage to my
gravatar instead and make a series of [gliders][] that ran across the
timeline. The result of my experiment can be seen in the image at the top of
this post.

The script that I used to generate the commits with faked dates is available
in my [bd808/profile-life][] repository.

The script takes the path to a pattern file and an optional start date as
arguments.

``` sh
./bin/pattern-to-commits.sh patterns/glider.cells 2012-04-15 | sh
```

The pattern file is expected to be in the [plaintext][] Life format. This
format allows you to specify an on/off pattern. When a cell is "on" the script
will output 23 commits (one per hour) for the corresponding day. "Off" cells
won't generate any commit activity.

``` text
!Name: Profile Glider Train
!A simulation of a glider cruising across the contributions timeline.
O.O...O.O....O..................................................................
.OO.O.O..OO...O.O.O...O.O....O..................................................
.O...OO.OO..OOO..OO.O.O..OO...O.O.O...O.O....O..................................
.................O...OO.OO..OOO..OO.O.O..OO...O.O.O...O.O....O..................
.................................O...OO.OO..OOO..OO.O.O..OO...O.O.O...O.O....O..
.................................................O...OO.OO..OOO..OO.O.O..OO...O.
.................................................................O...OO.OO..OOO.
```

The script reads in this file a column at a time using the `cut` command. It
loops over the characters from the column and when it finds an `O` it echos
commit commands to stdout:

``` sh
GIT_AUTHOR_DATE='2013-04-17T20:00' GIT_COMMITTER_DATE='2013-04-17T20:00' \
git commit --allow-empty -m '2013-04-17T20:00'
```

This output can be piped to bash to apply the commits to the repository.

An interesting extension of this script would be to support all 5 possible
colors. It would also be nice if the script read your current contribution
history to determine how many commits are necessary to hit the 4th quartile
every time. For now these additions are left as an exercise for the reader. :)

[contributions calendar]: https://help.github.com/articles/viewing-contributions#contributions-calendar
[quartiles]: https://en.wikipedia.org/wiki/Quartile
[normal distribution]: https://en.wikipedia.org/wiki/Normal_distribution
[@will]: https://github.com/will
[will/githubprofilecheat]: https://github.com/will/githubprofilecheat
[will/githubprofilecheat2]: https://github.com/will/githubprofilecheat2
[git documentation]: http://git-scm.com/docs
[git-commit-tree]: http://git-scm.com/docs/git-commit-tree#_commit_information
[gliders]: https://en.wikipedia.org/wiki/Glider_%28Conway%27s_Life%29
[plaintext]: http://www.conwaylife.com/wiki/Plaintext
[bd808/profile-life]: https://github.com/bd808/profile-life
