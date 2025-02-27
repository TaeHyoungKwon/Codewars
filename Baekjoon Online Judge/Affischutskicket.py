c4_g, a3_g, a4_g = map(int, input().split())
c4 = c4_g * 0.229 * 0.324
a3 = a3_g * 0.297 * 0.42
a4 = a4_g * 0.21 * 0.297
print(f"{2*c4 + 2*a3 + a4:.6f}")