```python
def comp(array1, array2):
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False
```

```python
def comp(a1, a2):
    return None not in (a1,a2) and [i*i for i in sorted(a1)]==sorted(a2)
```