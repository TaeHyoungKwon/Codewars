```python
def correct_tail(body, tail):
    return body.endswith(tail)
```

```python
def correct_tail(body, tail):
    return body[-1] == tail
```

```python
correct_tail = lambda a,t: a[-1]==t
```