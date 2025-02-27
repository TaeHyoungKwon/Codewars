from math import floor

n, k = map(int, input().split())
ranks = list(map(int, input().split()))

result = []

for rank in ranks:
    percentage = floor(rank / n * 10**2) / 10**2

    if 0 <= percentage <= 0.04:
        result.append(1)
    elif 0.04 < percentage <= 0.11:
        result.append(2)
    elif 0.11 < percentage <= 0.23:
        result.append(3)
    elif 0.23 < percentage <= 0.40:
        result.append(4)
    elif 0.40 < percentage <= 0.60:
        result.append(5)
    elif 0.60 < percentage <= 0.77:
        result.append(6)
    elif 0.77 < percentage <= 0.89:
        result.append(7)
    elif 0.89 < percentage <= 0.96:
        result.append(8)
    else:
        result.append(9)

print(*result)
