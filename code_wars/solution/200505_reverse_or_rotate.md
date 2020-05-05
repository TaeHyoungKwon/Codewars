```python
def revrot(strng, sz):
    return ''.join(
        chunk[1:] + chunk[:1] if sum(int(d)**3 for d in chunk) % 2 else chunk[::-1]
        for chunk in map(''.join, zip(*[iter(strng)]*sz))
    )

```