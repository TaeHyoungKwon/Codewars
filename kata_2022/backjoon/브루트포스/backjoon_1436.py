import sys

END_NUMBER_666 = "666"


def solution():
    number = int(sys.stdin.readline())
    last_end_number = 666

    while number:
        if END_NUMBER_666 in str(last_end_number):
            number -= 1
        last_end_number += 1
    return last_end_number - 1


if __name__ == "__main__":
    print(solution())
