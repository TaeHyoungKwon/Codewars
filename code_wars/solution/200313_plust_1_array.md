```python
def up_array(arr):
    if arr and all(0 <= x <= 9 for x in arr):
        return map(int, str(int(''.join(map(str, arr))) + 1))
```

