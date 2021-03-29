```python
import itertools

def solution(s):
    return [''.join(xs) for xs in itertools.zip_longest(s[::2], s[1::2], fillvalue='_')]
```

```python
import re

def solution(s):
    return re.findall(".{2}", s + "_")
```

```python
def solution(s):
    result = []
    if len(s) % 2:
        s += '_'
    for i in range(0, len(s), 2):
        result.append(s[i:i+2])
    return result
```

```python
def solution(s):
    return [s[x:x+2] if x < len(s) - 1 else s[-1] + "_" for x in range(0, len(s), 2)]
```

```python
def solution(s):
    return [(s + "_")[i:i + 2] for i in range(0, len(s), 2)]
```

```python
import re

def solution(s):
    return re.findall('..', s + '_')
```