loop = int(input())

for i in range(1, loop + 1):
    rank = int(input())

    if rank > 4500:
        print(f"Case #{i}: Round 1")
    elif rank > 1000:
        print(f"Case #{i}: Round 2")
    elif rank > 25:
        print(f"Case #{i}: Round 3")
    else:
        print(f"Case #{i}: World Finals")
