```python
def fillable(stock, merch, n):
    return stock.get(merch, 0) >= n
```

```python

def fillable(stock, merch, n):
    return merch in stock and stock[merch] >= n
```