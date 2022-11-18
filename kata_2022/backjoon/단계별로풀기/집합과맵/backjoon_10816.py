import sys
from collections import Counter


def solution():
    case_count = int(input())
    sanguen_cards = [int(item) for item in sys.stdin.readline().split()]
    target_case_count = int(input())
    target_cards = map(int, sys.stdin.readline().split())

    count_map = Counter(sanguen_cards)
    return " ".join(str(count_map.get(target_card, 0)) for target_card in target_cards)


if __name__ == "__main__":
    print(solution())