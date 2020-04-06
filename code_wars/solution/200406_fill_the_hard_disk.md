```python
from itertools import accumulate

def save(sizes, hd):
    i = 0
    for i, acc in enumerate(accumulate(sizes), 1):
        if acc > hd:
            return i-1
    return i
```

```python
def save(sizes, hd): 
    for i,s in enumerate(sizes):
        if hd < s: return i
        hd -= s
    return len(sizes)
```

```python
from itertools import *

def save(sizes, hd): 
    return sum(1 for _ in takewhile(hd.__ge__, accumulate(sizes)))
```