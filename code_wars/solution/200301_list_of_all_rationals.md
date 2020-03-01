```python
def all_rationals():
    yield (1, 1)
    for a, b in all_rationals():
        yield from [(a, a + b), (a + b, b)]
```


```python
def all_rationals():
    prev_level = [(1, 1)]
    cur_level = []

    yield prev_level[0]
    while True:
        for val in prev_level:
            cur_level.append((val[0], val[0] + val[1]))
            yield cur_level[-1]
            cur_level.append((val[0] + val[1], val[1]))
            yield cur_level[-1]

        prev_level = [x for x in cur_level]
        cur_level = []
```


```python
def all_rationals():
    queue = [(1, 1)]
    while queue:
        current = queue.pop(0)
        a, b = current
        queue.extend([(a, a + b), (a + b, b)])
        yield current
```

```def f():
    yield(1,1)
    for a,b in f():
        yield(a,a+b)
        yield(a+b,b)
all_rationals=f
```