```python
def max_multiple(divisor, bound):
    return bound - (bound % divisor)
```

```python
def max_multiple(divisor, bound):
    return bound // divisor * divisor
```