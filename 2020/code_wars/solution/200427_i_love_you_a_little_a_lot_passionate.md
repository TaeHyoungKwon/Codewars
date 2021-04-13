```python
def how_much_i_love_you(nb_petals):
    return ["I love you", "a little", "a lot", "passionately", "madly", "not at all"][nb_petals % 6 - 1] #g
```

```python
def how_much_i_love_you(nb_petals):
    # your code
    words = {1: 'I love you', 2: 'a little', 3: 'a lot', 4: 'passionately',
            5: 'madly', 0: 'not at all'}
    return words[nb_petals%6]
```