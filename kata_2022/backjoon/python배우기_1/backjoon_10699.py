from datetime import datetime


def solution():
    return f"{datetime.now():%Y-%m-%d}"


if __name__ == "__main__":
    print(solution())
