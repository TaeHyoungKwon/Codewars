```python
def sum_of_n(n):
    return [(-1 if n < 0 else 1) * sum(xrange(i+1)) for i in xrange(abs(n)+1)]
```