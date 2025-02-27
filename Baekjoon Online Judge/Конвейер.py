_ = int(input())
moving_histories = map(int, input().split())

total = sum(moving_histories)

if total == 0:
    print("Stay")
    exit()

if total > 0:
    print("Right")
else:
    print("Left")
