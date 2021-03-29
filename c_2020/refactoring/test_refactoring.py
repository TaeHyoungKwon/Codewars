import json
import unittest

from refactoring.main import statement


class TestStatement(unittest.TestCase):
    def test_statement(self):
        # Given: json 파일로 부터 invoice와 plays를 불러오고,
        with open("invoices.json") as json_file:
            invoice = json.load(json_file)[0]
        with open("plays.json") as json_file:
            plays = json.load(json_file)

        # When: statement 함수를 호출 하면,
        actual = statement(invoice, plays)

        # Then: 실제 값은 예상 값대로 나와야 한다.
        expected = (
            "청구 내역 (고객명: BigCo)\n"
            " Hamlet: $650.00 (55석)\n"
            " As You Like It: $580.00 (35석)\n"
            " Othello: $500.00 (40석)\n"
            "총액: $1,730.00\n"
            "적립 포인트': 47점\n"
        )
        self.assertEqual(actual, expected)
