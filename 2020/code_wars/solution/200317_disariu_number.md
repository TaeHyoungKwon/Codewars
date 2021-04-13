```python
def disarium_number(number):
    disarium = number == sum(int(n) ** i for i, n in enumerate(str(number), 1))
    return 'Disarium !!' if disarium else 'Not !!'
```