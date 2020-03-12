```python
def remove_url_anchor(url):
  return url.partition('#')[0]
```

```python
def remove_url_anchor(url):
  return url.split('#')[0]
```

```python
def remove_url_anchor(url):
  import re
  return re.sub('#.*$','',url)
```