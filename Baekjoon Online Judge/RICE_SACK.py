count = int(input())

for i in range(1, count + 1):
    input_values = map(int, input().split())
    print(f"Case #{i}: {max(input_values)}")
