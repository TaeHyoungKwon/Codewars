```python
def mxdiflg(a1, a2):
    if a1 and a2:
        return max(
            len(max(a1, key=len)) - len(min(a2, key=len)),
            len(max(a2, key=len)) - len(min(a1, key=len)))
    return -1
```

```python
def mxdiflg(a1, a2):
    if a1 and a2:
        return max(abs(len(x) - len(y)) for x in a1 for y in a2)
    return -1
```


```python
def mxdiflg(a1, a2):
    if not (a1 and a2):
        return -1
    x, y = (list(map(len, a)) for a in [a1, a2])
    return max(abs(max(x) - min(y)), abs(min(x) - max(y)))
```