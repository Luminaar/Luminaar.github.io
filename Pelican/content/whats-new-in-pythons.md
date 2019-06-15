Title: Python - what is new in which version?
Date: 2019-06-10 15:17:58
Category: Python
Tags: python, python3
Summary: A summary of new features and improvements in Python versions from 3.5 to 3.8

In this post I would like to summarize which features can be used in which
Python3 versions. I only choose features and changes that are relevant or
interesting to me. There is a link to "What's new" page for each version where
you can find the full list.

## Python 3.5
Released in September 2015. Comes pre-installed on Debian 9 (Stretch) and Ubuntu
16.04. Complete list of changes is [here](https://docs.python.org/3.5/whatsnew/3.5.html).

### New syntax
Coroutines can now be defined with `async` keyword, `await` keyword.  In this
version these keywords are not reserved yet. They will be become proper reserved
keywords in Python 3.7.

`async` can also be used in [async
for](https://docs.python.org/3.5/reference/compound_stmts.html#async-for) and
[async
with](https://docs.python.org/3.5/reference/compound_stmts.html#async-with)
statements for asynchronous `for` loops and context managers.

### New library modules
[typing](https://docs.python.org/3.5/library/typing.html#module-typing) module
adds support for Type Hints ([PEP484](https://www.python.org/dev/peps/pep-0484/)).

Syntax for function annotation was introduced back in Python3.0
([PEP3107](https://www.python.org/dev/peps/pep-3107/)). This module provides
some standard tools (such as types - Any, Union, Tuple, Callable, etc. - that
can be used in type annotations).

[zipapp](https://docs.python.org/3.5/library/zipapp.html#module-zipapp) provides
tools to manage the creation of zip files containing Python code, which can be
executed directly by the Python interpreter.

### Improvements in stdlib
[collections.OrderedDict](https://docs.python.org/3.5/library/collections.html#collections.OrderedDict)
is significantly faster now.

`os` module has a new function -
[scandir()](https://docs.python.org/3.5/library/os.html#os.scandir)
- for [better and faster way of directory
  traversal](https://docs.python.org/3.5/whatsnew/3.5.html#whatsnew-pep-471).


## Python 3.6
Released in December 2016. Comes pre-installed on Ubuntu 18.04. Complete list
of changes is [here](https://docs.python.org/3.8/whatsnew/3.6.html).

### New syntax
Formatted string literals
([f-strings](https://docs.python.org/3.6/reference/lexical_analysis.html#f-strings)).
Defined in [PEP498](https://www.python.org/dev/peps/pep-0498/).

```python
>>> name = "Max"
>>> print(f"Hello, {name}!")
Hello, Max!
```

Support for variable type hints
([PEP526](https://www.python.org/dev/peps/pep-0498/)).


Underscores in numeric literals: `1_000_000`
([PEP515](https://www.python.org/dev/peps/pep-0515/)).


Asynchronous generators ([PEP525](https://www.python.org/dev/peps/pep-0525/))
and comprehensions ([PEP530](https://www.python.org/dev/peps/pep-0530/)).

### New library modules
[secrets](https://docs.python.org/3.8/library/secrets.html#module-secrets) for
generating cryptographically strong random numbers suitable for managing data
such as passwords, account authentication, security tokens, and related secrets.
Described in [PEP506](https://www.python.org/dev/peps/pep-0505/).

### Implementation improvements
The new implementation of dictionaries is 20% to 25% smaller and preserves
insertion order (but this **should not** be relied upon yet).
See this great [talk by Raymond Hettinger](https://www.youtube.com/watch?v=p33CVV29OG8)
in which he explains how dictionaries changed over time.

### Improvements in stdlib
[asyncio](https://docs.python.org/3.8/library/asyncio.html#module-asyncio) is no
longer provisional and the API is considered stable.

A new [file system path protocol](https://docs.python.org/3.8/whatsnew/3.6.html#whatsnew36-pep519) added
to support [path-like object](https://docs.python.org/3.8/glossary.html#term-path-like-object).

The [datetime](https://docs.python.org/3.8/library/datetime.html#module-datetime)
module has gained support for [Local Time Disambiguation](https://docs.python.org/3.8/whatsnew/3.6.html#whatsnew36-pep495).

[json](https://docs.python.org/3.8/library/json.html) functions `load()` and
`loads()` now support binary input.

New function [random.choices()](https://docs.python.org/3.8/library/random.html#random.choices)
returns a list of elements of specified size from the given population with
optional weights.

Class `unittest.mock.Mock` has new methods `assert_called` and
`assert_called_once`.

## Python 3.7
Released in June 2018. Comes pre-installed on Debian 10 (Buster) and  Ubuntu
18.04 and 19.04. Complete list of changes is
[here](https://docs.python.org/3.8/whatsnew/3.7.html).

### New syntax features
Postponed evaluation of type annotations
([PEP526](https://www.python.org/dev/peps/pep-0526/)).

* Annotations can now support forward references
* Annotations are cheaper and faster to store

`async` and `await` are now reserved keywords.

### New library modules
[dataclasses](https://docs.python.org/3.8/library/dataclasses.html#module-dataclasses)
provides a decorator and functions for automatically adding generated special
methods such as `__init__()` and `__repr__()` to user-defined classes. It is useful
when you need to create a simple class that only holds data but has no
behaviour.

### New built-in features
[breakpoint()](https://docs.python.org/3.8/library/functions.html#breakpoint) function for debuggers.

Dictionaries now officially preserve insertion order of elements.

### Improvements in stdlib
[asyncio](https://docs.python.org/3.8/library/asyncio.html#module-asyncio)
received a lot of new features and improvements (high-level `asyncio.run()`
function for running coroutines, many others).

[time](https://docs.python.org/3.8/library/time.html#module-time) module now has
support for [nanosecond resolution](https://docs.python.org/3.8/whatsnew/3.7.html#whatsnew37-pep564).

### Deprications
Debian 8, Ubuntu 16, CentOS 7.5 and other platforms that use OpenSSL 0.9.8 and
1.0.1 are no longer supported. At least OpenSSL 1.0.2 is required. You can build
Python3.7 on those platforms but you have to manually link a new OpenSSL
version.

## Python 3.8
Will be released sometime in 2019. Will come pre-installed on Debian 9, Ubuntu
19.04. Complete list of changes is [here](https://docs.python.org/3.8/whatsnew/3.8.html).


### New syntax
[Assignment expressions](https://www.python.org/dev/peps/pep-0572/) (the "walrus operator", `:=`):

```python
if (n := len(a)) > 10:
    print(f"List is too long ({n} elements, expected <= 10)")
```

[Positional only arguments](https://www.python.org/dev/peps/pep-0570/): There is
new syntax (`/`) to indicate that some function parameters must be specified
positionally.

```python
def pow(x, y, z=None, /):
    r = x**y
    if z is not None:
        r %= z
    return r
```

This is in addition to [keyword only
arguments](https://www.python.org/dev/peps/pep-3102/).

### Library improvements
`json.tool` has a new option (`--json-lines`) to parse every input line as
separate JSON object.

New class `unittest.mock.AsyncMock` for asynchronous mocking.
