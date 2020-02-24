```python
def index_equals_value(arr):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = lo + hi >> 1
        if arr[mid] >= mid:
            hi = mid
        else:
            lo = mid + 1
    return lo if lo < len(arr) and arr[lo] == lo else -1
```

```python
def f(xs, l, h):
    if l > h:
        return -1
    i = (l + h) // 2
    if i > xs[i]:
        return f(xs, i+1, h)
    j = f(xs, l, i-1)
    return j if j >= 0 else (i if i == xs[i] else -1)

def index_equals_value(xs):
    return f(xs, 0, len(xs)-1)
```