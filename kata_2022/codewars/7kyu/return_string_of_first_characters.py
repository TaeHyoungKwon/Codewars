def make_string(s: str) -> str:
    return "".join(word[0] for word in s.split())


class TestMakeString:
    def test_make_string(self):
        assert make_string(s="sees eyes xray yoat") == "sexy"


"""
문제
* 주어진 변수 s의 각 단어의 맨 앞자만 따서 합친 후 리턴해야 한다
해결
* 문제 조건과 절차에 맞게 답을 풀자
조건
- input and output
    - input s: str / output -> str
- 적어도 1개의 공간이 있음 leading/trailing 공간 없음 letter와 space만 가짐
절차
1. Workflow
    1. split()을 해서 각 단어별로 쪼갠다
    2. for loop를 돌면서 맨 앞에 있는 char를 뽑아낸다
    3. 2번에 뽑아낸 것들을 합쳐서 리턴한다
테스트
- 띄어쓰기가 몇개 있는 단어로 이루어진 문장 --> 조건을 봤을 때 이 케이스 밖에 없다
    
"""