# python_test
Demonstration of [unittest](https://docs.python.org/2/library/unittest.html) and [behave](http://pythonhosted.org/behave/) ([BDD](https://en.wikipedia.org/wiki/Behavior-driven_development) python style).


## unittest_demo

*httpsim.py* - http get returns a simple JSON document, post responds with a 201, put and delete respond with a 404, runs on localhost:1234 by default

*test_example.py* - example tests using the sim, requires requests module and httpsim.py running on localhost:1234

*test_asserts.py* - assertion examples

*test_custom_assertions.py* - custom assertion definition, one of the test fails to show the AssertionError generated

Some ways the tests can be run:

`python test_example.py`

`python test_example.py UnitTestExample.test_book_retrieval`

`python -m unittest discover`

`nosetests`

`nosetests --with-xunit`


## behave_demo

*bookapi.feature* - contains feature scenarios

*environment.py* - code that runs before/after certain events during test execution

*httpsim.py* - http get to retrieve books or a single book, post to create a book, delete to delete all books or a single book, runs on localhost:1234 by default

*steps/bookapi.py* - step implementations for the scenarios

With httpsim.py running on localhost:1234, run:

`behave`
