```python
def triple_trouble(*args):
        return "".join("".join(a) for a in zip(*args))
```

```python
def triple_trouble(*args):
    return ''.join(sum(zip(*args), ()))
```

```python
def triple_trouble(one, two, three):
    return "".join(map("".join, zip(one, two, three)))
```