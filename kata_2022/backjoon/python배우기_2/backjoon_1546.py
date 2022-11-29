def solution():
    lecture_count = int(input())
    scores = list(map(int, input().split()))
    max_scores = max(scores)
    modified_scores = map(lambda score: score / max_scores * 100, scores)
    return sum(modified_scores) / lecture_count


if __name__ == "__main__":
    print(solution())
