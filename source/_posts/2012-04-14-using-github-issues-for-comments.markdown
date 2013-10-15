---
layout: post
title: "Using GitHub issues for comments"
date: 2012-04-14 20:22
comments: true
github_issue_id: 7
categories: 
---

I was inspired by [Ivan Zuzak's post](http://ivanzuzak.info/2011/02/18/github-hosted-comments-for-github-hosted-blogs.html) to try using GitHub issues on the [repository for this blog](https://github.com/bd808/bd808.github.com) to collect and display reader comments. I'm using [Octopress](http://octopress.org/) to generate the site, so I decided to make some customizations to make applying Ivan's ideas easy for me.

I started by adding a new configuration setting to my `_config.yml` file: `github_comments: true`. I'll use this configuration switch to turn the new feature on in other places in the codebase.

<!-- more -->

Next I changed the [Liquid template](https://github.com/mojombo/jekyll/wiki/Liquid-Extensions) in source/\_layout/post.html to include a link to the comment thread for the post. I added this block right after the existing disqus rendering block:

{% codeblock source/_layout/post.html %}{% raw %}
{% if site.github_comments and page.github_issue_id %}
<section id="comments">
  <header>
    <h2>Comments</h2>
    <p>Visit <a href="https://github.com/{{site.github_user}}/{{site.github_user}}.github.com/issues/{{page.github_issue_id}}">this post's issue page on GitHub</a> to add a comment.</p>
  </header>
</section>
{% endif %}
{% endraw %}{% endcodeblock %}

If the `github_comments: true` flag is set and the [yaml front
matter](https://github.com/mojombo/jekyll/wiki/yaml-front-matter) for the post
contains a `github_issue_id: N` setting, this block with display a link to
issue N in the associated GitHub repository.

Next I wanted to display any current comments. I use a slightly tweaked
version of Ivan's javascript to do this.

{% codeblock source/_includes/github_comments.html %}{% raw %}
{% if site.github_comments and page.comments == true %}
<script type="text/javascript">
$.ajax({
    url: "https://api.github.com/repos/{{site.github_user}}/{{site.github_user}}.github.com/issues/{{page.github_issue_id}}/comments"
  , method: "get"
  , headers: { Accept: "application/vnd.github.full+json" }
  , error: function(e){}
  , success: function(resp){
      var cuser, cuserlink, clink, cbody, cavatarlink, cdate;
      for (var i=0; i<resp.length; i++) {
        cuser = resp[i].user.login;
        cuserlink = "https://github.com/" + resp[i].user.login;
        clink = "https://github.com/{{site.github_user}}/{{site.github_user}}.github.com/issues/{{page.github_issue_id}}#issuecomment-" + resp[i].url.substring(resp[i].url.lastIndexOf("/")+1);
        cbody = resp[i].body_html;
        cavatarlink = resp[i].user.avatar_url;
        cdate = (new Date(resp[i].created_at)).toLocaleString();

        $("#comments").append('<div class="comment"><div class="comment-header"><a class="comment-user" href="' + cuserlink + '"><img class="comment-gravatar" src="' + cavatarlink + '" alt="" width="20" height="20"> ' + cuser + '</a><a class="comment-date" href="' + clink + '">' + cdate + '</a></div><div class="comment-body">' + cbody + '</div></div>');
      }
    }
});
</script>
{% endif %}
{% endraw %}{% endcodeblock %}

I added an include for this new file in source/_includes/after_footer.html to
get it tacked on to each page:

{% codeblock source/_includes/after_footer.html %}{% raw %}
{% include github_comments.html %}
{% endraw %}{% endcodeblock %}

Those changes plus the OAuth application configuration described in Ivan's post have the blog all setup for comments. The only problem is that I have to remember to manually create an issue on the GitHub side and add it to the yaml front matter for the post. Being a lazy programmer I wanted to get rid of that burden as well. Lucky for me Octopress already has a Rake task that sets up a new blog post. The changes I made here aren't pretty, but they are pragmatic.

{% codeblock Rakefile lang:ruby %}{% raw %}
def create_comment_issue(title, url)
  require 'octopi'
  include Octopi

  authenticated :config => "_github.yml"  do
    user = User.find("bd808")
    repo = user.repository(:name => "bd808.github.com")

    issue = Issue.open :user => user, :repo => repo,
      :params => {
      :title => title,
      :body => "Reader comments on [#{title}](#{url})"
    }
    puts "Successfully opened issue \##{issue.number}"

    labels = issue.add_label "blog-post"

    return issue.number
  end
end
{% endraw %}{% endcodeblock %}

I plugged this function into the existing `new_post` task so that it will
create an issue and plug it's id into the front matter for the new post
automatically when I run a command like `rake new_post["Using GitHub Issues
for Comments"]`:

{% codeblock source/_posts/2012-04-14-using-github-issues-for-comments.markdown lang:yaml%}{% raw %}
---
layout: post
title: "Using GitHub issues for comments"
date: 2012-04-14 20:22
comments: true
github_issue_id: 7
categories: 
---

{% endraw %}{% endcodeblock %}
