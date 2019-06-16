Title: New Python dictionaries
Date: 2019-06-20 15:00:00
Category: Python
Tags: python, python3
Summary: How did dictionaries change in Python3.6. Are they ordered now? What does 'preserve insertion order' mean?



Changes in standard library:

- csv.DictReader uses OrderedDict in 3.7 but dict in 3.8

Relevant PEP
https://www.python.org/dev/peps/pep-0468/


How OrderedDict is different:

One answer from Raymont H. why the two will not be merged:
https://groups.google.com/d/msg/dev-python/12hGKqr4WU8/gyAV6ICTBAAJ


Details about implementation
Initial proposal by Raymond H.
https://mail.python.org/pipermail/python-dev/2012-December/123028.html

Technical overview from PyPy
https://morepypy.blogspot.com/2015/01/faster-more-memory-efficient-and-more.html


Relevant mailing list thread
https://groups.google.com/forum/#!msg/dev-python/mgKoaSFEmvk/ep3paPeECgAJ;context-place=searchin/dev-python/dict%7Csort:date

Hashing randomization, some explanation of hashing
https://groups.google.com/forum/#!searchin/dev-python/dict|sort:date/dev-python/dJeQ8w2EgLo/TGdqw8K4AQAJ

