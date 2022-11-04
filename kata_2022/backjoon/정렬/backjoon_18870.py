import sys


def solution():
    number_count = int(sys.stdin.readline())
    numbers = list(map(int, sys.stdin.readline().split()))
    sorted_numbers = sorted(list(set(numbers)))
    mapping = {
        sorted_number: index
        for index, sorted_number in enumerate(sorted_numbers)
    }
    return " ".join(str(mapping[number]) for number in numbers)


if __name__ == "__main__":
    print(solution())
