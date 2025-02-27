from collections import Counter


_ = int(input())
k = int(input())

result = Counter(num % 2 == 1 for num in map(int, str(k)))

odd_count = result[True]
even_count = result[False]

if even_count > odd_count:
    print(0)
elif even_count < odd_count:
    print(1)
else:
    print(-1)
