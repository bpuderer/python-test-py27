# python_test
Demonstration of [unittest](https://docs.python.org/2/library/unittest.html) and [behave](http://pythonhosted.org/behave/) ([BDD](https://en.wikipedia.org/wiki/Behavior-driven_development) python style).

*books_api.json* - Books API in [OpenAPI](https://github.com/OAI/OpenAPI-Specification) format

*flask_http_sim.py* - [Flask](https://github.com/mitsuhiko/flask) based implementation of Books API.  Runs on localhost:1234 by default

*http_sim.py* - BaseHTTPServer based implementation of Books API.  Runs on localhost:1234 by default


## unittest_demo

*test_example.py* - example tests using the sim, requires requests module and one of the above sims running on localhost:1234

*test_asserts.py* - assertion examples

*test_custom_assertions.py* - custom assertion definition, one of the test fails to show the AssertionError generated

*test_json_schema.py* - example validating [JSON Schema](http://json-schema.org/) using [jsonschema](https://github.com/Julian/jsonschema)

Some ways the tests can be run:

`python test_example.py`

`python test_example.py UnitTestExample.test_book_retrieval`

`python -m unittest discover`

`nosetests`

`nosetests --with-xunit`


## behave_demo

*bookapi.feature* - contains feature scenarios

*environment.py* - code that runs before/after certain events during test execution

*steps/bookapi.py* - step implementations for the scenarios

With one of the sims running on localhost:1234, run:

`behave`
