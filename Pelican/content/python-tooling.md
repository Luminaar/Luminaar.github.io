Title: Python tooling
Date: 2020-01-09 13:32:47
Category: Python
Tags: python
Summary: Overview of development tools for Python - linters, formatters and other. Short description of how we are using some of these tools in production.



# Introduction
This post started as a talk for the Python Guild (a monthly gathering of Python
developers at Avast). I decided to research and put together a summary of
different tools related to Python development. Turns out there are not that
many.


After I gave the talk there was a short discussion and a couple of interesting
ideas were proposed.

I realized that a more interesting topic would be how to use all these tools in
everyday work. That's why I decided to expand this post a bit. First section
contains a list of tools categorized in different categories. In the second
section I will put some thoughts on how these tools can be used in different
scenarios.

----

# The tools

When I started doing research for this post I expected it to be a much more
complicated topic (same as packaging for example). Turns out there are not that
many tools - there is almost only one way to do things.

I this section I will categorize different tools into five categories, describe and
compare them. I know a lot more about tools that I use everyday but I've
experimented with most of the others too.

## Formatters
[PEP8](https://www.python.org/dev/peps/pep-0008/) (Style guide for Python code)
and [PEP257](https://www.python.org/dev/peps/pep-0257/) (Docstring conventions)
are two PEPs that describe how Python code should look. The PEP8 is not meant to
be dogmatic and adhering to it is not the only necessary prerequisite for good
Python code, but it is a start. Because formatting code by hand is tedious,
using some kind of formatter is almost a necessity.

When working in a team, it's is better when everyones code looks the same.
Ideally it shouldn't be obvious who wrote the code from just looking at it. If
everyone is using the same formatter, there will not be any "stylistic" comments
in code review and no unnecessary diffs if two people work on the same module.

There are several code formatters for Python code:


### [black](https://github.com/psf/black)
> The Uncompromising Code Formatter

Black is similar to `gofmt` - there is almost no configuration (line length is
pretty much the only thing you can configure and even that is discouraged). This
is a good thing because you don't have to synchronize configuration across
developers in the team.

When formatting it makes sure that the AST of the code did not change (it will
not break your code).

In my experiments it worked pretty well with `pycodestyle` (see Linters)
although you may have to disable some checks.

Pros:

- no need to keep config files in sync between developers
- run on save and never think about formatting again
- no need to run style checkers
- supported/owned by Python Software Foundation
- good support in IDEs (can be enabled in VSCode, has plugin in PyCharm)
- is actively developed

Cons:

- a bit unusual line length by default (88 characters)
- in tiny amount of cases the formatting could be nicer (it still makes
	sense, but I would do in differently)
- is a new project and formatting can sometimes change between versions


### [YAPF](https://github.com/google/yapf)
YAPF is developed by Google and takes a similar approach to `black` and `gofmt`
but has much more configuration options.

Pros:

- good support in IDEs (can be enabled in VSCode, has plugin in PyCharm)
- very configurable (if that's what you need)

Cons:

- is developed but still considered Alpha (since 2015)


### [autopep8](https://github.com/hhatto/autopep8)
Autopep8 fixes errors returned by `pycodestyle`. It can be configured to ignore
certain errors.


### [isort](https://github.com/timothycrosley/isort)
Another aspect of code formatting is import sorting. Isort will split imports in
a module into types (builtin, local, third party) and sort them alphabetically.

Pros:
- does its job

Cons:

- needs a bit of configuration to work well with Black (see [this
issue](https://github.com/timothycrosley/isort/issues/694#issuecomment-564261886))
- sometimes changes its mind (depending on active environemnt and available
packages) and causes diffs



## Linters
Linters are tools that analyze your code and report problems.

### [pycodestyle](https://pycodestyle.readthedocs.io/)
Check if the code conforms to PEP8 standard. Is used by `autopep8` to find
errors but can be used also with `black`.

### [pyflakes](https://github.com/PyCQA/pyflakes)
Analyzes syntax tree of modules and looks for various errors. It does not check
for stylistic errors.

It is fast but the checks it can do are more limited. Is is also
not as configurable. It is a good choice for if you need a linter to run in your
editor.


### [pylint](https://github.com/PyCQA/pylint)
From Readme:

> Static code analysis tool that looks for programming
> errors, helps enforcing a coding standard, finds code smells and suggests
> refactorings.

It is very configurable, has **a lot** of checkers (modules that check certain
things). It also has extensive documentation with HOW-TOs, tutorials and
technical reference.

Pros:

- powerful
- configurable

 Cons:

- slooow for large projects or on slow machines
- too noisy with default settings (best is to disable everything first, then
   enable only what you need). Here is an [example config](https://github.com/datawire/quark/blob/master/.pylintrc)



## Static type-checkers
Python has type annotation syntax since version [3.0](https://www.python.org/dev/peps/pep-3107/)
and support for type hints since version 3.5 in
[typing](https://docs.python.org/3.5/library/typing.html#module-typing) library.
Type annotation are not mandatory ([and never will be](https://www.python.org/dev/peps/pep-0484/#non-goals))
and any type checking is left to third party tools.

Here are some of the more well-known tools for static type checking:


### [mypy](https://mypy.readthedocs.io/)
This one feels more "official" because Guido is involved in it's development and
it lives in "python" Github organization.

It can give you some benefits even with no type annotations in your code. It is
not bulletproof and sometimes needs help but it does catch errors.


### [pyre](https://pyre-check.org/)
Pyre is developed by Facebook but I have not tried it.


### [pyright](https://github.com/microsoft/pyright)
Pyright is developed by Microsoft but its Readme states:
> Pyright is a side project with no dedicated team. There is
no guarantee of continued development on the project. If you find it useful,
feel free to use it and contribute to the code base.



## Other tools
Here are some tools that don't belong in any of the categories. Although
interesting, most of these tools are not well known or very mature:

- [jedi](https://github.com/davidhalter/jedi) - autocompletion and static
analysis library
	- can be integrated with many different editors (Vim, Emacs, Sublime,
	VSCode,...)
- [rope](https://github.com/python-rope/rope) - renaming/refactoring
	- only partial Python3 support
- [Vulture](https://github.com/jendrikseipp/vulture) - finds unused code
- mccabe - code complexity measure
- dodgy - looks for things that  should not be in the code
	- SCM diff checkings, passwords, secret keys, etc.
- [bandit](https://bandit.readthedocs.io/)
	- looks for security issues by applying a predefined set of tests
- [eradicate](https://github.com/myint/eradicate) - removes commented-out code



## Tool bundles
There are a couple of projects that bundle several tools togehter:

- [prospector](https://github.com/PyCQA/prospector)
	- Pylint, pyflakes, pycodestyle, mccabe, dodgy and some others by default
	- also supports Vulture and mypy
- [Flake8](http://flake8.pycqa.org/en/latest/)
	- PyFlakes, pycodestale, mccabe
- [pylama](https://pylama.readthedocs.io/)
	- pycodestyle, pydocstyle, pyflakes, mccabe, pylint and some other tools



## IDEs
All mentioned tools can be used by themselves from command-line or CI/CD (see
below), but mostly we want to have them run in real time while we are writing
code. We are not cave-people banging rocks together - everyone should use some
kind of IDE.


### PyCharm
PyCharm has its own language server that implements intellisense, refactoring,
linting, import sorting etc. But it has support for "external tools" that will
be run from inside the IDE.

### Visual Studio Code
VSCode has great [support for Python](https://code.visualstudio.com/docs/python/python-tutorial).
It also has its own language server, but it integrates external tools for
different tasks:

- Formatting
	- `autopep8` is enabled by default, but `black` can be enabled in settings
- `isort` is used by default for import sorting
- `pylint` is enabled by default but other linters can be used enabled:
	- Flake8
	- mypy
	- pycodestyle
	- prospector
	- pylama
	- bandit


### (Neo)vim
Vim is not an IDE, but it can be setup for Python development pretty well.
Here are [some](https://medium.com/@hanspinckaers/setting-up-vim-as-an-ide-for-python-773722142d1d)
[resources](https://github.com/rapphil/vim-python-ide/) on how to do that.
[Here](https://github.com/Luminaar/dotfiles/blob/master/nvim/init.vim) is my setup.

It is a lot of work but it can be done. I'm using Vim for Python development
every day at work.



# Using Python tools

## What are we using?
Over time and after some discussion our team settled on following tools (by
settled I mean that most of us are using them and we recommend them to
newcomers):

- `black` for code formatting
- `isort` configured to work with black
- `pylint` and `pycodestyle` with configuration in our package definition (more
    on that later)
- optionally `mypy` (we are using type annotations in our code)

What is not completely clear is how to best "enforce" usage of those tools.

## How to use the tools
There are two main use-cases:

- local development
- centralized checks in CI

When I'm writing code, I want it to be formatted (`black`, `isort`) and I want
my IDE to catch errors as I'm making them (`pylint`, language server).

After pushing my code, I want CI system to check that the code adheres to our
coding standard (so that reviewers don't need to waste time checking my
formatting) and check that there are no errors (run tests and static analysis).

I want the centralized checks to be handled for me so that I don't have to worry
about (or forget) setting them up with each new project. But I also would like
to be able run the same checks locally to catch any errors before I push my code
(so I don't have to wait for a build to fail).

So the requirements are:

1. some tools integrated with the editor
2. centralized checks in CI that do not depend on developers remembering to set
    them up
3. ability to run the same checks locally


### Tools integrated with the editor
This is not something that we as a team can control directly. Everyone uses
different editors and environment. What we have done is agreeing on a common set
of tools which everyone should use.

We have a document called `Python Stack` that contains this information. This
document is a kind of a decision log for us. It is also useful for beginners and
newcomers in our team.


### Centralized checks in CI
As a team we have decided what checks will be run in CI (Teamcity in our case)
and we are letting the system enforce it. Because each project in Teamcity is
created from a template, we don't need to worry about setting the checks up
ourselves.

These checks require some configuration and with that comes a question of where
to put it. In our team we put all our code in Python packages that have a
`setup.cfg` file. This file can be used to store configuration for `pylint`,
`pycodestyle` and many other tools.

To make packaging more comfortable, we use [cookicutter
templates](https://cookiecutter.readthedocs.io/). That way configuration is the
same for all projects but can be customized if needed. Checks in Teamcity then
rely on this configuration. This is a compromise between centralized control and
freedom to customize things.

Here is an example of a package configuration (from my [personal
project](https://github.com/Luminaar/k8secret) but it is based on what we use in
production).

`setup.py` looks like this:

```python
from setuptools import setup

setup()
```

and `setup.cfg` file looks like this:

```cfg
# ...

[options]

setup_requires =
	pytest-runner >= 5.0, <6.0

# ...

tests_require =
    pytest >=5.0, <6.0
    pytest-cov >=2.8.1, <3.0
    pytest-pylint >=0.14.1, <1.0
    pytest-pycodestyle >=2.0.0, <3.0

# ...

[aliases]
test=pytest

[tool:pytest]
addopts = --verbose --pylint --pylint-rcfile=setup.cfg --cov=k8secrets --cov-report html --pycodestyle

[pycodestyle]
# Black tries to enforce 88 characters but will leave
# long strings unchanged. We leave some room for that
max-line-length=120
ignore=E4,E7,W3

# Configuration for pylint
[MASTER]
ignore=CVS
good-names=logger,e,i,j,n,m,f,_

[MESSAGES CONTROL]
disable=all
enable=unused-import,
       fixme,
       useless-object-inheritance,
       unused-variable,
       unused-argument,
       unexpected-keyword-arg,
       string,
       unreachable,
       invalid-name,
       logging-not-lazy,
       unnecesary-pass
```


### Running CI checks locally
If you look at the package configuration you will see a lot of different
`pytest` related dependencies.

`pytest-runner` allows us to run tests with `setuptools` like this:

`python setup.py test`

This will install the package and its dependencies and run tests. This is done
independently in its own environment.

`pytest-cov`, `pytest-pylint` and `pytest-pycodestyle` are plugins that run code
coverage, pylint and pycodestyle respectively, together with tests.

This works both locally and in Teamcity, so you can run CI checks before pushing
your code. One option is to add a pre-commit hook to the Git repository that
will not allow commiting code that did not pass the checks. This is up to each
developer and needs to be done for each project. There are some tools that help
with this, such as [pre-commit.com](https://pre-commit.com/).

One issue with setup that I personally have is, that I always run my tests with
setuptools (`python setup.py test`) and that runs both tests and linters
every time. I haven't found a good solution yet. For now I just turn off the
linters temporarily (I run linters with the same settings right in my editor).
This is of course not ideal, because I can easily forget to turn the linters back
on and they will not run in CI.

# Conclusion
There really isn't one. I've described some tools and hove we use some of them
in our team. There is still a lot that can be improved and that will happen
incrementally over time. For now, we are happy with how everything works.
