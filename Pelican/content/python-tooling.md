Title: Python tooling
Date: 2020-01-09 13:32:47
Category: Python
Tags: python
Summary: Overview of development tools for Python


> This post is a work in progress. Don't mind the typos and other errors

When I started doing research for this post I expected it to be a much more
complicated topic (same as packaging for example). Turns out there are not that
many tools - there is almost only one way to do things.

I this post I will categorize different tools into five categories, describe and
compare them. I have tried to use almost all of the tools at least a little.
At the end I propose a way to incorporate the tools in CI/CD pipelines for
python projects.



# Formatters
[PEP8](https://www.python.org/dev/peps/pep-0008/) (Style guide for Python code)
and [PEP257](https://www.python.org/dev/peps/pep-0257/) (Docstring conventions)
are two PEPs that describe how Python code should look. The PEP8 is not meant to
be dogmatic and adhering to it is not the only necessary prerequisite for good
Python code, but it is a start.

When working in a team, it's is better when everyones code looks the same.
Ideally it shouldn't be obvious who wrote the code from just looking at it.

And because formatting code by hand is tedious, using some kind of formatter
almost a necessity. If everyone is using the same formatter, there will not be
any "stylistic" comments in code review and no unnecessary diffs if two people
work on the same module.

There are several code formatters for Python code:


## [black](https://github.com/psf/black)
> The Uncompromising Code Formatter

Black is similar to `gofmt` - there is almost no configuration (line length is
pretty much the only thing you can configure and even that is discouraged). This
is a good thing because you don't have to synchronize configuration across
developers in the team.

When formatting it makes sure that the AST of the code did not change (it will
not break your code).

In my experiments it worked pretty well with `pycodestyle` (see Linters).

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
- is a new project


## [YAPF](https://github.com/google/yapf)
YAPF is developed by google and takes a similar approach to `black` and `gofmt`
but has much more configuration options.

Pros:

- good support in IDEs (can be enabled in VSCode, has plugin in PyCharm)

Cons:

- is developed but still considered Alpha (since 2015)


## [autopep8](https://github.com/hhatto/autopep8)
Autopep8 fixes errors returned by `pycodestyle`. It can be configured to ignore
certain errors.


## [isort](https://github.com/timothycrosley/isort)
Another aspect of code formatting is import sorting. Isort will split imports in
a module into types (builtin, local, third party) and sort them alphabetically.

Pros:
- does its job

Cons:

- needs a bit of configuration to work well with Black (see [this
issue](https://github.com/timothycrosley/isort/issues/694#issuecomment-564261886))
- sometimes changes its mind and causes diffs



# Linters
Linters are tools that analyze your code and report problems.

## [pycodestyle](https://pycodestyle.readthedocs.io/)
Check if the code conforms to PEP8 standard. Is used by `autopep8` to find
errors but can be used also with `black`.

## [pyflakes](https://github.com/PyCQA/pyflakes)
Analyzes sytax tree of modules and looks for various errors. It does not check
for stylisic errors.

It is fast but the checks it can do are more limited. Is is also
not as configurable. It is a good choice for a first linter.


## [pylint](https://github.com/PyCQA/pylint)
According to the Readme: Static code analysis tool that looks for programming
errors, helps enforcing a coding standard, finds code smells and suggests
refactorings.

It is very configurable, has **a lot** of checkers. It also has extensive
documentation with HOW-TOs, tutorials and technical reference.

Pros:

- powerful
- configurable

 Cons:

- slooow for large projects or on slow machines
- too noisy with default settings (best is to disable everything first, then
   enable only what you need). Here is an [example config](https://github.com/datawire/quark/blob/master/.pylintrc)



# Static type-checkers
Python has type annotation syntax since version [3.0](https://www.python.org/dev/peps/pep-3107/)
and support for type hints since version 3.5 in
[typing](https://docs.python.org/3.5/library/typing.html#module-typing) library.
Type annotation are not mandatory ([and never will be](https://www.python.org/dev/peps/pep-0484/#non-goals))
and any type checking is left to third party tools.

Here are some of the more well-known tools for static type checking:


## [mypy](https://mypy.readthedocs.io/)
This one feels more "official" because Guido is involved in it's development and
it lives in "python" Github organization.

It can give you some benefits even with no type annotations in your code. It is
not bulletproof and sometimes needs help but it does catch errors.


## [pyre](https://pyre-check.org/)
Pyre is developed by Facebook but I have not tried it.


## [pyright](https://github.com/microsoft/pyright)
Pyright is developed by Microsoft but its Readme states:
> Pyright is a side project with no dedicated team. There is
no guarantee of continued development on the project. If you find it useful,
feel free to use it and contribute to the code base.



# Other tools
Here are some tools that don't belong in any of the categories. Although
interesting, most of these tools are not well known are very mature:

- [rope](https://github.com/python-rope/rope) - renaming/refactoring
	- only partial Python3 support
- [Vulture](https://github.com/jendrikseipp/vulture) - finds unused code
- mccabe - code complexity measure
- dodgy - looks for things that  should not be in the code
	- SCM diff checkings, passwords, secret keys, etc.
- [bandit](https://bandit.readthedocs.io/)
	- looks for security issues by applying a predefined set of tests
- [eradicate](https://github.com/myint/eradicate) - removes commented-out code



# Tool bundles
There are several projects that bundle several tools togehter

- [prospector](https://github.com/PyCQA/prospector)
	- Pylint, pyflakes, pycodestyle, mccabe, dodgy and some others by default
	- also supports Vulture and mypy
- [Flake8](http://flake8.pycqa.org/en/latest/)
	- PyFlakes, pycodestale, mccabe
- [pylama](https://pylama.readthedocs.io/)
	- pycodestyle, pydocstyle, pyflakes, mccabe, pylint and some other tools



# IDEs
All mentioned tools can be used by themselves from commandline or CI/CD (see
below), but mostly we want to have them run in real time while we are writing
code. We are not cave-people banging rocks together - everyone should use some
kind of IDE.


## PyCharm
PyCharm has its language server that implements intellisense, refactoring,
linting, import sorting etc. But it has support for "external tools" - tools
that will be run from inside the IDE.

## Visual Studio Code
VSCode has great [support for Python](https://code.visualstudio.com/docs/python/python-tutorial).
It also has its own language server, but it integrates extenal tools for
different tasks:

- Formatting
	- `autopep8` is enabled by default, but `black` can be enabled in settings
- Uses `isort` for import sorting
- `pylint` is enabled by default but other linters are enabled:
	- Flake8
	- mypy
	- pycodestyle
	- prospector (combines other tools)
	- pylama
	- bandit


## (Neo)vim
Vim is not an IDE, but it can be setup for Python development pretty well.
Here are [some](https://medium.com/@hanspinckaers/setting-up-vim-as-an-ide-for-python-773722142d1d)
[resources](https://github.com/rapphil/vim-python-ide/) on how to do that.
[Here](https://github.com/Luminaar/dotfiles/blob/master/nvim/init.vim) is my setup.

It is a lot of work but it can be done. I'm using Vim for Python development
every day at work.



# Python tooling in CI/CD workflows
Besides using tools in development, we would like to also have some checks setup
in Teamcity that enforce code quality.
