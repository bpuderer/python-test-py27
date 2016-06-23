import pytest


@pytest.fixture(scope='module', autouse=True)
def module_setup(request):
    print '\nmodule_setup'
    def module_teardown():
        print '\nmodule_teardown'
    request.addfinalizer(module_teardown)

@pytest.fixture(scope='function')
def function_setup(request):
    print 'function_setup'
    def function_teardown():
        print '\nfunction_teardown'
    request.addfinalizer(function_teardown)


def test_one(function_setup):
    print 'TEST test_one'

def test_two():
    print '\nTEST test_two'
