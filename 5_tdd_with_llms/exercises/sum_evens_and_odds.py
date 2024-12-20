def sum_evens_and_odds(items: list) -> dict:
    """ Sum Evens and Odds
    
    Write a function that takes a list of numbers 
    and returns a dictionary with sums of the even and odd numbers in the list.

    Parameters: 
        items: list of numbers to search

    Returns -> dict: the sum the evens and the sum of odds number in the list

    Raises:
      AssertionError: if input is not a list or contains strings
      ValueError: if list is empty

    Examples:
        >>> sum_evens_and_odds([2, 3, 4, 7])
        {'even': 6, 'odd': 10}
        
        >>> sum_evens_and_odds([-1, -2, -3, -4])
        {'even': -6, 'odd': -4}
        
        >>> sum_evens_and_odds([1.5, 2.5, 3.5, 4.5])
        {'even': 0, 'odd': 0}
    """
    # Ensure input is a list
    assert isinstance(items, list), "Input must be a list"
    
    # Ensure list is not empty
    if not items:
        raise ValueError("List cannot be empty")
    
    # Ensure all elements in the list are numbers
    for item in items:
        if not isinstance(item, (int, float)):
            raise AssertionError("All elements in the list must be numbers")
    
    # Calculate sums of even and odd numbers
    even_sum = 0
    odd_sum = 0
    for num in items:
        # Check if the number is an integer to classify as even/odd
        if isinstance(num, int):
            if num % 2 == 0:
                even_sum += num
            else:
                odd_sum += num
    
    return {'even': even_sum, 'odd': odd_sum}
