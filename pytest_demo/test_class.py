import pytest

class TestClass:

    def test_passes(self):
        assert True

    def test_dicts(self):
        assert {'a': 0, 'b': 1, 'c': 2} == {'a': 1, 'c': 2}

    def test_exception(self):
        with pytest.raises(ValueError):
            raise ValueError('ValueError message')
