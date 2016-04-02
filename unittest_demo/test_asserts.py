import unittest


class AssertionExamples(unittest.TestCase):


    def assert_dict_contains_subset(self, a, b):
        """checks dictionary a is a subset of dictionary b"""

        missing_keys = []
        mismatched_values = {}

        for key in a:
            if key not in b:
                missing_keys.append(key)
            elif a[key] != b[key]:
                mismatched_values[key] = (a[key], b[key])

        error_msg = ''
        if missing_keys:
            error_msg += "Missing: {}".format(missing_keys)
        if mismatched_values:
            if error_msg:
                error_msg += "; "
            error_msg += "Mismatched values: {}".format(mismatched_values)

        if missing_keys or mismatched_values:
            raise AssertionError(error_msg)

    def assert_sequence_contains_subset(self, a, b):
        """checks sequence a is a subset of sequence b"""

        missing_items = [item for item in a if item not in b]
        if missing_items:
            raise AssertionError("Missing: {}".format(missing_items))


    def test_sequences_same(self):
        list_a = [0, 1, 2]
        list_b = [0, 1, 2]
        # sequences types: str, unicode, list, tuple, bytearray, buffer, xrange
        # sequences must be exactly the same
        self.assertEqual(list_a, list_b)

    def test_sequences_order_irrelevant(self):
        list_a = [0, 1, 1]
        list_b = [1, 0, 1]
        # same elements in same quantity but order not checked
        # changed to assertCountEqual in python 3
        self.assertItemsEqual(list_a, list_b)

    def test_sequences_count_irrelevant(self):
        list_a = [0, 1, 2]
        list_b = [2, 2, 1, 2, 0, 0, 1]
        # set contents are unordered and unique
        # https://docs.python.org/2/library/stdtypes.html#types-set
        self.assertEqual(set(list_a), set(list_b))


    def test_dicts_same(self):
        dict_a = {'a': 0, 'b': 1, 'c': 2}
        dict_b = {'b': 1, 'c': 2, 'a': 0}
        # dicts have exactly same key/val pairs
        self.assertEqual(dict_a, dict_b)

    def test_dicts_subset1(self):
        dict_a = {'a': 0, 'b': 1, 'c': 2}
        dict_b = {'a': 0, 'b': 1, 'c': 2, 'bb': 11, 'cc': 22}
        # confirms all key/val pairs in first exist in second
        # reversing the order of the args would fail unless they're equal
        # assertDictContainsSubset was removed from python 3.3+ with no replacement
        self.assertDictContainsSubset(dict_a, dict_b)

    def test_dicts_subset2(self):
        dict_a = {'a': 0, 'b': 1, 'c': 2}
        dict_b = {'a': 0, 'b': 1, 'c': 2, 'bb': 11, 'cc': 22}
        # confirms all key/val pairs in first exist in second
        # same test but does not use assertDictContainsSubset
        # AssertionError msg isn't very helpful however
        self.assertTrue(set(dict_a.items()).issubset(set(dict_b.items())))

    def test_dicts_subset3(self):
        dict_a = {'a': 0, 'b': 1, 'c': 2}
        dict_b = {'a': 0, 'b': 1, 'c': 2, 'bb': 11, 'cc': 22}
        # confirms all key/val pairs in first exist in second
        # another way with a custom assertion and a more useful message
        self.assert_dict_contains_subset(dict_a, dict_b)


    def test_dict_keys(self):
        dict_a = {'a': 0, 'b': 1, 'c': 2}
        expected_keys = ['a', 'c', 'b']
        # check keys in dictionary against list (of keys)
        self.assertItemsEqual(dict_a.keys(), expected_keys)
    
    def test_dict_keys_subset1(self):
        dict_a = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4}
        expected_keys = ['a', 'd', 'e']
        # check keys in list are all found in dictionary
        # AssertionError msg isn't very helpful
        self.assertTrue(set(expected_keys).issubset(set(dict_a.keys())))

    def test_dict_keys_subset2(self):
        dict_a = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4}
        expected_keys = ['b', 'd', 'e']
        # check keys in list are all found in dictionary
        # another way with a custom assertion and a more useful message
        self.assert_sequence_contains_subset(expected_keys, dict_a)


    def test_dicts_keys(self):
        dict_a = {'a': 0, 'b': 1, 'c': 2}
        dict_b = {'b': 'abc', 'c': True, 'a': 42}
        # check keys in two dictionaries are the same
        self.assertItemsEqual(dict_a.keys(), dict_b.keys())

    def test_dicts_keys_subset1(self):
        dict_a = {'a': 0, 'b': 1, 'c': 2}
        dict_b = {'b': 42, 'c': 'doctor', 'a': False, 'bb': 11, 'cc': 22}
        # check keys in first dictionary are a subset of second
        self.assertTrue(set(dict_a).issubset(set(dict_b)))

    def test_dicts_keys_subset2(self):
        dict_a = {'a': 0, 'b': 1, 'c': 2}
        dict_b = {'b': 42, 'c': 'doctor', 'a': False, 'bb': 11, 'cc': 22}
        # check keys in first dictionary are a subset of second
        # another way with a custom assertion and a more useful message
        self.assert_sequence_contains_subset(dict_a, dict_b)


    def test_membership(self):
        a_list = [42, 3.14, 1.21, 2112, 2001]
        self.assertIn(3.14, a_list)

        # assertIn/assertNotIn better than assertTrue with an expression
        # self.assertTrue(3.15 in a_list)
        # AssertionError with assertTrue: AssertionError: False is not true
        # with assertIn: AssertionError: 3.15 not found in [42, 3.14, 1.21, 2112, 2001]

        a_dict = {'key1': 'val1', 'key2': 'val2', 'key3': 'val3'}
        self.assertNotIn('key4', a_dict)

        a_str = "look at the eyebrows. these are attack eyebrows."
        self.assertIn('attack', a_str)


    def test_exception(self):
        with self.assertRaises(TypeError):
            # statements that raise exception
            raise TypeError

    def test_exception_regex(self):
        # renamed to assertRaisesRegex in python3
        with self.assertRaisesRegexp(IOError, 'No such.*idontexist.txt'):
            with open('idontexist.txt') as f:
                pass


    def test_check_all_for_failure(self):
        """tests stop after first failure but can continue with the
        subTest context manager.  it was added in python 3.4
        but has not been backported to 2.7.
        https://docs.python.org/3/library/unittest.html#distinguishing-test-iterations-using-subtests

        the code below is ugly but accomplishes something similar.
        it asserts everything in test_values and compiles the failures
        which are listed with the AssertionError.
        whether one assert fails or all of them fail, this test will
        report a single failure.
        """
        failed = False
        failures = []

        #test_values = range(12)
        test_values = range(0, 12, 2)
        for val in test_values:
            try:
                self.assertEqual(val % 2, 0)
            except AssertionError:
                failed = True
                failures.append('{} is not even'.format(val))
        if failed:
            raise AssertionError(failures)


if __name__ == '__main__':
    unittest.main(verbosity=2)
