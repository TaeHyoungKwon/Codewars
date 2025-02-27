w, h = map(int, input().split())

diagonal = (w ** 2 + h ** 2) ** (1/2)

print(f"{w + h - diagonal:.9f}")
