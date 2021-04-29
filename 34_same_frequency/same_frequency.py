def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    (num1, num2) = (str(num1), str(num2))
    return count(num1) == count(num2)

def count(str):
  count = {}
  for char in str:
    count[char] = count.get(char, 0) + 1
  return count