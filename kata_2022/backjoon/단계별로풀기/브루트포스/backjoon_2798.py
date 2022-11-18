from itertools import combinations


def solution():
    _, dealer_card_number = map(int, input().split())
    my_card_numbers = [int(number) for number in input().split()]

    approximate_value = 0
    for case in combinations(my_card_numbers, 3):
        sum_of_card_numbers = sum(case)
        if sum_of_card_numbers > dealer_card_number:
            continue

        if sum_of_card_numbers > approximate_value:
            approximate_value = sum_of_card_numbers

    return approximate_value


if __name__ == "__main__":
    print(solution())
