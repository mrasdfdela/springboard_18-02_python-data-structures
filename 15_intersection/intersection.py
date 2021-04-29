def intersection(l1, l2):
    """Return intersection of two lists as a new list::
    
        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]
        
        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]
        
        >>> intersection([1, 2, 3], [3, 4])
        [3]
        
        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """
    # l1_set = set(l1)
    # l2_set = set(l2)
    
    intersection = []
    for el in set(l1):
      if el in set(l2):
        intersection.append(el)
    return intersection


print(intersection([1, 2, 3], [2, 3, 4])) # [2, 3]
print(intersection([1, 2, 3], [1, 2, 3, 4]))  # [1, 2, 3]
print(intersection([1, 2, 3], [3, 4])) # [3]
print(intersection([1, 2, 3], [4, 5, 6])) # []
