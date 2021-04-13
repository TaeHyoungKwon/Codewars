```python
def cyclic_string(s):
    return next((i for i, _ in enumerate(s[1:], 1) if s.startswith(s[i:])), len(s))
```

```python
from itertools import cycle

def cyclic_string(s):
    i = 0
    while True:
        i = s.find(s[0], i+1)
        if i == -1: return len(s)
        if all(c1==c2 for c1,c2 in zip(cycle(s[:i]), s[i:])): return i
```

```python
def cyclic_string(s):
    length = len(s)
    for i in range(1, length + 1):
        if s in s[:i] * length:
            return i
```

```python
def cycle_at(s, n):
    prefix = s[:n]
    return all(s[i:i+n] == prefix or prefix.startswith(s[i:i+n]) for i in range(n, len(s), n))

def cyclic_string(s):
    return next(i for i in range(1, len(s)+1) if cycle_at(s, i))
```