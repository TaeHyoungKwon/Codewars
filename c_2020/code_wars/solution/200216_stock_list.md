```python
from collections import Counter

def stock_list(arts, cats):
    cnt = Counter()
    for art in (cats and arts):
        x, c = art.split()
        cnt[x[0]] += int(c)
    return ' - '.join('({} : {})'.format(c, cnt[c]) for c in (arts and cats))
```

```python
def stock_list(stocklist, categories):
    if not stocklist or not categories:
        return ""
    return " - ".join(
        "({} : {})".format(
            category,
            sum(int(item.split()[1]) for item in stocklist if item[0] == category))
        for category in categories)
```