def solution(
    origin_meat_temperature: int,
    target_temperature: int,
    time_to_burn_for_1_degree_from_frozen_meat: int,
    time_to_defrost_from_frozen_meat: int,
    time_to_burn_from_nonfrozen_meat: int,
) -> int:
    if origin_meat_temperature > 0:
        return (
            target_temperature - origin_meat_temperature
        ) * time_to_burn_from_nonfrozen_meat
    else:
        return (
            (0 - origin_meat_temperature) * time_to_burn_for_1_degree_from_frozen_meat
            + time_to_defrost_from_frozen_meat
            + (target_temperature * time_to_burn_from_nonfrozen_meat)
        )


if __name__ == "__main__":
    case_count = 5
    input_ = [int(input()) for _ in range(case_count)]
    print(solution(*input_))
