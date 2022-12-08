def validate_password(target_password: str) -> bool:
    return 6 <= len(target_password) <= 9


def solution():
    case_count = int(input())
    passwords = [input() for _ in range(case_count)]
    return "\n".join(
        "yes" if validate_password(target_password=password) else "no"
        for password in passwords
    )


if __name__ == "__main__":
    print(solution())
