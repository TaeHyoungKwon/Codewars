```python
def nb_dig(n, d):
    d = str(d)
    return sum(str(i**2).count(d) for i in range(n+1))

```

```python
def nb_dig(n, d):
    return ''.join(str(a ** 2) for a in xrange(n + 1)).count(str(d))
```