def solution(winner_results: list[str]) -> str:
    dalgu_win_count = 0
    ponix_win_count = 0

    for winner in winner_results:
        if winner == "D":
            dalgu_win_count += 1
        else:
            ponix_win_count += 1

        if abs(dalgu_win_count - ponix_win_count) == 2:
            break

    return f"{dalgu_win_count}:{ponix_win_count}"


if __name__ == "__main__":
    winner_results = [input() for _ in range(int(input()))]
    print(solution(winner_results))
