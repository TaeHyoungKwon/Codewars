class Dictionary(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def newentry(self, word: str, definition: str) -> None:
        self[word] = definition

    def look(self, key: str) -> str:
        return self.get(key, f"Can't find entry for {key}")


class TestDictionary:
    def test_look_should_return_value_on_key_does_exist(self):
        # Given
        d = Dictionary(**{
            "Apple": "A fruit",
            "Monkey": "An Animal"
        })
        # Expected
        assert d.look("Apple") == "A fruit"
        assert d.look("Monkey") == "An Animal"

    def test_look_should_return_value_on_key_does_not_exist(self):
        # Given
        d = Dictionary()
        # Expected
        melon = "Melon"
        assert d.look(melon) == f"Can't find entry for {melon}"

    def test_newentry_should_return_value_on_key_does_exist(self):
        # Given
        d = Dictionary()
        d.newentry("Orange", "orange is very fresh.")
        # Expected
        assert d.look("Orange") == "orange is very fresh."


"""
문제
- dict 기능을 랩핑한 Dictionary 클래스를 만들어야 한다
해결
- 아래 조건대로 문제를 해결하자
조건
1. newentry -> dict에 key value를 추가함
2. look -> dict의 key로 value를 리턴함
3. look에서 해당하는 key가 없으면 Can't find entry for {word} 를 리턴함 
절차
1. 각 메소드 별로 인수조건을 세우고, 테스트를 만들어보자

테스트
1. newentry
    - 성공
        - key, value를 입력 했을 때, look을 통해서 해당 key로 접근하면 value가 나와야 한다
2. look
    - 성공
        - Dictionary에 저장된 값으로 부터 해당 key가 있으면 value를 리턴해줘야 한다
    - 실패
        - Dictionary에 저장된 값으로 부터 해당 key가 없으면 Can't find entry for {word} 를 리턴함 

"""