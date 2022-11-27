def solution():
    problem_count = int(input())
    score_card = [int(score) for score in input().split()]

    prev = score_card[0]
    result = score_card[0]
    temp = 0
    for score in score_card[1:]:
        if prev == 0:
            temp = 0
        else:
            temp += 1

        if score == 1:
            result += 1 + temp
            prev = 1
        else:
            prev = 0
            temp = 0
    return result


if __name__ == "__main__":
    print(solution())
