STUDENTS_COUNT = 28


def solution():
    r = int(input())
    s = int(input())
    return r * 8 + s * 3 - STUDENTS_COUNT


if __name__ == "__main__":
    print(solution())
