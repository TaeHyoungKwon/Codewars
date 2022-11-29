CASE_COUNT = 7


def solution():
    numbers = [int(input()) for _ in range(CASE_COUNT)]
    odd_numbers = [number for number in numbers if number % 2 == 1]
    return "\n".join(map(str, [sum(odd_numbers), min(odd_numbers)])) if odd_numbers else -1


if __name__ == "__main__":
    print(solution())
