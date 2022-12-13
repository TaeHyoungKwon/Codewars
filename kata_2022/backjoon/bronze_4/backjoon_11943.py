def solution():
    apple_1, orange_1 = map(int, input().split())
    apple_2, orange_2 = map(int, input().split())
    return min(apple_1 + orange_2, orange_1 + apple_2)


if __name__ == "__main__":
    print(solution())
