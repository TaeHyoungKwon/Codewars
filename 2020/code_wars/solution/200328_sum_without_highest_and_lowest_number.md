```python
def sum_array(arr):
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)
```

```python
def sum_array(arr):
    return sum(sorted(arr)[1:-1]) if arr and len(arr) > 1 else 0
```

```python
def sum_array(arr):
    return 0 if arr == None else sum(sorted(arr)[1:-1])
```