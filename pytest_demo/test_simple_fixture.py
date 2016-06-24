import pytest


@pytest.fixture()
def setup1():
    print '\nsetup1'

@pytest.fixture()
def setup2():
    print 'setup2'

#using funcarg / funcarg mechanism
def test_1_setup1_funcarg(setup1):
    print 'test_1_setup1_funcarg()'

def test_2_no_fixtures():
    print '\ntest_2_no_fixtures()'

@pytest.mark.usefixtures('setup1')
def test_3_setup1_marker():
    print 'test_3_setup1_marker()'

#can use more than one fixture
def test_4_setup1_and_setup2(setup1, setup2):
    print 'test_4_setup1_and_setup2()'



#return something from fixture
@pytest.fixture()
def return_data():
    data = {'foo': 0, 'bar': 1}
    return data

def test_return_data(return_data):
    print '\nreturn data from return_data():', return_data
    assert return_data['bar'] == 1



#fixture calling another fixture
@pytest.fixture()
def return_dict():
    print '\nreturn_dict fixture'
    data = {'foo': 0, 'bar': 1}
    return data

@pytest.fixture()
def return_complete_dict(return_dict):
    print 'return_complete_dict fixture'
    return_dict['baz'] = 2
    return return_dict

def test_return_dict(return_complete_dict):
    assert return_complete_dict['foo'] == 0
    assert return_complete_dict['bar'] == 1
    assert return_complete_dict['baz'] == 2
