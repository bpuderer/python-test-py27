import unittest

class CustomAssertions:

    def assertDead(self, state):
        dead_states = ["passed on", "ceased to be", "expired", "bereft of life"]
        if state not in dead_states: 
            raise AssertionError(state + " not in " + str(dead_states))


class UseCustomAssertion(unittest.TestCase, CustomAssertions):

    def test_swallow(self):
        self.assertDead("carrying a coconut")

    def test_parrot(self):
        self.assertDead("ceased to be")


if __name__ == '__main__':
    unittest.main(verbosity=2)
