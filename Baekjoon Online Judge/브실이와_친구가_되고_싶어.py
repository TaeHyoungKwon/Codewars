a, b = map(int, input().split())
k, x = map(int, input().split())

friend_range = {i for i in range(a, b + 1)}
bsil_enable_friend_range = {i for i in range(k - x, k + x + 1)}

intersection = friend_range & bsil_enable_friend_range

if intersection:
    print(len(intersection))
else:
    print("IMPOSSIBLE")
