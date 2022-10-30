from collections import Counter

def absent_vowel(x):
    result = {k.lower() for k in Counter(x) if k in "aeiouAEIOU"}
    return list(set("aeiou") - result)[0]