def setup_module(module):
    print "\nsetup_module      module:{}".format(module.__name__)

def teardown_module(module):
    print "teardown_module   module:{}".format(module.__name__)

def setup_function(function):
    print "setup_function    function:{}".format(function.__name__)

def teardown_function(function):
    print "\nteardown_function function:{}".format(function.__name__)

def test_module_test():
    print 'test_module_test'
    assert True


class TestFixtureExample:

    @classmethod
    def setup_class(cls):
        print "setup_class       class:{}".format(cls.__name__)

    @classmethod
    def teardown_class(cls):
        print "teardown_class    class:{}".format(cls.__name__)

    def setup_method(self, method):
        print "setup_method      method:{}".format(method.__name__)

    def teardown_method(self, method):
        print "\nteardown_method   method:{}".format(method.__name__)

    def test_something1(self):
        print 'TEST test_something1'
        assert True

    def test_something2(self):
        print 'TEST test_something2'
        assert True
