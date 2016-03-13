import unittest


class UnitTestTemplate(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """runs before tests

        an exception here results in tests and tearDownClass not running"""
        #raise TypeError
        print "in setUpClass"
 
    @classmethod
    def tearDownClass(cls):
        """runs after tests"""
        print "in tearDownClass"

    def setUp(self):
        """setting up test"""
        print "\nin setUp"

    def tearDown(self):
        """tearing down test

        only runs if setUp succeeds"""
        print "in tearDown"

    def test_something(self):
        """test_something description

        tests must start with "test"
        """
        print "in test_something"


if __name__ == '__main__':
    unittest.main(verbosity=2)
