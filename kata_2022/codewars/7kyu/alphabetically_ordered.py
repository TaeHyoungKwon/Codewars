"""
# Best Practices

def alphabetic(s):
    return sorted(s) == list(s)


def alphabetic(s):
    return all(a<=b for a,b in zip(s, s[1:]))

"""


def alphabetic(s):
    nums = list(map(ord, s))
    return all(front <= back for front, back in zip(nums, nums[1:]))


