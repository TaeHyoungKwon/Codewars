```python
def remove_duplicate_words(s):
    return ' '.join(dict.fromkeys(s.split())
```

```python
def remove_duplicate_words(s):
    s = s.split(" ")
    words = []
    for item in s:
        if item not in words:
            words.append(item)
    return " ".join(words)
```

```python
def remove_duplicate_words(s):
    def f():
        seen = set()
        for word in s.split():
            if word in seen:
                continue
            seen.add(word)
            yield word
    return ' '.join(f())
```


```python
def remove_duplicate_words(s):
    new_list = []
    for word in s.split():
        if word not in new_list:
            new_list.append(word)
    return " ".join(new_list)
```


```python
d = {}
remove_duplicate_words = lambda s: " ".join(d.setdefault(w, w) for w in s.split() if w not in d)
```