```python
def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    p1_won = (p1, p2) in [
        ('rock', 'scissors'),
        ('scissors', 'paper'),
        ('paper', 'rock')
    ]
    return "Player {} won!".format(1 if p1_won else 2)
```

```python
def rps(p1, p2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        return "Player 1 won!"
    if beats[p2] == p1:
        return "Player 2 won!"
    return "Draw!"
```

```python
def rps(p1, p2):
    hand = {'rock':0, 'paper':1, 'scissors':2}
    results = ['Draw!', 'Player 1 won!', 'Player 2 won!']
    return results[hand[p1] - hand[p2]]

```

```python
def rps(p1, p2):
    if p1 == p2:
        return 'Draw!'
    elif (p1 == 'rock' and p2 == 'scissors') or (p1 == 'scissors' and p2 == 'paper') or (p1 == 'paper' and p2 == 'rock'):
        return 'Player 1 won!'
    else:
        return 'Player 2 won!'
        
```

```python
def rps(p1, p2):
    d1 = [('paper','rock'), ('rock', 'scissors'), ('scissors', 'paper')]
    return 'Draw!' if p1 == p2 else "Player {} won!".format(1 if (p1, p2) in d1 else 2)
```