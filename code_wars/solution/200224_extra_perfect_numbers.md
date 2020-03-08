```python
def extra_perfect_number(n):
    n = format(n, 'b')
    return n[0] == n[-1] == '1'

def extra_perfect(n):
    return list(filter(extra_perfect_number, range(1, n+1)))
```
