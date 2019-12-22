```python
def cakes(recipe, available):
    return min(
        available.get(ing, 0) // recipe[ing]
        for ing in recipe
    )
```

```python
def cakes(recipe, available):
  return min(available.get(k, 0)/recipe[k] for k in recipe)
```

```python
def cakes(recipe, available):
    return min(available.get(k, 0) // v for k,v in recipe.iteritems())
```