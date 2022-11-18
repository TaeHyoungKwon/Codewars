def _input():
    return [int(input()) for _ in range(10)]


def solution():
    numbers = _input()
    return len(set(number % 42 for number in numbers))


if __name__ == "__main__":
    print(solution())
