import pytest


@pytest.fixture(scope='module')
def conftest_module_setup(request):
    print '\nconftest_module_setup'
    def conftest_module_teardown():
        print '\nconftest_module_teardown'
    request.addfinalizer(conftest_module_teardown)

@pytest.fixture()
def conftest_function_setup():
    print '\nconftest_function_setup'
