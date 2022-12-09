def solution():
    case_count = int(input())
    result = []
    for _ in range(case_count):
        lt, wt, le, we = map(int, input().split())
        if lt * wt > le * we:
            result.append("TelecomParisTech")
        elif le * we > lt * wt:
            result.append("Eurecom")
        else:
            result.append("Tie")
    return "\n".join(result)


if __name__ == "__main__":
    print(solution())
