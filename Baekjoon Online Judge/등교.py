n, x = map(int, input().split())

result = []

for _ in range(n):
    s, t = map(int, input().split())
    if s + t <= x:
        result.append(s)
try:
    print(max(result))
except ValueError:
    print(-1)
