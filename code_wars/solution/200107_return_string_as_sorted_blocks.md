```python
from collections import Counter

def blocks(s):
    sort = lambda c: (c.isdigit(), c.isupper(), c)
    answer, counter = [], Counter(s)
    while counter:
        block = ''.join(sorted(counter, key=sort))
        answer.append(block)
        counter = counter - Counter(block)
    return '-'.join(answer)
```

```python
from string import ascii_letters, digits
from collections import Counter

ALPHABET = ascii_letters + digits
C_ALPHABET = Counter(ALPHABET)

def blocks(s):
    d = Counter(ALPHABET + s) - C_ALPHABET
    return "-".join("".join(x for x in d if d[x] > i) for i in range(max(d.values(), default=0)))
```

```python
from collections import Counter as C
from string import ascii_lowercase as l,digits as d
def blocks(s):
    if not s:return ''
    char = sorted(C(s).items(), key=lambda x: (l+l.upper()+d).index(x[0]))
    li = ['']*max(char, key=lambda x: x[1])[1]
    for i, j in char : 
        for pos in range(j) : li[pos]+=i
    return '-'.join(li)
```