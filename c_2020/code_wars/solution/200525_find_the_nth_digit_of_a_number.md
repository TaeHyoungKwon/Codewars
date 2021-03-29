```python
def find_digit(num, nth):
    if nth <= 0:
        return -1
    m = 10 ** (nth - 1)
    return abs(num) // m % 10
```