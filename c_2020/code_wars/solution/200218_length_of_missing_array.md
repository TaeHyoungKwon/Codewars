```python
def get_length_of_missing_array(arrays):
    arrays = [len(a) if a is not None else 0 for a in arrays ]
    arrays.sort()
    if 0 in arrays or len(arrays) == 0 : return 0
    for i in range(len(arrays)):
        if arrays[i+1] != arrays[i] + 1: return arrays[i]+1
```

```python
def get_length_of_missing_array(a):
    lns = a and all(a) and list(map(len, a))
    return bool(lns) and sum(range(min(lns), max(lns) + 1)) - sum(lns)
```
