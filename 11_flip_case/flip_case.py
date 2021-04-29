def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    new_arr = []

    arr = list(phrase)
    for char in arr:
      if char.lower() == to_swap.lower():
        if char == char.lower():
          new_arr.append(char.upper())
        else:
          new_arr.append(char.lower())
      else:
        new_arr.append(char)
    
    return "".join(new_arr)

print(flip_case('Aaaahhh', 'a'))
print(flip_case('Aaaahhh', 'A'))
print(flip_case('Aaaahhh', 'h'))