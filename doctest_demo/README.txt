doctest_example module
======================

Using doctest_example
---------------------

This README is used to demo doctest verifying interactive python contained in a text file.

The entire file is treated as one big docstring.

The tests can be executed by running 'python -m doctest -v README.txt' or with testfile():

import doctest
doctest.testfile('README.txt')

with verbose output:

import doctest
doctest.testfile('README.txt', verbose=True)

>>> from doctest_example import findall_lod
>>> findall_lod([{'a': 1}, {'a': 1}], 'a', 1)
[{'a': 1}, {'a': 1}]
>>> findall_lod([{'a':1}, {'a':2}], 'a', 2)
[{'a': 2}]
>>> findall_lod([{'a': 1}, {'a': 2}], 'a', 3)
[]
>>> findall_lod([{'a': 1}, {'a': 2}], 'a', '1')
[]
>>> findall_lod([{'a': 1}, {'a': 2}], 'b', 1)
Traceback (most recent call last):
    ...
KeyError: 'b'

fin
