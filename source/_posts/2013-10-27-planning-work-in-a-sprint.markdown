---
layout: post
title: "Planning Work in a Sprint"
date: 2013-10-27 20:05
comments: true
github_issue_id: 19
categories: scrum sdlc
---

We've been having some discussions at `$DAYJOB` about process and
methodologies. The topic of late is [scrum](https://scrum.org/) and how it may
or may not be helpful for the particular group I work with. I've been
providing some anecdotal input based my past experience with scrum and other
methodologies/frameworks/practices and asking questions about what problems
the group is hoping to find new solutions for.

I started to write a big wall o' text™ email about a particular topic and then
decided that maybe a blog post would be a better way to work through my idea.
So dear reader^[1](#n1) <a name="n1-r"></a>, here are some of my highly
opinionated and mostly unsubstantiated thoughts about one process that a group
of people could use to plan a scrum sprint (*or really any other iterative
unit of work)*.

<!-- more -->

Pick some work you think you can get done
-----------------------------------------
Step one, pick some work. Sounds easy, but pick it from where? Well that's
a damn good question but one that's going to depend on your environment. For
the sake of this post let's assume that you have access to an ordered list of
features that need to be implemented. Let's further assume that the team and
the stakeholders have talked about these features a little and that the team
has reached a general consensus about how big the top few features are
relative to features the team has worked on in the past. Scrum calls this
a "groomed backlog", but you can call it whatever you'd like.

Now that you know where the work comes from, pick some. How much? Well, as
much as the team thinks it can get done in the iteration. Without knowing your
team and the length of the iteration and how tricky the problems are I can't
tell you. Just go with your collective gut and pick some. If you pick too
little you can always come back and get more. If you pick too much the team
can use that experiential data to adjust when choosing for the next iteration.
Just pick some work for now and adjust in the future based on what happens
during the iteration^[2](#n2) <a name="n2-r"></a>.

Figure out what ties the work together
--------------------------------------
Step two, come up with a narrative about why you chose the work. A list of
features and bugs you want to implement is a great start, but you can do
better. It will be a lot easier for the team to make good choices during the
iteration if they have a more noble goal than "cross off all the things on
this list." If the goal is just to get each item done it's more likely that
people will think of each part in isolation rather than thinking about how
this work builds on what came before and enables more enhancements in the
future.

This step may lead you to switch out some of the things you've chosen with
other things that are in the backlog to make a more cohesive story. That's ok
as long as you keep the most important thing. After all that's the MOST
important thing; if you get it done plus some other stuff and everything works
people should be happy.

This narrative you've created and the work that supports it are the forecast
for the iteration. The product owner can take this information back to the
rest of the stakeholders and tell them what to expect to hear about in the
demonstration meeting at the end of the iteration. Be careful not to tell them
to expect to see all of this work completed. The team has said they'll try to
do this but they can't promise that it will get done any more than the CEO can
promise how much money will be raised or how many new customers will be
acquired.

Figure out how to do the work
-----------------------------
The last step before you close the planning meeting and get back to "real
work", is to figure out how to actually *do* the work. We're talking about
agile practices here so nobody should expect a gantt chart chart or
a architecture document, but <strike>anarchists</strike> agile teams need
enough of a plan to do today's work efficiently. The product owner doesn't
need to stick around for this half of the meeting. The team should have enough
information from the feature descriptions already given to make the tactical
plan.

I'm sure there are other methods that would work as well, but I've personally
had success with a process that starts with finding dependencies. The team
looks at the stories and tries to determine their rough interdependencies. The
goal here is to identify communication interfaces that need to be specified
and sequential implementation order dependencies. The team also looks for ares
of uncertainty that could be resolved with tech spikes and/or further
investigation of the requirements.

Once you've got the dependencies sorted, start breaking down the most obvious
"starting point" features. Start making a list of the smaller tasks that need
to be completed to finish the feature. Keep breaking those tasks down into
even smaller tasks. Stop when the leaf tasks are "small enough". My rule of
thumb is that something that feels like it will take 3-5 ideal hours is small
enough. Getting smaller than that early on is probably a waste of time, but
but staying larger leaves more uncertainty and risk in the plan. Scrum calls
this step "story decomposition". If you only have a few features to break down
do the work as a group. If there are quite a few to get through you can split
up into appropriately skilled groups and work in parallel.

The list of decomposed tasks that the team has created is the start of the
iteration backlog. Just like the product backlog this needs to be put in order
so that when a team member or pair needs more work to do they can just pull
the next most important thing in their area of expertise off of the backlog.
You'll reorder the list as the iteration progresses, but get started by
ordering the tasks you just decomposed.

Depending on your team and the time you have left in the meeting (two hours
per week of iteration is a suggested total duration), you may have time to
outline all of the features. You need to at least outline enough to keep
the whole team occupied for the rest of today and tomorrow. If you have some
high risk things to accomplish in the iteration try to break them down as
early as you can so that someone (or some pair) can start on the tech spikes
or API design or whatever sooner rather than later. Don't forget to put
a "decompose feature X" task onto the backlog for any stories that you
didn't have time to get to by the end of the time box.


Get to work
-----------
Now you've got a list of features to implement, a narrative about why these
things go together and at least a day or two of granular tasks to start
working on. Each team member or pair now needs to select one thing to begin
working on. Start at the start and chose the highest priority task that you
have the skill set to accomplish. When you get **Done**^[3](#n3)
<a name="n3-r"></a> with the task you've taken come back to the backlog and
chose another. Don't forget to mark the things you are working on as in
progress by whatever tracking mechanism the team is using so you and another
team member don't duplicate the work.

Whew. That would have been a nasty email to read. I hope you like it better as
a blog post. Don't forget to use inspection and adaptation to refine this
process so that it works well for your team. I think I've given a reasonable
outline of a process that has worked for me in the past, but never be afraid
to look for ways to improve.

---
1. <a name="n1"></a>*Hi Mom!* [↩](#n1-r)
2. <a name="n2"></a>*"Inspect and adapt" is a common refrain in scrum.* [↩](#n2-r)
3. <a name="n3"></a>*"Definition of Done" is a topic for another post.* [↩](#n3-r)
