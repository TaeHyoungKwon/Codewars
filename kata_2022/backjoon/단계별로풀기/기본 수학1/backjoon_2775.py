import sys


def solution():
    case_count = int(sys.stdin.readline())

    result = []
    for _ in range(case_count):
        floor = int(input())
        num = int(input())

        zero_floor = [i for i in range(1, num + 1)]

        for _ in range(floor):
            for j in range(1, num):
                zero_floor[j] += zero_floor[j - 1]

        result.append(zero_floor[-1])
    return "\n".join(str(ele) for ele in result)


if __name__ == "__main__":
    print(solution())
