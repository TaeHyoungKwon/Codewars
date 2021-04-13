```python
parens = dict([')(', '][', '}{'])

def group_check(s):
    stack = []
    for c in s:
        if c in parens:
            if not (stack and parens[c] == stack.pop()):
                return False
        else:
            stack.append(c)
    return not stack
```

```python
BRACES = { '(': ')', '[': ']', '{': '}' }

def group_check(s):
    stack = []
    for b in s:
        c = BRACES.get(b)
        if c:
            stack.append(c)
        elif not stack or stack.pop() != b:
            return False
    return not stack
```