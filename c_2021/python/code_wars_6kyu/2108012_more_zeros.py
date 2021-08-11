import unittest


# def more_zeros(s):
#     result = []
#     for digit in s:
#         binary_ascii = bin(ord(digit))[2:]
#         if binary_ascii.count("0") <= binary_ascii.count("1") or digit in result:
#             continue
#         result.append(digit)
#     return result

def is_zero_dominant(letter):
    s = format(ord(letter), 'b')
    return s.count("0") > s.count("1")


def more_zeros(s):
    return list(dict.fromkeys(letter for letter in s if is_zero_dominant(letter)))
    
    
class TestMoreZeros(unittest.TestCase):
    def test_more_zeros_on_no_duplicated_case(self):
        self.assertEqual(more_zeros(s='abcde'), ['a', 'b', 'd'])

    def test_more_zeros_on_duplicated_case(self):
        self.assertEqual(more_zeros(s='THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG'), ['T', 'H', 'E', 'Q', 'I', 'C', 'B', 'R', 'F', 'X', 'J', 'P', 'L', 'A', 'D'])


"""
문제
    * s가 주어질 때, 각 digit의 ascii 값을 2진수로 변환하고,1보다 0이 더 많은 digit에 해당하는 alphabet 를 모아서 리스트로 리턴해라
해결
    * 아래 절차대로 진행 
조건
    * 중복은 무시해야하는데, 순서는 유지되어야 한다
절차
    1. for loop를 돌린다(s)
    2. 각 digit을 ascii 로 변환한다
    3. 2번을 2진수로 번환한다
    4. 1보다 0이 많은지 검사한다
        - True이면,
            - 이미 list에 존재하는지 검사한다
                - 있다면, 패스한다
                - 없다면, 해당하는 알파벳을 list에 append 한다
        - False이면, 해당하는 알파벳은 패스한다  
    5. 루프를 모두 돌고나서 list를 리턴한다

테스트
1. 중복인 케이스
2. 중복이 아닌 케이스
"""