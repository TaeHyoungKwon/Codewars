```python
from collections import Counter

def numericals(s):
    def f(s):
        cnts = Counter()
        for c in s:
            cnts[c] += 1
            yield cnts[c]
    return ''.join(map(str, f(s)))
```

```python
from collections import defaultdict

def numericals(s):
    memo = defaultdict(lambda: 1)
    result = ''
    for c in s:
        result += str(memo[c])
        memo[c] += 1

    return result
```

```python
def numericals(s):
    dictio = {}
    t = ""
    for i in s:
        dictio[i] = dictio.get(i,0) + 1 
        t += str(dictio[i])
    return t
```

```python
from collections import defaultdict

def numericals(s):
    d, lst = defaultdict(int), []
    for c in s:
        d[c] += 1
        lst.append(d[c])
    return ''.join(map(str, lst))
```