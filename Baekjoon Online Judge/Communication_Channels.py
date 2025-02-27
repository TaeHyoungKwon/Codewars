t = int(input())

for _ in range(t):
    n, m = map(str, input().split())
    if n == m:
        print("OK")
    else:
        print("ERROR")
