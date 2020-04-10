```python
def is_divide_by(number, a, b):
  return number % a == number % b == 0
```

```python
def is_divide_by(number, a, b):
    return 0 == number % a and 0 == number % b
```

```python
def is_divide_by(number, a, b):
  return not (number%a or number%b)
```

```python
def is_divide_by(number, *divisors):
    return all(number % divisor == 0 for divisor in divisors)
```

```python
def is_divide_by(num, *n):
    return not any([num%x for x in n])
```