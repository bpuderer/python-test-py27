# python_test
requires requests module

httpsim.py - http get returns a simple JSON document, post responds with a 201, put and delete respond with a 404

test_example.py - example tests using the sim

asserts.py - assertion examples

custom_assertions.py - custom assertion example and a couple of tests


python -m unittest discover
nosetests
nosetests --with-xunit
