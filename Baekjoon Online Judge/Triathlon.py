n = int(input())

max_value = 0

for _ in range(n):
    scores = list(map(int, input().split()))
    a, d, g = scores

    target_value = a * (d + g)
    if a == (d + g):
        target_value *= 2

    max_value = max(max_value, target_value)

print(max_value)
