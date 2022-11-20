def solution():
    case_count = int(input())
    result = []
    for _ in range(case_count):
        university_case_count = int(input())
        temp = [input().split() for _ in range(university_case_count)]
        result.append(sorted(temp, key=lambda x: int(x[1]), reverse=True)[0][0])
    return "\n".join(result)


if __name__ == "__main__":
    print(solution())
