```python
def divisors(n):
    sq = n ** 0.5
    return 2 * sum(n % i == 0 for i in range(1, int(sq) + 1)) - sq.is_integer()
```

```python
def divisors(n):
    return sum(2 if x*x!=n else 1 for x in range(1, int(n**0.5)+1) if n%x==0)
```