```python
from itertools import cycle, islice

def stringy(size):
    return ''.join(islice(cycle('10'), 0, size))
```

```python
def stringy(size):
    return ''.join('1' if i % 2 != 1 else '0' for i in range(size))
```