import unittest

from ..sum_evens_and_odds import sum_evens_and_odds
class TestSumEvensAndOdds(unittest.TestCase):

    def test_mixed_integers(self):
        """Test with a mix of positive integers"""
        self.assertEqual(sum_evens_and_odds([2, 3, 4, 7]), {'even': 6, 'odd': 10})

    def test_negative_integers(self):
        """Test with a mix of negative integers"""
        self.assertEqual(sum_evens_and_odds([-1, -2, -3, -4]), {'even': -6, 'odd': -4})

    def test_floats(self):
        """Test with float numbers only"""
        self.assertEqual(sum_evens_and_odds([1.5, 2.5, 3.5, 4.5]), {'even': 0, 'odd': 0})

    def test_empty_list(self):
        """Test with an empty list"""
        with self.assertRaises(ValueError):
            sum_evens_and_odds([])

    def test_non_list_input(self):
        """Test with input that is not a list"""
        with self.assertRaises(AssertionError):
            sum_evens_and_odds("not a list")

    def test_non_numeric_items(self):
        """Test with list containing non-numeric items"""
        with self.assertRaises(AssertionError):
            sum_evens_and_odds([2, 'three', 4])

    def test_mixed_floats_and_integers(self):
        """Test with a mix of floats and integers"""
        self.assertEqual(sum_evens_and_odds([2, 3.5, 4, 7.1]), {'even': 6, 'odd': 0})

    def test_all_zeros(self):
        """Test with a list of zeros"""
        self.assertEqual(sum_evens_and_odds([0, 0, 0]), {'even': 0, 'odd': 0})

    def test_single_even(self):
        """Test with a single even number"""
        self.assertEqual(sum_evens_and_odds([2]), {'even': 2, 'odd': 0})

    def test_single_odd(self):
        """Test with a single odd number"""
        self.assertEqual(sum_evens_and_odds([3]), {'even': 0, 'odd': 3})

if __name__ == "__main__":
    unittest.main()
