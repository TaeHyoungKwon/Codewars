```python
import re

def validPhoneNumber(phone_number):
    return bool(re.match(r'\(\d{3}\) \d{3}-\d{4}$', phone_number))
```