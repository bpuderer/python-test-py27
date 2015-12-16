# python_test
Demonstration of python's [unittest](https://docs.python.org/2/library/unittest.html) module.


*httpsim.py* - http get returns a simple JSON document, post responds with a 201, put and delete respond with a 404, runs on localhost:1234 by default

*test_example.py* - example tests using the sim, requires requests module and the httpsim.py to be running on localhost:1234

*asserts.py* - assertion examples

*custom_assertions.py* - custom assertion definition and a couple of tests

Some ways the tests can be run:

`python test_example.py`

`python test_example.py UnitTestExample.test_book_retrieval`

`python -m unittest discover`

`nosetests`

`nosetests --with-xunit`
