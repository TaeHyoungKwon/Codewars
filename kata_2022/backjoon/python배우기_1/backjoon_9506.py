def divisors(number: int) -> list[int]:
    return [candidate_number for candidate_number in range(1, number + 1) if number % candidate_number == 0]


def solution():
    result = []
    while (target_number := int(input())) != -1:
        divisors_except_target_number = divisors(number=target_number)[:-1]
        is_perfect_number = (
            sum(divisor for divisor in divisors_except_target_number) == target_number
        )

        if is_perfect_number:
            result.append(f"{target_number} = {' + '.join(str(divisor) for divisor in divisors_except_target_number)}")
        else:
            result.append(f"{target_number} is NOT perfect.")

    return "\n".join(result)


if __name__ == "__main__":
    print(solution())
