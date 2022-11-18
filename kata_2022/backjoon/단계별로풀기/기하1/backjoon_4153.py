def solution():
    while True:
        max_value, mid_value, min_value = sorted([int(number) for number in input().split()], reverse=True)
        if max_value == 0:
            break

        if mid_value ** 2 + min_value ** 2 == max_value ** 2:
            print("right")
        else:
            print("wrong")


if __name__ == "__main__":
    solution()
