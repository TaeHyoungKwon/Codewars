from math import ceil


s = int(input())
a = int(input())
b = int(input())

if a >= s:
    print(250)
else:
    print(int(250 + (ceil((s - a) / b) * 100)))
