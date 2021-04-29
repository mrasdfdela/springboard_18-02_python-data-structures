def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    new_phrase = list(phrase)
    new_phrase.reverse()
    return "".join(new_phrase)

print(reverse_string('awesome'))
print(reverse_string('sauce'))
