import pytest


def solution():
    return


class TestSolution:
    def test_should_fail(self):
        pytest.fail()


"""
문제
- base converter를 만드는 것
- 이것은 bases와 알파벳 사이의 positive interger를 컨버팅 하는 것
해결
- 
조건
- input과 source는 같은 값과 타입을 나타내는 것으로 볼 수 있고 is_valid 하지 않아도 된다
- convert(input: str, source: str, tartget: str) -> is_valid 체크는 하지 않아도 됨
- input value의 최대값은 숫자로 인코딩 될 수 있다 precision의 loss 없이
- 함수는 이미 정의되것 뿐 아니라 어떤 임의의 알파벳들에 대해서도 동작해야한다
- 음수는 고려하지 않아도 된다. 
절차
1. input을 target 으로 바꾸면 ` 

테스트
1. 숫자 -> 숫자로 변경
-- dec -> bin, oct, hex 등으로 바로 변환
-- dec이 아니면, dec으로 변환후, 재변환
2. 숫자 -> 알파벳으로 변경
3. 알파벳 -> 숫자로 변경
4. 알파벳 -> 알파벳으로 변경

"""