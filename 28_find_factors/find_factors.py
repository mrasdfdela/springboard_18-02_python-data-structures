def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    eval_nums = list(range(1,int(num/2)+1))
    eval_nums.append(num)
    return [i for i in eval_nums if num % i == 0]

print(find_factors(10))
print(find_factors(11))
print(find_factors(111))
print(find_factors(321421))