```python
def add_letters(*letters):
    return chr((sum(ord(c) - ord('a') + 1 for c in letters) - 1) % 26 + ord('a')) if len(letters) > 0 else 'z'
```

```python
def add_letters(*letters):
    LETTERS = 'zabcdefghijklmnopqrstuvwxy'
    INDEX_TO_LETTERS = {i:v for i, v in enumerate(LETTERS, start=0)}
    LETTERS_TO_INDEX = {v:i for i, v in enumerate(LETTERS, start=0)}
    
    
    return INDEX_TO_LETTERS[sum(LETTERS_TO_INDEX[l] for l in letters) % len(LETTERS)]
```