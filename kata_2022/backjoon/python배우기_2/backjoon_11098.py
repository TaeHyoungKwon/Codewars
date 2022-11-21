def solution():
    case_count = int(input())
    result = []
    for _ in range(case_count):
        player_count = int(input())
        temp = []
        for _ in range(player_count):
            temp.append(input().split())
        result.append(max(temp, key=lambda x: int(x[0])))
    return "\n".join(element[1] for element in result)


if __name__ == "__main__":
    print(solution())
