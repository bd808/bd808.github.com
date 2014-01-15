---
layout: post
title: "How do you know when you're done?"
date: 2014-01-14 21:48:20 -0700
comments: true
github_issue_id: 22
categories: scrum sdlc
---

In scrum a story is "Done" when it meets the team's shared "Definition of
Done". The definition of done is roughly a list of requirements that all parts
of the software increment must adhere to to be called complete. Like most
things in scrum the implementation details are left to the team to decide.
When I was first working with scrum I had a hard time finding examples of what
a typical definition of done would include. Most scrum authors (and even many
trainers) wave their hands and say that it's too specific to the team and
their environment to generalize.

<!-- more -->

Intellectually I agree with this, but pragmatically I think that having some
sort of rough draft of ideas to start from makes writing the first draft
easier. This particular definition of Done is written from the perspective of
a cross functional team responsible for implementing features in a product. It
does not include Done criteria for the operations or support teams that will
maintain the deployed software or assist customers in its use. It does however
include deliverables that must be produced by the development team to support
those additional teams.

This list taken as a whole looks pretty daunting. It turns out that producing
production ready software is hard work. It is such hard work that it takes
a group of well trained individuals working as a team to complete properly.
This list is a recipe that can and should be used by the team to ensure that
they produce an increment that is worthy of their combined energy. When used
properly it will increase the reputation and worth of the team, their product
and the organization.

Done with grooming a story
--------------------------

A groomed story is ***clear, feasible and testable***.

<dl>
<dt>Business Goal described</dt>
<dd>Why will we build this?</dd>
<dt>Acceptance criteria defined</dt>
<dd>What will it do?</dd>
<dt>Tasks identified</dt>
<dd>How will we do it?</dd>
<dt>Story points estimated</dt>
<dd>What will it cost?</dd>
</dl>

It may take several iterations to achieve this level of clarity. In fact
anything that can be quickly groomed is necessarily trivial. It may still take
significant time to implement, but it would have to be a variation on work
that has already been done that is understood by the whole team.

Themes, Epics and large stories will need to be decomposed into smaller parts.
This must happen recursively until the smallest parts are describable using
the criteria established above.

Spikes or other research may need to be done to remove uncertainty about new
tech or legacy impact. These things are stories in their own right and should
be treated as such. R&D must be traceable expense and is just as important as
the final product/feature.


Done with a story
-----------------

<dl>
<dt>Everything from "Done with grooming a story"</dt>
<dd>A story must be groomed before it can be implemented.</dd>
<dt>Design complete</dt>
<dd>Design is not one size fits all. Some stories must have UML and detailed
functional descriptions. Others will only need a statement of "do this just
like we always do an X feature." The level of design required should be
determined during grooming by the team.</dd>
<dt>Design artifacts in wiki/bug tracker/other</dt>
<dd>Design isn't complete until it's tangible artifacts are available to the
team and the business.</dd>
<dt>Design reviewed by peers</dt>
<dd>Similar to a code review, design should get a once over by at least one
tangentially involved party to ensure that the level of detail is appropriate
to the story and that the proposed implementation makes sense.</dd>
<dt>Code complete</dt>
<dd>All code for the story has been written.</dd>
<dt>Unit tests written</dt>
<dd>Unit tests have been written to verify that the code works at the most basic
level. This can be done via TDD or code-then-test as best suits the team and
the story.</dd>
<dt>All code checked into version control</dt>
<dd>Feature code and tests are committed to version control.</dd>
<dt>All unit tests passing</dt>
<dd>Unit tests are passing in all testable environments.</dd>
<dt>Automated code checks passing</dt>
<dd>Coding style, lint and other common automated code quality measurements are passing
according to the organization's definition of passing.</dd>
<dt>CI tests passing</dt>
<dd>Automated tests in the continuous integration environment are passing.</dd>
<dt>Peer code review completed</dt>
<dd>A code review has been completed involving at least one tangentially
involved party.</dd>
<dt>Material defects from code review addressed</dt>
<dd>All questions and defects raised in the code review have been addressed.</dd>
<dt>All acceptance tests (manual and automated) identified, written and passing.</dt>
<dd>Given/When/Then style or other detailed acceptance tests for the story have
been written and verified either with automated tests or manual testing.
Automated tests are preferred as they do not increase the overall manual
testing load of the product.</dd>
<dt>Help/documentation updated</dt>
<dd>"Just enough" help and documentation has been produced so that the feature
can be used by clients, maintained by developers and supported by customer
service and operations.</dd>
<dt>Release notes updated</dt>
<dd>Deliverable artifacts and deployment procedures have been documented.</dd>
</dl>

Done with a sprint
------------------
<dl>
<dt>Everything from "Done with a story"</dt>
<dd>All stories in the sprint must be done (or returned to the backlog) for the
sprint to be done.</dd>
<dt>Released to beta/integration environment</dt>
<dd>The deliverables identified in the release notes for the Sprint must be
deployed in the beta/integration environment. </dd>
<dt>Demoed in beta/integration environment (UAT)</dt>
<dd>The demonstration of the increment to Product Owner and other Stakeholders
must be performed from the beta/integration environment.</dd>
<dt>Approved by Stakeholders</dt>
<dd>The increment must be approved following UAT.</dd>
<dt>CI/automated tests passing</dt>
<dd>All automated tests against the product must be passing. </dd>
<dt>Integration tests passing</dt>
<dd>Manual integration tests for the product must be passing.</dd>
<dt>Regression tests passing</dt>
<dd>Manual regression tests for the product must be passing.</dd>
<dt>Code coverage for automated tests meets acceptable guidelines.</dt>
<dd>Code coverage measurements for unit tests must be within acceptable ranges.</dd>
<dt>Performance tests passing</dt>
<dd>Performance/scaling tests must return results within acceptable ranges.</dd>
<dt>Diagrams/documentation updated to match final state</dt>
<dd>Documentation for design, implementation, deployment, support and use must
be updated to match the completed increment.</dd>
<dt>Bugs closed or pushed into backlog</dt>
<dd>Defects identified in UAT, QA and development must be resolved or appended
to the backlog for Product Owner triage.</dd>
<dt>Unfinished stories pushed into backlog</dt>
<dd>Any work in the sprint which does not meet this definition of done will be
returned to the backlog. The Sprint isn't done as long as any non-done issues
are associated with it.</dd>
</dl>

Done with a QA/staging release
------------------------------
<dl>
<dt>Everything from "Done with a sprint"</dt>
<dd>All Sprints that are to be included in the release must be Done.</dd>
<dt>Operations guide updated and approved by Ops</dt>
<dd>The support documentation delivered to Ops via the wiki must be updated and
those updates must be approved (UAT) by the Operations team.</dd>
<dt>Automated tests passing</dt>
<dd>All automated tests available for the QA/Staging environment must be
passing.</dd>
</dl>

Done with a production release
------------------------------
<dl>
<dt>Everything from "Done with a QA/Staging Release"</dt>
<dd>A successful QA/Staging release is a prerequisite for a Production release.</dd>
<dt>Stress/Load tests passing</dt>
<dd>Stress/Load testing in the QA/Staging environment must return results within
acceptable ranges.</dd>
<dt>Network/Component diagrams updated</dt>
<dd>Documentation for design, implementation, deployment, support and use must
be updated to match the proposed release.</dd>
</dl>
