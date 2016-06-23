import pytest


#use fixture in conftest.py
def test_conftest1(conftest_module_setup):
    print 'TEST test_conftest1'

@pytest.mark.usefixtures('conftest_module_setup', 'conftest_function_setup')
def test_conftest2():
    print 'TEST test_conftest2'
