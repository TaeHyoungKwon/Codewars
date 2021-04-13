```python
def distinct(seq):
    return sorted(set(seq), key = seq.index)
```

```python
from collections import OrderedDict
def distinct(seq):
    return list(OrderedDict.fromkeys(seq))
```

```python
def distinct(seq):
    return list(dict.fromkeys(seq))
```