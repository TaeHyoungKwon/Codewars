```python
def power_of_two(x):
    return x != 0 and ((x & (x - 1)) == 0)
```

```python
def power_of_two(num):
    return bin(num).count('1') == 1
```

```python
def power_of_two(x):
    return x and (not(x&(x-1)))
```

```python
import math

def power_of_two(x):
    while x > 1:
        x, r = divmod(x, 2)
        if r:
            return False
    return x == 1
```