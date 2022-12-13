TARGET_MONTH = 2
TARGET_DAY = 18


def solution():
    month = int(input())
    day = int(input())

    if month > TARGET_MONTH:
        return "After"

    if month < TARGET_MONTH:
        return "Before"

    if month == TARGET_MONTH:
        if day > TARGET_DAY:
            return "After"
        elif day < TARGET_DAY:
            return "Before"
        else:
            return "Special"


if __name__ == "__main__":
    print(solution())
