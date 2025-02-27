STRATEGY_PASS_SCORE = 35
MANAGEMENT_PASS_SCORE = 25
TECHNOLOGY_PASS_SCORE = 40


n = int(input())

for _ in range(n):
    identity_number, strategy_score, management_score, technology_score = map(
        int, input().split()
    )
    total_score = strategy_score + management_score + technology_score

    pass_condition = (
        total_score >= 55
        and strategy_score / STRATEGY_PASS_SCORE >= 0.3
        and management_score / MANAGEMENT_PASS_SCORE >= 0.3
        and technology_score / TECHNOLOGY_PASS_SCORE >= 0.3
    )
    result = "PASS" if pass_condition else "FAIL"

    print(f"{identity_number} {total_score} {result}")
