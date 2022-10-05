"""
1. 둘중의 하나가 letter가 아니면, return -1
2. 같은 case 이면 return 1
3. 둘다 letter 이나 case가 다르면 0
"""


def same_case(a, b):
    if is_either_of_the_charters_is_not_a_letter(a, b):
        return -1

    if is_same_case(a, b):
        return 1
    else:
        return 0


def is_either_of_the_charters_is_not_a_letter(a, b):
    return not (a.isalpha() and b.isalpha())


def is_same_case(a, b):
    return is_lower(a) and is_lower(b) or is_upper(a) and is_upper(b)


def is_lower(c: str):
    return c.islower()


def is_upper(c: str):
    return c.isupper()
