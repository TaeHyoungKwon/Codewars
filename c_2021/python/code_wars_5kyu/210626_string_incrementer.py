import re
import unittest


def increment_string(s):
    all_numbers = re.findall(r"\d+", s)
    if not all_numbers:
        return f"{s}1"
    last_num_part = all_numbers[-1]
    new = int(last_num_part) + 1
    return s.replace(last_num_part, str(new).rjust(len(last_num_part), "0"))


class TestIncrementString(unittest.TestCase):
    def test_increment_string_on_not_end_with_a_number(self):
        self.assertEqual(increment_string(s="foo"), "foo1")

    def test_increment_string_on_end_with_a_number(self):
        self.assertEqual(increment_string(s="foobar001"), "foobar002")

    def test_increment_string_on_empty_space(self):
        self.assertEqual(increment_string(s=""), "1")

    def test_increment_string_on_edge_case(self):
        self.assertEqual(
            increment_string(
                s="9269021;#w}^1K<yh5418050%d84`ZcU=~e)0177428864QX?B\\50,"
                "7256883~HnY2315285(v{kC<e#509112000000872532389"
            ),
            "9269021;#w}^1K<yh5418050%d84`ZcU=~e)0177428864QX?B\\50,7256883~HnY2315285(v{" "kC<e#509112000000872532390",
        )


"""
문제
해결
조건
* leading zero가 고려 되어야 한다 099 -> 100 or 0042 -> 0043
절차
1. strng 를 루프를 돌린다
2. 숫자가 나오는 index를 알아 낸다.
3. 슬라이스로 숫자부분을 추출한다, -> foobar001 일 때, index 가 6 이라면 s[6:] 을 숫자로 본다 / s[:6]은 문자로 본다
4. 슬라이싱 숫자 부분의 길이를 체크 하고, int(s[x:])를 만들고 1을 더한다
5. 길이체크한 만큼 0 ljust를 포함해준다
6. 문자와 숫자 부분을 더해준다
7. 숫자가 나오는 index가 없으면 주어진 strng에 1을 더한다
테스트
해피패스
    1. string 뒤에 숫자가 없는 경우
    2. string 뒤에 숫자가 있는 경우
조건
    1. leading zero -> ex) 099 -> 100 
"""
