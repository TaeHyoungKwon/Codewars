def solution():
    w_university = [int(input()) for _ in range(10)]
    k_university = [int(input()) for _ in range(10)]

    w_university_score = _calculate_score_for_top3(w_university)
    k_university_score = _calculate_score_for_top3(k_university)

    return f"{w_university_score} {k_university_score}"


def _calculate_score_for_top3(university_scores: list[int]):
    return sum(sorted(university_scores, reverse=True)[:3])


if __name__ == "__main__":
    print(solution())
