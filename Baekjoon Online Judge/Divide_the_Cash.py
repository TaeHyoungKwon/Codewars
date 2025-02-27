n, d = map(int, input().split())
result = [int(input()) for _ in range(n)]

total = sum(result)

for ele in result:
    print(int(ele / total * d))
