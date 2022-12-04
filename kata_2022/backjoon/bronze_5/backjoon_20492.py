TAXES_AND_THE_PUBLIC_UTILITIES_CHARGE = 0.22


def solution():
    n = int(input())

    case_1 = n - int(n * TAXES_AND_THE_PUBLIC_UTILITIES_CHARGE)
    case_2 = n - int(n * 0.2 * TAXES_AND_THE_PUBLIC_UTILITIES_CHARGE)

    return f"{case_1} {case_2}"


if __name__ == "__main__":
    print(solution())
