```python
import re

def solve(s):
    return max(sum(ord(c)-96 for c in subs) for subs in re.split('[aeiou]+', s))
```

```python
import re
import string

scores = {c: i for i, c in enumerate(string.ascii_lowercase, 1)}

def solve(s):
    return max(sum(map(scores.get, x)) for x in re.findall('[^aeiou]+', s))
```