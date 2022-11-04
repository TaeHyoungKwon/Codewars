import sys


def solution():
    case_count = int(sys.stdin.readline())
    check_list = [0] * 10001

    for i in range(case_count):
        input_number = int(sys.stdin.readline())
        check_list[input_number] += 1

    for i in range(10001):
        if check_list[i] != 0:
            for j in range(check_list[i]):
                print(i)


if __name__ == "__main__":
    solution()
