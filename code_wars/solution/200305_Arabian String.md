```python
import re


def camelize(s):
    return ''.join(word[0].upper() + word[1:].lower() for word in re.findall(r'(?i)[a-z\d]+', s))
```

```python
import re

def camelize(s):
    return "".join([w.capitalize() for w in re.split("\W|_", s)])
```

```python
import re

def camelize(s):
    return "".join(map(str.capitalize, re.split("\W|_", s)))
```


```python
import re
def camelize(s):
    return "".join(map(str.capitalize, re.findall(r"[a-zA-Z0-9]+", s)))
```


```python

```