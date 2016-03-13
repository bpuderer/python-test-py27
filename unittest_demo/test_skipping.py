import unittest
import platform


class UnitTestSkipping(unittest.TestCase):


    @unittest.skip("to unconditionally skip a test add this decorator")
    def test_something(self):
        """test_something description"""
        print "in test_something"

    @unittest.skipIf(platform.system() == 'Windows', 'does not run on windows')
    def test_skip_if_windows(self):
        """"test_skip_if_windows description"""
        print "in test_skip_if_windows"

    @unittest.skipUnless(platform.system() == 'Linux', 'Linux required')
    def test_skip_unless_linux(self):
        """"test_skip_unless_linux"""
        print "in test_skip_unless_linux"

    @unittest.expectedFailure
    def test_that_fails(self):
        """test_that_fails description

        failure not counted with expectedFailure decorator
        if it passes it counts as an unexpected success
        """
        self.assertTrue(False)

    def test_skip_during_test(self):
        """test_skip_during_test description"""
        print "test_skip_during_test #1"
        
        # can also be called in setUp()
        self.skipTest('detected something during test execution that should abort test')
        
        print "test_skip_during_test #2"


if __name__ == '__main__':
    unittest.main(verbosity=2)
