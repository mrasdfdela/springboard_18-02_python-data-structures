def frequency(lst, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """
    count = {search_term:0}
    for el in lst:
      if el == search_term:
        count[el] += 1
        
    return count[search_term]


print(frequency([1, 4, 3, 4, 4], 4))
print(frequency([1, 4, 3], 7))
