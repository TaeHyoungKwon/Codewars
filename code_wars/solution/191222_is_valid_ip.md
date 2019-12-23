```python
def is_valid_IP(strng):
    arr = strng.split('.')
    if len(arr) != 4:
        return False
    for s in arr:
        if len(s) > 1 and s[0] == '0':
            return False
        try:
            to_int = int(s)
            if str(to_int) != s:
                return False
            if not 0 <= to_int <= 255:
                return False
        except:
            return False
    return True
```

```python
import re
def is_valid_IP(strng):
    try:
        m = re.match(r'([12]?\d{1,2})\.([12]?\d{1,2})\.([12]?\d{1,2})\.([12]?\d{1,2})\Z', strng)
        return bool(m) and len(m.groups()) == 4 and all(0<=int(d)<=255 for d in m.groups())
    except ValueError:
        return False
    
```

```python
import ipaddress

def is_valid_IP(s):
    try:
        ipaddress.ip_address(s)
    except ValueError:
        return False
    return True
```