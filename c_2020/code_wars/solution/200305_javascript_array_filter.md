```python
def get_even_numbers(arr):
    return list(filter(lambda x: x % 2 == 0, arr))
```

```python
is_even = lambda x: x % 2 == 0

def get_even_numbers(arr):
    return list(filter(is_even, arr))
```

```python
def get_even_numbers(arr):
    return [v for v in arr if not v&1]
```