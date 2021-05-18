import unittest


def to_time(seconds):
    quotient, rest = divmod(seconds, 3600)
    return f"{quotient} hour(s) and {rest // 60} minute(s)"


class TestToTime(unittest.TestCase):
    def test_to_time_with_no_remaining_seconds(self):
        self.assertEqual(to_time(seconds=323500), "89 hour(s) and 51 minute(s)")

    def test_to_time_with_remaining_seconds(self):
        self.assertEqual(to_time(seconds=3601), "1 hour(s) and 0 minute(s)")


"""
문제
- seconds를 받았을 때, 알맞은 포맷(시간 + 분)으로 변환하여 리턴하여라
해결
- 주어진 seconds를 받아서, hour, min 을 구한 뒤에 포맷에 맞게 변경해준다
조건
- 남은 초는 무시한다
- "X hour(s) and X minute(s)" 의 형태를 유지한다
- input -> seconds: int / output -> str
절차
1. seconds를 3600으로 나눠서 몫을 구한다 - hour
2. 1번에서 나온 나머지를 60으로 나눠서 몫을 구한다 - minute
3. 각각을 포맷에 맞게 리턴한다

테스트
1. 초가 없는 형태
2. 초가 있는 형태
"""