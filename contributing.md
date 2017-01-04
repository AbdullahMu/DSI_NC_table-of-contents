# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Contributing Guidelines

Our instructor community has grown tremendously, and everyone does so much to adapt, correct bugs, and enhance our curriculum as they prepare for the classroom.  For this reason, we ask that you share your work back to this master repository so other instructors can benefit. The more contributions we get, the more we can refine our materials and provide robust supporting resources.

Please use the documentation below as a guide for instructor contributions. Included in this file is information about:

- [DSI GitHub Community](#the-community)
- [Contributing Guidelines for Issues or Pull Requests](#contributing-guidelines-issues-and-pull-requests)
- [Using Labels Appropriately](#labels)
- [Contributor Expectations](#contributors-expectations)

_Note: A lot of the language in this readme has been taken and adapted from GitHub's guidelines about contributing to open-source projects_.


## The Community

We've broken down the DSI community as follows:

- **Owner:** Product Manager

- **Maintainers** (write access to the repository): Lead and Senior Instructors; Instructional Designers

- **Contributors** (everyone who can open and have a pull request merged into a project): Instructors; Subject Matter Experts

- **Community Members** (users who often use and care deeply about the project and are active in discussions for future product updates): Producers, RDs

## Contributing Guidelines: Issues and Pull Requests

Contributing back should take the form of issues or pull requests depending on the nature of the contribution.  Contributions via GitHub pull requests and issues should *only* be created for DSI curriculum related materials.  Production feedback or questions should be submitted to [GA's helpdesk](ga.co/helpdesk).

#### Create an Issue

If you find a bug in a lesson, lab, or readme (and you don’t know how to fix it) if have higher-level questions about the scope or sequence of a unit or lesson, or have a general question about the curriculum, create an issue!

Here are a few tips when creating an issue:

- Check existing issues for your issue. Duplicating an issue is slower for both parties so search through open and closed issues to see if what you’re running into has been addressed already.

- Be clear about your feedback or question by using a label and thorough details in your issue description: what lesson were you using? what should have happened that didn't happen? how would you change a week? etc.

- Include error messages, logs, or screenshots

- Paste error output or logs in your issue or in a Gist. If pasting them in the issue, wrap it in three backticks so that it renders nicely.

#### Create a Pull Request

If you’re able to patch the bug, create a new lesson/lab, or correct some syntax/spelling yourself – fantastic! Make a pull request with your changes! Be sure you’ve read our [styleguide](styleguide.md) and follow accordingly as it will speed up the merging process. Once you’ve submitted a pull request, the owners and maintainers will carefully review your code/suggestions to determine whether or not more action is needed or the request should be merged or closed.

Here are a few tips when creating a pull request:

- All pull requests should be submitted from a feature branch on your local fork, straight to *generalassembly-studio/dsi-course-materials/master*.

- Before submitting a pull request, please make sure your local feature branch is up to date with generalassembly-studio/dsi-course-materials/master:

```bash
$ git remote add upstream git@github.com:generalassembly-studio/dsi-course-materials
$ git fetch --all
$ git checkout -b my-feature-branch upstream/master
```

- Contribute in the style of this repository to the best of your abilities. This may mean using indents, semi colons or comments differently than you would in your own repository, but makes it easier for the maintainer to merge, others to understand and maintain in the future.  Again, look at our [styleguide](styleguide.md) for more information.

- If you're submitting a new _lesson_, _lab_, or _homework_ resource, **create a feature branch** for each individual resource.  Lesson branch naming should follow the same naming style and convention we use for folders. For example:

```bash
$ git checkout master
On branch master
nothing to commit, working directory clean

$ git checkout -b intro-to-relational-data-modeling
Switched to a new branch intro-to-relational-data-modeling
```

- If a lesson/lab/homework both have the exact same name, just denote which with `-lesson` or `-lab`.

```bash
$ git checkout -b layouts-partials-and-views-lesson
```

... or ...

```bash
$ git checkout -b layouts-partials-and-views-lab
```

- Again, if submitting a new lesson or lab resource, please make sure the resources are in the standard [lesson](../../templates/baseline-lessons) and [lab](../../templates/baseline-labs/) templates.


##### Open Pull Requests

Once you’ve opened a pull request, a discussion may start around your proposed changes. Other contributors and users may chime in, but ultimately the decision is made by the maintainer(s) and the owner. You may be asked to make some changes to your pull request, if so, add more commits to your branch and push them – they’ll automatically go into the existing pull request.

If your pull request is merged – great! If it is not, no sweat, it may not be what the project maintainer had in mind, or they were already working on it.

## Labels

As discussed, please use labels to make it easier for owners and maintainers to work through and address issues and merge pull requests.  Take a look at the labels and label use cases below:

<p align="center">
  <img src="https://i.imgur.com/l51r7vz.png">
</p>

- **Bug Fix**:  Used by contributors for either pull requests that contain solutions or issues reporting a bug

- **Discussion/Question**:  Used by maintainers, owners, or contributors on issues for higher-level discussions or questions about the curriculum

- **Duplicate**:  Used by maintainers or owners to classify duplicate issues or pull requests

- **Enhancement/Suggestion**:  Used by contributors to suggest changes in an issue or enhance a lesson/lab for various reasons

- **Help Wanted**:  Used by maintainers, owners, or contributors to invite others to collaborate; this will be used in conjunction with assignment

- **Needs Review**: Used by maintainers or owners to call for technical support or a second set of eyes

- **Needs Revision**:  Used by maintainers or owners to notify contributors that more work is needed before a merge

- **New Resource**:  Used by contributors to submit a new lesson, lab, or homework


## Contributors Expectations

Given the bandwidth of the owners and maintainers, issues and pull requests will be addressed about once a week, by a group of owners and maintainers, going forward.  The outcome of the issue or pull request is likely to fall into one of three buckets:

1. **Merged / Addressed** - The feedback, solution, new resource, or bug fix is merged in or addressed immediately. Bug fixes will take priority and, as long as merge conflicts are not an issue, will be merged, immediately.

2. **Prioritized for Product Sprint** - If the feedback or pull request cannot be addressed in the time dedicated each week, but the owners and maintainers acknowledge the immediate impact, the pull request or issue will be brought to the next sprint planning meeting (these occur every two weeks) and appropriate time will be budgeted to address and work through the issue or pull request.

3. **Logged into the feedback log** - If the feedback or pull request cannot be addressed in the time dedicated each week, and the owners and maintainers do not see the immediate value in prioritizing this feedback, it will be closed and logged into the WDI feedback log to be used for future iterations and releases of the curriculum. 

Expect all your issues or pull requests to be commented on by an owner or maintainer.
