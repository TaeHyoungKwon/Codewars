def solution():
    num_list = [10, 23, 5, 17, 35, 9, 12, 19]
    min = num_list[0]
    for num in num_list[1:]:
        if num < min:
            min = num
    return min

print(solution())