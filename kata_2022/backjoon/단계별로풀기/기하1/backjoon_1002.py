import math


def solution():
    case_count = int(input())
    test_cases = [map(int, input().split()) for _ in range(case_count)]

    result = []
    for test_case in test_cases:
        x1, y1, r1, x2, y2, r2 = test_case
        distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        if distance == 0 and r1 == r2:
            result.append(-1)
            continue

        if abs(r1 - r2) == distance or r1 + r2 == distance:
            result.append(1)
        elif abs(r1 - r2) < distance < (r1 + r2):
            result.append(2)
        else:
            result.append(0)
    return "\n".join(str(number) for number in result)


if __name__ == "__main__":
    print(solution())
