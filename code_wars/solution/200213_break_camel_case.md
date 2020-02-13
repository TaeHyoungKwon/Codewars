```python
def solution(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)
```

```python
import re
def solution(s):
    return re.sub('([A-Z])', r' \1', s)
```