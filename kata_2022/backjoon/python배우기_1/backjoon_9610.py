from collections import defaultdict


def solution():
    case_count = int(input())

    result = dict.fromkeys(["Q1", "Q2", "Q3", "Q4", "AXIS"], 0)
    for _ in range(case_count):
        x, y = map(int, input().split())
        if x > 0 and y > 0:
            result["Q1"] += 1
        elif x < 0 and y > 0:
            result["Q2"] += 1
        elif x < 0 and y < 0:
            result["Q3"] += 1
        elif x > 0 and y < 0:
            result["Q4"] += 1
        else:
            result["AXIS"] += 1

    return "\n".join(f"{q}: {count}" for q, count in result.items())


if __name__ == "__main__":
    print(solution())
