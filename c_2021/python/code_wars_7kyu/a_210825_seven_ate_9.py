def seven_ate9(str_):
    result = []
    for index, ele in enumerate(str_):
        if index != len(str_) - 1 and index != 0:
            if ele == "9" and str_[index - 1] == "7" and str_[index + 1] == "7":
                continue
        result.append(ele)
    return "".join(result)


class TestSevenAte9:
    def test_seven_ate9(self):
        assert seven_ate9(str_='165561786121789797') == '16556178612178977'


"""
문제
* str_을 받아서, 7사이에 있는 9를 삭제해서 리턴해라
해결
* string 내 9가 나왔을 때, 앞뒤가 7 인지 검사하여 판별한다
조건
* 루프의 index를 체크하여서 문자열 길이와 같다면 검사하는 절차를 생략하고 패스한다
절차
1. str_ 루프를 돌린다
2. 각 수를 list에 append 한다
2. 만약 9가 나온다면, 앞뒤가 7인지 검사한다
    앞뒤가 7이라면, pass
    앞뒤가 7이 아니면, list에 append 한다

테스트
1.해피패스만 진행해도 될 것 같다
"""
