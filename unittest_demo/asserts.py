import unittest


class AssertionExamples(unittest.TestCase):

    def test_lists_exact(self):
        list_a = [0, 1]
        list_b = [0, 1]
        #lists must be exactly the same
        #assertEqual calls type specific equality function
        #if args are the same type in python 2.7
        self.assertEqual(list_a, list_b)

    def test_lists_order(self):
        list_a = [0, 1]
        list_b = [1, 0]
        #same elements in same quantity but order not checked
        self.assertItemsEqual(list_a, list_b)

    def test_lists_dupes(self):
        list_a = [0, 1, 2]
        list_b = [2, 2, 1, 2, 0, 0, 1]
        #set contents are unordered and unique
        self.assertEqual(set(list_a), set(list_b))


if __name__ == '__main__':
    unittest.main(verbosity=2)
