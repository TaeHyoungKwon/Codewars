MEMOIZATION = [0] * 100


def solution(num):
    if num == 0:
        return 0
    if num <= 2:
        return 1
    if MEMOIZATION[num] != 0:
        return MEMOIZATION[num]
    MEMOIZATION[num] = solution(num - 1) + solution(num - 2)
    return MEMOIZATION[num]


if __name__ == "__main__":
    num = int(input())
    print(solution(num))
