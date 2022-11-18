from collections import Counter


class DiceRewardCalculator:
    def __init__(self, dice_numbers: list[int]):
        self._dice_numbers = dice_numbers

    def calculate(self):
        count_map = Counter(self._dice_numbers)
        if len(count_map) == 1:
            return 10000 + self._dice_numbers[0] * 1000
        elif len(count_map) == 2:
            target = count_map.most_common(1)[0][0]
            return 1000 + target * 100
        else:
            return max(self._dice_numbers) * 100


def solution():
    case_count = int(input())
    return max(
        [
            DiceRewardCalculator(
                dice_numbers=[int(dice_number) for dice_number in input().split()]
            ).calculate()
            for _ in range(case_count)
        ]
    )


if __name__ == "__main__":
    print(solution())
