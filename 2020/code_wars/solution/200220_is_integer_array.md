```python
def is_int_array(a):
    return isinstance(a, list) and all(isinstance(x, (int, float)) and x == int(x) for x in a)
```

```python
def is_int_array(arr):
    return isinstance(arr, list) and all(isinstance(e, int) or isinstance(e, float) and e.is_integer() for e in arr)
```

```python
def is_int_array(arr):
    return isinstance(arr, list) and all(map(lambda x: isinstance(x, (int,float)) and int(x)==x, arr))
```