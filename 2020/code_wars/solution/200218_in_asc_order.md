```python
def in_asc_order(a):
    return all(x < y for x, y in zip(a, a[1:]))
```

```python
in_asc_order = lambda l: sorted(l) == l
```


```python
def in_asc_order(arr):
    return next((False for i in range(1, len(arr[1:])+1) if not arr[i] > arr[i-1]), True)
```

```python
def in_asc_order(arr):
    return {a<=b for a,b in zip(arr,arr[1:])} == {True}
```