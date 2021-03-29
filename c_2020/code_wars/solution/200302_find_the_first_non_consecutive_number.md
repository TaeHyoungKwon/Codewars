```python
def first_non_consecutive(arr):
    return next((b for a, b in zip(arr, arr[1:]) if b-a != 1), None)
```