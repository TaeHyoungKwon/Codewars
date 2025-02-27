loop = int(input())
count = 0
for _ in range(loop):
    s = input()
    if "01" in s or "OI" in s:
        count += 1

print(count)