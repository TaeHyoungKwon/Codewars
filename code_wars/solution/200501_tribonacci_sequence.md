```python
def tribonacci(signature, n):
    output = signature[:n]
    while len(output) < n:
        output.append(sum(output[-3:]))
    return output
```

```python
import itertools

def f(signature):
    a, b, c = signature
    while True:
        yield a
        a, b, c = b, c, a + b + c
            
def tribonacci(signature, n):
    return list(itertools.islice(f(signature), 0, n))
```

```python
def tribonacci(signature, n):
  res = signature[:n]
  for i in range(n - 3):
      res.append(sum(res[-3:]))
  return res
```