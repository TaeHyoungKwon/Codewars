from collections import Counter


def solution():
    judges_count = int(input())
    judge_record = input()

    if judge_record.count("A") > judge_record.count("B"):
        return "A"
    elif judge_record.count("A") < judge_record.count("B"):
        return "B"
    else:
        return "Tie"


if __name__ == "__main__":
    print(solution())
