```python
In [1]: lights = ['green', 'yellow', 'red']

In [2]: transition = dict(zip(lights, lights[1:] + lights[:1]))

In [3]: transition
Out[3]: {'green': 'yellow', 'red': 'green', 'yellow': 'red'}

```