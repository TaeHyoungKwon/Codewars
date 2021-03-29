```python
def twos_difference(a):
    s = set(a)
    return sorted((x, x + 2) for x in a if x + 2 in s)
```

```python
def twos_difference(lst): 
    matches = []
    for n in sorted(lst):
        if((n + 2) in lst):
            matches.append((n, n+2))
    return matches
```