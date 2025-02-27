_ = int(input())
m = map(int, input().split())

result = []

for ele in m:
    if ele == 300:
        result.append(1)
    elif ele >= 275:
        result.append(2)
    elif ele >= 250:
        result.append(3)
    else:
        result.append(4)

print(" ".join(map(str, result)))
