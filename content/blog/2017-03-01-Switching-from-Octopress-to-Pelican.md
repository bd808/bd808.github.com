Title: Switching from Octopress to Pelican
Date: 2017-03-01T04:19:06Z
Comments: True
Github_issue_id: 25
Tags: github, octopress, pelican, howto

I fell down a rabbit hole a few days ago. I wanted to write a blog post about
[my new irc library], but the [rbenv] I had setup to run [Octopress] was all
messed up. I stated poking around to try and remind myself how to get it
working again and eventually decided that I should really look for a new
static site generator written in language that I like to use. I ended up
picking [Pelican].

<!-- more -->

There are [plenty of blog posts] already that cover the basics, so I won't try
to give a complete walk through. I mostly used the guides by [Jake Vanderplas]
and [Jinghao Shi] along with the [manual]. I have blogged before about how
I setup Octopress to make [GitHub issues for comments]. I ported this
functionality to Pelican with a couple of commits:

* [bd808/bd808.github.com@412c0b3] adds the javascript and template changes
  needed to render comments and a link to the GitHub issue for a given post.
* [bd808/bd808.github.com@fe45c78] adds a `new_post` target to my [fabric]
  file which creates an issue in the GitHub project and adds the needed
  metadata to a stub Markdown file.

[my new irc library]: https://python-ib3.readthedocs.io/
[rbenv]: //github.com/rbenv/rbenv
[Octopress]: http://octopress.org/
[Pelican]: https://blog.getpelican.com/
[plenty of blog posts]: https://www.google.com/search?q=octopress+to+pelican
[Jake Vanderplas]: https://jakevdp.github.io/blog/2013/05/07/migrating-from-octopress-to-pelican/
[Jinghao Shi]: http://jhshi.me/2015/10/11/migrating-from-octopress-to-pelican/
[manual]: http://docs.getpelican.com/en/stable/
[GitHub issues for comments]: /blog/2012/04/14/using-github-issues-for-comments/
[bd808/bd808.github.com@412c0b3]: https://github.com/bd808/bd808.github.com/commit/412c0b3fc45dacda2bd2800ca5b2d8a49d9ee46e
[bd808/bd808.github.com@fe45c78]: https://github.com/bd808/bd808.github.com/commit/fe45c78fd96577923f958f1c743f8572c0714829
[fabric]: http://www.fabfile.org/
