Title: Python tooling
Date: 2020-01-09 13:32:47
Category: Python
Tags: python
Summary:

# Outline
Goals:

- describe different classes and tools
- compare pros and cons for different tools in each class
- decide, which tools we want to use - which are mandatory
- provide a list of tools and configurations for local development
- setup tooling in CI/CD chains
	- use mandatory tools

# Classes of tools

## Formatters
Why use formatters?
PEP8 defines a code style. If everyones code looks the same, it is easier for
multiple developers work on the same code. If everyone uses the same formatter
and settings, when people collaborating there are no style related diffs in
Git.

- black - https://github.com/psf/black
	- opinionated, "uncompromising"
	- very little configuration
	- best  run as-is
	- similar philosophy as gofmt (there should be only one way to do things)
	- formatting is nice in 99% of the cases
	- Pros:
		- no need to keep config files in sync between developers
		- run on save and never think about formatting again
		- no need to run style checkers
		- supported/owned by Python Software Foundation
		- good support in IDEs (in VS Code by default)
	- Cons:
		- in tiny amount of cases the formatting could be nicer (it still makes
			sense, but I would do in differently)
- pep8ify - looks dead
- autopep8
	- relies on pycodestyle
- YAPF - https://github.com/google/yapf
	- is developed but still considered Alpha

Another aspect of code formatting is import sorting:

- isort
	- needs a bit of configuration to work well with black
- ...

## Linters
- pycodestyle - https://pycodestyle.readthedocs.io/en/latest/intro.html#configuration
	- checks if code conforms to PEP8 standard
	- could be used in CI/CD to check if the code was formatted with anything?
- pyflakes
	- included in Flake8 and other tools
	- Only analyzes syntax tree of the modules
- pylint
	- has good documentation - HOW-TOs, tutorials, technical reference,
	integration with IDEs
	- Cons:
		- slooow for large files or on slow machines
		- too noisy with default settings (best is to disable everything
		first, then enable only what you need)
			- example config - https://github.com/datawire/quark/blob/master/.pylintrc

## Static type-checkers
- mypy - https://mypy.readthedocs.io/
	- Guido is involved
	- "official", actively developed
- pyre - https://pyre-check.org/
- pyright
	- From readme: `Pyright is a side project with no dedicated team. There is
	no guarantee of continued development on the project. If you find it useful,
	feel free to use it and contribute to the code base.`


## Other
- rope - renaming/refactoring
	- only partial Python3 support
- Vulture - unused code
- mccabe - code complexity measure
- dodgy - looks for things that  should not be in the code - SCM diff checkings,
passwords, secret keys, ... (not very mature)
- bandit - https://bandit.readthedocs.io/
	- looking for security issues

## Tool bundles
There are several projects that bundle several tools togehter
- prospector
- Flake8
- pylama - https://pylama.readthedocs.io/
	- pycodestyle, pydoctyle, pyflakes, mccabe, pylint

## IDEs
Vim - good luck with that ;) Vim setup is out of scope of this
article, but it is possible (I'm using Vim for Python development every day).

PyCharm implements a lot of functionality and does not rely on external tools
for most things.

- implements it's own language server, type checking, refactoring, linting,
formatter
- has some support for other tools:
	- black plugin
	- pylint - can be used as an external tool

VSCode supports most tools

- autopep8 by default, but supports black
- uses isort for imports
- Pylint enabled by default
	- other linters supported:
		- Flake8
		- mypy
		- pycodestyle
		- prospector (combines other tools)
		- pylama
		- bandit

# Which do we mandate?
Black, isort
Pylint

# Python tooling in CI/CD workflows
When do the tools need to be run?
- Before commiting - hooks in Github? local hooks?
- In Teamcity - failing builds

https://pre-commit.com/
