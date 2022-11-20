import operator

OPERATOR_MAP = {
    "+": operator.add,
    "*": operator.mul,
}


def solution():
    a = int(input())
    operator_ = input()
    b = int(input())
    return OPERATOR_MAP[operator_](a, b)


if __name__ == "__main__":
    print(solution())
