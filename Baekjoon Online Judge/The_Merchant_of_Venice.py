k = int(input())


for i in range(1, k + 1):
    result = 0
    n, s, d = map(int, input().split())
    for _ in range(n):
        di, vi = map(int, input().split())
        if di <= s * d:
            result += vi
    print(f"Data Set {i}:\n{result}\n")
