import sys


def solution():
    # 아직 못품
    number_count = int(sys.stdin.readline())
    numbers = sys.stdin.readline().split()
    sorted_numbers = sorted(numbers)
    return " ".join(str(sorted_numbers.index(number)) for number in numbers)


if __name__ == "__main__":
    print(solution())
