```python
import re

def triple_double(num1, num2):
    matched = re.search(r'(.)\1\1', str(num1))
    if not matched:
        return 0
    return matched.group(1) * 2 in str(num2)
```

```python
def triple_double(num1, num2):
    return any([i * 3 in str(num1) and i * 2 in str(num2) for i in '0123456789'])
```

```python
def triple_double(num1, num2):
    for x in range(10):
        if str(x) * 3 in str(num1):
            if str(x) * 2 in str(num2):
                return 1
    return 0
```