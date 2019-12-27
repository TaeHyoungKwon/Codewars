```python
def palin(length, pos):
    left = str(10**((length-1) // 2) + (pos - 1))
    right = left[::-1][length%2:]
    return int(left + right)
```

```python
def palin(a,b):
    s = str(10**((a-1)//2) + b-1)
    return int(s+s[::-1][a%2:])
```

```python
def palin(a, b):
    half = str(10**((a + 1) // 2 - 1) + b - 1)
    return int(half + (half[::-1] if a % 2 == 0 else half[:-1][::-1]))
```

```python
def palin(a, b):
    n = (a - 1) // 2
    x, y = divmod(b - 1, 10 ** n)
    result = str(x + 1) + (a > 2) * f'{y:0{n}}'
    return int(result + result[-1 + (a%-2)::-1])
```