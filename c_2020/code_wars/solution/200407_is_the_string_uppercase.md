```python
def is_uppercase(inp):
    return inp.isupper()
```

```python
def is_uppercase(inp):
    return all(c.isupper() for c in inp if c.isalpha())
```