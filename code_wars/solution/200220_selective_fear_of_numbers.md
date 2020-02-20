```python
afraid = {
    'Monday': lambda x: x == 12,
    'Tuesday': lambda x: x > 95,
    'Wednesday': lambda x: x == 34,
    'Thursday': lambda x: x == 0,
    'Friday': lambda x: x % 2 == 0,
    'Saturday': lambda x: x == 56,
    'Sunday': lambda x: abs(x) == 666,
}

def am_I_afraid(day, num):
    return afraid[day](num)
```

```python
def am_I_afraid(day,num):
    return {
        'Monday':  num == 12,
        'Tuesday': num > 95,
        'Wednesday': num == 34,
        'Thursday': num == 0,
        'Friday': num % 2 == 0,
        'Saturday': num ==  56,
        'Sunday': num == 666 or num == -666,
    }[day]

```