Title: Python Pip --freeze, editables and git
Date: 2018-11-16 07:55:12
Category: Python
Tags: python, git
Summary: Interesting behaviour when using Pip --freeze on a locally installed package with .git directory.

When developing a Python package, the recommended practice is to install your package in editable mode. This way you can still edit your source code and run your tests on installed version of your package, without having reinstalling it each time.

Usually, your project structure will be something like this:

	My_project/
	|-- .git
	|-- my_project/
	|   |-- __init__.py
	|   |-- module.py
	|
	|-- setup.py

You can run `pip install -e .` in the top level directory to install your package locally.

After that, an interesting thing happens if you do a `pip freeze`. If there is a  `.git` directory (or a directory for other VCS), your package will be listed as follows:

	-e git+git@github.com:user/my-project.git@079d2ae797515c740a1742fc77bdcd68e577cbe5#egg=my-project

I.e. it will point to the repository of your project instead of just naming your package. I could not find a mention of this anywhere in the documentation and it surprised me at first.

Note: If there is not remote specified for your repository it will fallback to the package name and insert a comment in the output:

	## !! Could not determine repository location
