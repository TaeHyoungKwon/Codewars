```python
def high(x):
    return max(x.split(), key=lambda x:sum(ord(c) - ord('a') + 1 for c in x))
```

```python
from string import ascii_lowercase

s = {c: i for i, c in enumerate(ascii_lowercase, 1)}

def score(word):
    return sum(s[c] for c in word)

def high(x):
    return max(x.split(), key=score)
```