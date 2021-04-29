def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """
    if command not in {'add', 'remove'} or location not in {'beginning', 'end'}:
      # print('list_manipulation: none')
      return None
    elif command == 'add':
      # print('list_manipulation: add')
      new_list = list_add(lst, location, value)
      return new_list
    elif command == 'remove':
      # print('list_manipulation: remove')
      new_list = list_remove(lst, location)
      return new_list

def list_add(lst, location, value):
  if location == 'beginning':
    lst.insert(0,value)
    return lst
  elif location == 'end':
    lst.extend([value])
    return lst

def list_remove(lst, location):
  if location == 'beginning':
    el = lst.pop(0)
    return el
  elif location == 'end':
    el = lst.pop()
    return el

lst = [1, 2, 3]

print(list_manipulation(lst, 'remove', 'end'))
# 3

print(list_manipulation(lst, 'remove', 'beginning'))
# 1

print(lst)
# [2]

# add: add item at beginning/end, and return list

lst = [1, 2, 3]

print(list_manipulation(lst, 'add', 'beginning', 20))
# [20, 1, 2, 3]

print(list_manipulation(lst, 'add', 'end', 30))
# [20, 1, 2, 3, 30]

print(lst)
# [20, 1, 2, 3, 30]

# Invalid commands or locations should return None:

print(list_manipulation(lst, 'foo', 'end') is None)
# True

print(list_manipulation(lst, 'add', 'dunno') is None)
# True
