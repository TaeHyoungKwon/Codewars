def solution(p1: int, s1: int, s2: int, p2: int) -> str:
    if p1 + p2 > s1 + s2:
        return "Persepolis"
    elif p1 + p2 < s1 + s2:
        return "Esteghlal"
    else:
        if p2 > s1:
            return "Persepolis"
        elif p2 < s1:
            return "Esteghlal"
        else:
            return "Penalty"


if __name__ == "__main__":
    persepolis_home_score = list(map(int, input().split()))
    esteghlal_home_score = list(map(int, input().split()))
    print(solution(*persepolis_home_score, *esteghlal_home_score))
