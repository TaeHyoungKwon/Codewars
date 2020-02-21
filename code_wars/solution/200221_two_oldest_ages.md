```python
def two_oldest_ages(ages):
    return sorted(ages)[-2:]
```

```python
from heapq import nlargest

def two_oldest_ages(ages):
    return sorted(nlargest(2,ages))
```

```python
two_oldest_ages = lambda a: sorted(a)[-2:]
```