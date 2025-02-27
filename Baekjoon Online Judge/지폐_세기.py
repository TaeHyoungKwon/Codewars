loop = int(input())

result = []

for _ in range(loop):
    width, _ = map(int, input().split())

    if width == 136:
        price = 1000
    elif width == 142:
        price = 5000
    elif width == 148:
        price = 10000
    else:
        price = 50000

    result.append(price)

print(sum(result))
