def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    freq = {}
    for char in phrase:
      freq[char] = (freq[char] + 1 if char in freq else 1)
    return freq

print(multiple_letter_count('yay'))
print(multiple_letter_count('Yay'))