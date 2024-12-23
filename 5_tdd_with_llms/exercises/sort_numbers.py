"""Sort Numbers

Write a function that takes in a list of numbers
It will return a new list with the same numbers from lowest to highest
-> this function does not have side effects
"""

def sort_numbers(input_list: list) -> list:
  """ This function takes a list of numbers and sort it from lowest to highest
    
    Parameters:
      list [int, float] : the list can contain numbers which can be either integers or floats
    
    Returns:
      list: this list will contain sorted numbers from lowest to highest.add()
    
    Raises:
      AssertionError: if the list is empty
      AssertionError: if the list contains string
      AssertionError: if the parameter is not a list
      
    >>> sort_numbers([3,5,2])
    [2,3,5]
    
    >>> sort_numbers([2.5, 6.4, 1.6, 7]) 
    [1.6, 2.5, 6.4, 7]
    
    >>> sort_numbers([-5,-10,7,0])
    [-10, -5, 0 ,7]
  """
  
  assert all(isinstance(item, (int, float)) for item in input_list), 'Items in the list must be numbers; integers or floats'
  assert len(input_list) > 0, 'Empty lists can not be sorted'
  
  return sorted(input_list)
