```python
def capitalize(s):
    s = ''.join(c if i%2 else c.upper() for i,c in enumerate(s))
    return [s, s.swapcase()]
```

```python
def capitalize(s):
    result = ['','']
    for i,c in enumerate(s):
        result[0] += c.lower() if i % 2 else c.upper()
        result[1] += c.upper() if i % 2 else c.lower()
    return result
```