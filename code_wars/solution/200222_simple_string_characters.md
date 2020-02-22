```python
from collections import Counter

def solve(s):
    counter = Counter(
        0 if c.isupper() else
        1 if c.islower() else
        2 if c.isdigit() else
        3
        for c in s
    )
    return [counter[i] for i in range(4)]
```

```python
def solve(s):
  uc, lc, num, sp = 0, 0, 0, 0
  for ch in s:
    if ch.isupper(): uc += 1
    elif ch.islower(): lc += 1
    elif ch.isdigit(): num += 1
    else: sp += 1
  return [uc, lc, num, sp]
```