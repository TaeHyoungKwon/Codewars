```python
def find_longest(xs):
    return max(xs, key=lambda x: len(str(x)))
```

```python
def find_longest(arr):
    arr.sort(reverse=True) 
    return arr[0]
```