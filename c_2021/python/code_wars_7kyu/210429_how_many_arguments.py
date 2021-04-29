import unittest


def args_count(*args, **kwargs):
    return len(args) + len(kwargs)


class TestArgsCount(unittest.TestCase):
    def test_args_count(self):
        self.assertEqual(args_count(100), 1)

    def test_args_count_with_empty_args(self):
        self.assertEqual(args_count(), 0)

    def test_args_count_with_positional_arg(self):
        self.assertEqual(args_count(32, a1=12), 2)


"""
문제
 - argument의 개수를 리턴하는 함수를 만들어라.
해결
 - args 로 받아서, 리스트 내 element 개수를 반환한다.
절차
1. 함수를 만든다.
2. *args로 받아서, return은 args의 길이만큼 넘긴다
3. positional args 는 **kwargs 로 받아서, 길이만큼 더해준다.
"""