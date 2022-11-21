def solution():
    case_count = int(input())
    birthday_info = [input().split() for _ in range(case_count)]
    result = sorted(birthday_info, key=lambda x: (-int(x[3]), -int(x[2]), -int(x[1])))
    return "\n".join([result[0][0], result[-1][0]])


if __name__ == "__main__":
    print(solution())
