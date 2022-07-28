from itertools import groupby


def solution(arr: list[int]) -> int:
    count = 0
    while arr != [1]:
        grouped_by_consecutive_numbers = [list(group) for _, group in groupby(arr)]
        arr = list(map(len, grouped_by_consecutive_numbers))
        count += 1
    return count


def test_solution():
    assert solution([1, 1, 3, 3, 2, 2, 4, 5, 1, 1, 1, 3, 3, 3]) == 6
    assert solution([1, 2, 3]) == 3


"""
문제
* 자연수 list가 주어질 때, 연속해서 나오는 개수를 순서대로 나열하는 과정을 반복하려 함
* 이때, 최초로 [1] 이라는 수열이 나올때까지 과정을 몇번 수행했는지 return 하는 solution 함수를 만들어라

해결
* groupby를 활용해서, 연속해서 나오는 개수를 확인한다

조건
* arr의 길이는 1이상 1,000 이하이다.
* arr의 원소는 1이상, 1,000 이하 자연수 이다.

절차
1. arr 값을 받는다.
2. groupby를 활용해서 그룹핑 한다
3. groupby한 결과에 대해서, 각 요소의 개수 만큼으로 새롭게 리스트를 만든다
4. 2,3 번을 반복한다
5. [1]이 되는 시점에 루프가 몇번 돌았는지를 리턴한다

검증
1.
[1, 2, 3] -> 3
2.
[1, 1, 3, 3, 2, 2, 4, 5, 1, 1, 1, 3, 3, 3] -> 6
"""
