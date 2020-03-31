```python
def meeting(s):
    return ''.join(sorted('({1}, {0})'.format(*(x.split(':'))) for x in s.upper().split(';')))
```

```python
def meeting(s):
    return ''.join(f'({a}, {b})' for a, b in sorted(name.split(':')[::-1] for name in s.upper().split(';')))
```