BIRTH_DAY = 20000303


def solution():
    favorit_number = int(input())
    return favorit_number % BIRTH_DAY


if __name__ == "__main__":
    print(solution())
