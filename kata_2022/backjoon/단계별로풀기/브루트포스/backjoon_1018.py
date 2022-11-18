def solution():
    row, column = map(int, input().split())
    board = [input() for _ in range(row)]

    result = []
    for i in range(row - 7):
        for j in range(column - 7):
            case_1 = 0
            case_2 = 0

            for k in range(i, i + 8):
                for l in range(j, j + 8):
                    if (k + l) % 2 == 0:
                        if board[k][l] == "W":
                            case_1 += 1
                        else:
                            case_2 += 1
                    else:
                        if board[k][l] == "B":
                            case_1 += 1
                        else:
                            case_2 += 1
            result.append(case_1)
            result.append(case_2)
    return min(result)


if __name__ == "__main__":
    print(solution())
