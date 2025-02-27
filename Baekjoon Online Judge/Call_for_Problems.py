from collections import Counter

count = int(input())
counter = Counter(num % 2 == 1 for num in [int(input()) for _ in range(count)])
print(counter[True])
