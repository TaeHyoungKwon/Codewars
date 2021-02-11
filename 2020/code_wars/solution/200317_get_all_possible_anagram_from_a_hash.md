```python
from itertools import chain, permutations

def get_words(hash_of_letters):
    return sorted(set(''.join(v) for v in permutations(chain.from_iterable(v * k for (k, v) in hash_of_letters.iteritems()))))
```

```python
from itertools import permutations

def get_words(letters):
    word = "".join(qty * char for qty in letters for chars in letters[qty] for char in chars)
    return sorted({"".join(permutation) for permutation in permutations(word)})
```