```python
from math import hypot
from itertools import combinations


def furthestDistance(arr):
    pairs = combinations(arr, 2)
    distances = (hypot(a[0]-b[0], a[1]-b[1]) for a, b in pairs)
    furthest = max(distances)
    return round(furthest, 2)
```

```python
from itertools import combinations

def furthestDistance(arr):
    return round(max( sum((y-x)**2 for x,y in zip(*comb))**.5 for comb in combinations(arr, 2)), 2)
```

```python
from itertools import combinations
from math import hypot

def furthestDistance(arr):
    result = [hypot(a[0] - b[0], a[1] - b[1]) for a, b in combinations(arr, 2)]
    return round(max(result), 2)
```