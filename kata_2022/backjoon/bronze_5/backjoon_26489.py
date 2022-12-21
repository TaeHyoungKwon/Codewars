def solution():
    cnt = 0
    try:
        while (words := input().split()) != []:
            cnt += 1
    except EOFError:
        return cnt


if __name__ == "__main__":
    print(solution())
