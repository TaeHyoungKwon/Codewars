from datetime import datetime


def solution():
    now = datetime.utcnow()
    return f"{now.year}\n{now.month:02}\n{now.day:02}"


if __name__ == "__main__":
    print(solution())
