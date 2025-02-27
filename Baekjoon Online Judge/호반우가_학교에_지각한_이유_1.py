str_, dex, int_, luk, n = map(int, input().split())

sum_of_all_stats = str_ + dex + int_ + luk
result = 4 * n - sum_of_all_stats

if result <= 0:
    print("0")
else:
    print(result)
