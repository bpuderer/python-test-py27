import unittest


class AssertionExamples(unittest.TestCase):

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
        # changed to assertCountEqual in python3
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

    def test_dicts_subset(self):
        dict_a = {'a': 0, 'b': 1, 'c': 2}
        dict_b = {'b': 1, 'c': 2, 'a': 0, 'bb': 11, 'cc': 22}
        # confirms all key/val pairs in first arg exist in second
        # reversing the order of the args would fail unless they're the same
        self.assertDictContainsSubset(dict_a, dict_b)

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


if __name__ == '__main__':
    unittest.main(verbosity=2)
