import unittest
from ..sort_numbers import sort_numbers 


class TestSortNumbers(unittest.TestCase):
  
  def test_integers(self):
    self.assertEqual(sort_numbers([3,5,2]), [2,3,5])

  def test_integers_negatives(self):
    self.assertEqual(sort_numbers([-5,-10,7,0]), [-10, -5, 0 ,7])
    
  def test_floats(self):
    self.assertEqual(sort_numbers([2.5, 6.4, 1.6, 7]), [1.6, 2.5, 6.4, 7])
    
  def test_empty_list(self):
    """Test with an empty list"""
    with self.assertRaises(AssertionError):
      sort_numbers([])
      
  def test_non_list_input(self):
    """Test with input that is not a list"""
    with self.assertRaises(AssertionError):
        sort_numbers("not a list")

def test_non_numeric_items(self):
    """Test with list containing non-numeric items"""
    with self.assertRaises(AssertionError):
        sort_numbers([2, 'three', 4])
