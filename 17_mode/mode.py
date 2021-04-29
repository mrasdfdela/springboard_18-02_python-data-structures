def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    curr = {'start':0}
    for el in nums:
      count = {el: 0}
      
      for num in nums:
        if num == el:
          count[el] += 1

      if count[el] > list(curr.values())[0]:
        curr = count
    
    return list(curr.keys())[0]
      

print(mode([1, 2, 1]))
print(mode([2, 2, 3, 3, 2]))
    
