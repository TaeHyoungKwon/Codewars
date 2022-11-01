import sys


def solution():
    case_count = int(sys.stdin.readline())

    result = []
    for _ in range(case_count):
        floor, room_number, guest_number = map(int, sys.stdin.readline().split())
        quotient, remainder = divmod(guest_number, floor)
        if remainder:
            result.append(remainder * 100 + quotient + 1)
        else:
            result.append(floor * 100 + quotient)

    return "\n".join(str(number) for number in result)


if __name__ == "__main__":
    print(solution())