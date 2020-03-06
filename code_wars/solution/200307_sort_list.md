```python
import operator

def sort_list(sort_key, l):
  return sorted(l,key=operator.itemgetter(sort_key), reverse=True)
```

```python
def sort_list(sort_key, l):
  return sorted(l, key=lambda x: -x[sort_key])
```

```python
from operator import itemgetter
def sort_list(sort_by, lst):
  return sorted(lst, reverse=True, key=itemgetter(sort_by))
```