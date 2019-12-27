```python
def camel_case(s):
    #your code here
    return ''.join(s.title().split())
```

```python
def camel_case(s):
    return ''.join(x.capitalize() for x in s.split())
```

```python
def camel_case(string):
    result = ""
    if len(string) == 0:
        return result
    else:
        result = string.title().replace(" ","")
        return result
```

```python
def camel_case(string):
    return ''.join(s[0].upper() + s[1:] for s in string.split(' ') if s)
```