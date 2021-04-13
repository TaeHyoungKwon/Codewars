```python
def make_2d_list(head, row, col):
    return [[head + (i * col) + j for j in range(col)] for i in range(row)]
```