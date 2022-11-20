def solution():
    case_count = int(input())
    total_changyeong_score = 100
    total_sangduck_score = 100

    for _ in range(case_count):
        changyeong_score, sangduck_score = map(int, input().split())

        if changyeong_score == sangduck_score:
            continue

        if changyeong_score > sangduck_score:
            total_sangduck_score -= changyeong_score
        else:
            total_changyeong_score -= sangduck_score

    return "\n".join(str(element) for element in [total_changyeong_score, total_sangduck_score])


if __name__ == "__main__":
    print(solution())
