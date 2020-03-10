```python
def draw_stairs(n):
    return '\n'.join('{:>{}}'.format('I', i+1) for i in range(n))
```