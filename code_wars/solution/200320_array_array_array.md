```python
def explode(arr):  
    return [arr] * sum(v for v in arr if isinstance(v,int)) or 'Void!'
```

```python
def explode(arr):  
    numbers = [n for n in arr if type(n) == int]
    return [arr] * sum(numbers) if numbers else "Void!"
```

```python

```