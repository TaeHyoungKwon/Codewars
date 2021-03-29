```python
def solution(a, b):
    return a+b+a if len(a)<len(b) else b+a+b
```

```python
def solution(a, b):
    return '{0}{1}{0}'.format(*sorted((a, b), key=len))
```

```python
def solution(a, b):
    short, long = sorted((a, b), key=len)
    return short + long + short
```