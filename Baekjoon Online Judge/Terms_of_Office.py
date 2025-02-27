def lcm(a, b, c, d):
    return a * b * c * d // gcd(a, b, c, d)


def gcd(a, b, c, d):
    return gcd(b, a % b, c, d) if b else a


x = int(input())
y = int(input())

count = 0
for _ in range(x, y + 1):
    if count % 60 == 0:
        print(f"All positions change in year {x + count}")
    count += 1
