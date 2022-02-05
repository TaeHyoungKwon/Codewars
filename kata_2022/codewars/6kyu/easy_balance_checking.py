import re

import pytest


def balance(book):
    cleaned_book = re.sub("[^.a-zA-Z\d\s]+", "", book)
    split_cleaned_book = cleaned_book.splitlines()

    balance = float(split_cleaned_book.pop(0))
    reports = [f"Original Balance: {balance:.2f}"]
    expenses = []

    for index, line in enumerate(split_cleaned_book):
        if line == "":
            continue

        check_number, category, expense = line.split()
        expense = float(expense)
        expenses.append(expense)
        balance -= expense
        reports.append(f"{check_number} {category} {expense:.2f} Balance {balance:.2f}")

    reports.append(f"Total expense  {sum(expenses):.2f}")
    reports.append(f"Average expense  {sum(expenses) / len(expenses):.2f}")
    return "\r\n".join(reports)


no_blank = """1233.00
125 Hardware;! 24.8?;
123 Flowers 93.5
127 Meat 120.90
120 Picture 34.00
124 Gasoline 11.00
123 Photos;! 71.4?;
122 Picture 93.5
132 Tyres;! 19.00,?;
129 Stamps 13.6
129 Fruits{} 17.6
129 Market;! 128.00?;
121 Gasoline;! 13.6?;"""

no_blank_expected = """Original Balance: 1233.00\r
125 Hardware 24.80 Balance 1208.20\r
123 Flowers 93.50 Balance 1114.70\r
127 Meat 120.90 Balance 993.80\r
120 Picture 34.00 Balance 959.80\r
124 Gasoline 11.00 Balance 948.80\r
123 Photos 71.40 Balance 877.40\r
122 Picture 93.50 Balance 783.90\r
132 Tyres 19.00 Balance 764.90\r
129 Stamps 13.60 Balance 751.30\r
129 Fruits 17.60 Balance 733.70\r
129 Market 128.00 Balance 605.70\r
121 Gasoline 13.60 Balance 592.10\r
Total expense  640.90\r
Average expense  53.41"""

with_blank = """1000.00!=

125 Market !=:125.45
126 Hardware =34.95
127 Video! 7.45
128 Book :14.32
129 Gasoline ::16.10
"""

with_blank_expected = """Original Balance: 1000.00\r
125 Market 125.45 Balance 874.55\r
126 Hardware 34.95 Balance 839.60\r
127 Video 7.45 Balance 832.15\r
128 Book 14.32 Balance 817.83\r
129 Gasoline 16.10 Balance 801.73\r
Total expense  198.27\r
Average expense  39.65"""


first_line_is_invalid_position = """1000.0!=

125 Market !=:125.45
126 Hardware =34.95
127 Video! 7.45
128 Book :14.32
129 Gasoline ::16.10
"""

first_line_is_invalid_position_expected = """Original Balance: 1000.00\r
125 Market 125.45 Balance 874.55\r
126 Hardware 34.95 Balance 839.60\r
127 Video 7.45 Balance 832.15\r
128 Book 14.32 Balance 817.83\r
129 Gasoline 16.10 Balance 801.73\r
Total expense  198.27\r
Average expense  39.65"""


class TestBalance:
    @pytest.mark.parametrize(
        "book, expected",
        [
            (
                    no_blank, no_blank_expected
            ),
            (
                    with_blank, with_blank_expected
            ),
            (
                    first_line_is_invalid_position, first_line_is_invalid_position_expected
            )
        ]
    )
    def test_balance(self, book, expected):
        assert balance(book=book) == expected


"""
개선할 점

1. 정규표현식을 이해하고 적용하는 능력
2. split, splitlines의 활용
3. pop(0)을 사용함으로써, 코드 가독성 확보
4. expense를 중간에 계산하여서, 계산할 때, 적절히 활용
"""


"""
문제
* 주어진 book 변수에 대해서, 조건에 따라 formatting 된, 문자열을 리턴해라
해결
* 조건에 맞게 format을 만들어서 리턴한다
    - 계산해야하는 것
        - new_balance
        - total_expense
        - average expense
조건
* 용어
1. balance
2. each lines
    - check number
    - category
    - check amount
* 해야하는 것
1. letter, digit, dot, space를 남기고 모두 삭제해라
2. 다음과 같은 형태로 reformatting 해라
    1. Original Balance: {balance}\n
    2. {check_number} {category} {check_amount} Balance {new_balance}\r ... \n
    3. Total expense {total_expense}
    4. Average expense {average expense}
* 엣지 조건
1. 1개 혹은 그 이상의 라인이 blank 일수 도 있다
2. 소수점 2째자리 반올림해서 표현

절차
workflow
1. "\n" 기준으로 split() 해온다
1-1. 루프돌 때 공백은 무시한다
2. 첫번째의 경우는 Original_balance를 붙여서 새로운 리스트에 추가한다
3. 두번째 부터 끝까지는 new_balance를 계산해서 포맷대로 string을 만든 후 리스트에 추가한다
    - new_balance Original balance에서 expense를 뺀 것
    - total expense와 average expense를 미리 계산해서 변수에 저장해야한다
        - total expense는 원래 balance - 최종 balance 값
        - average expense는 total expense를 split 한 리스트의 길이 - 1 로 나눈것
4. 루프가 끝난 후에, total expense, average expense를 계산하여서 포맷에 맞게 리스트로 추가한다
테스트
1. 공백이 있을 때,
2. 공백이 없을 때,
"""