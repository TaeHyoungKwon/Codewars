```python
import datetime
def check_coupon(entered_code, correct_code, current_date, expiration_date):
    if entered_code is correct_code:
        return(datetime.datetime.strptime(current_date,'%B %d, %Y') <= datetime.datetime.strptime(expiration_date,'%B %d, %Y'))
    return False
```

```python
import datetime

def check_coupon(entered_code, correct_code, current_date, expiration_date):
    strptime = datetime.datetime.strptime
    format = "%B %d, %Y"
    return strptime(current_date, format) <= strptime(expiration_date, format) and\
                             entered_code is correct_code
```

```python
from time import strptime

def check_coupon(entered_code, correct_code, current_date, expiration_date):
    if not entered_code is correct_code:
        return False
    return strptime(current_date,"%B %d, %Y") <= strptime(expiration_date,"%B %d, %Y")
```