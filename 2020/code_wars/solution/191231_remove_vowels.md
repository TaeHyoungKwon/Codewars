```python
EMOVE_VOWS = str.maketrans('','','aeiou')

def remove_vowels(s):
    return s.translate(EMOVE_VOWS)
```

```python
def remove_vowels(strng):
    return ''.join([i for i in strng if i not in 'aeiou'])
```

```python
def remove_vowels(s):
    return s.translate(None, 'aeiou')
```