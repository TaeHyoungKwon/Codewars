```python
def pattern(n):
    return '\n'.join(''.join(str(j) for j in range(n, i, -1)) for i in range(n))
```


```python
def pattern(n):
    pat = map(str, xrange(n, 0, -1))
    return "\n".join("".join(pat[:i]) for i in xrange(n, 0, -1))
```