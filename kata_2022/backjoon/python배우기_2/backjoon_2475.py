def solution():
    numbers = map(lambda x: int(x) ** 2, input().split())
    return sum(numbers) % 10


if __name__ == "__main__":
    print(solution())
