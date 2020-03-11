```python
def format_words(words):
    words = list(filter(None, words or []))
    words[-2:] = [' and '.join(words[-2:])]
    return ', '.join(words)
```

```python
def format_words(words):
    return ', '.join(word for word in words if word)[::-1].replace(',', 'dna ', 1)[::-1] if words else ''
```

```python
def format_words(words):
    words = [w for w in words if w] if words else ''
    if not words:
        return ''
    return '{seq} and {last}'.format(seq=', '.join(words[:-1]), last=words[-1]) if len(words) !=1 else '{0}'.format(words[0])
```

```python
def format_words(words):
    words = [w for w in words if w] if words else ''
    if not words:
        return ''
    return f'{", ".join(words[:-1])} and {words[-1]}' if len(words) !=1 else words[-1]
```