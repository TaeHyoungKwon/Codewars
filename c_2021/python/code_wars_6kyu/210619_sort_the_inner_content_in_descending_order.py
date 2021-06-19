import unittest


def sort_the_inner_content(words):
    def generate_sort_the_inner_content():
        for word in words.split():
            if len(word) == 1:
                yield word
                continue
            first = word[0]
            last = word[-1]
            reversed_middle_word = "".join(sorted(word[1:-1], reverse=True))
            yield f"{first}{reversed_middle_word}{last}"
    return " ".join(generate_sort_the_inner_content())
    
    
class TestSortTheInnerContent(unittest.TestCase):
    def test_sort_the_inner_content(self):
        self.assertEqual(sort_the_inner_content(words="sort the inner content in descending order"), "srot the inner ctonnet in dsnnieedcg oredr")

    def test_sort_the_inner_content_when_one_of_the_word_length_is_one(self):
        self.assertEqual(sort_the_inner_content(words="zhmdbizzn pt h lgquvngcl wkhwmpyu vo qhuqswz h gi jyauml"), "zzzmihdbn pt h lvuqnggcl wywpmkhu vo qwusqhz h gi jyumal")


"""
문제
* 주어진 words의 각각 word를 맨앞뒤를 제외한 나머지 letter들을 내림차순 정렬해서 리턴해라
해결
* split을 word를 나눈 이후에, 맨앞뒤를 제외한 나머지에 대해서 내림차순으로 재 정렬 처리 후, 수정된 값을 저장하는 새로운 list를 만들고 그 list를 join 한다
조건
1. input -> words:str , output -> str
절차
1. words를 split으로 쪼갠다
2. 맨앞, 맨뒤 char를 따로 저장한다,
3. 루프를 돌면서, 내림 차순으로 word를 정렬 후, sorted(word[1:-1f], reversed=True) 와 맨앞 맨뒤를 뽑아낸것을 합쳐서 새로운 리스트에 넣는다
4. 새로운 리스트 resut 를 join으로 묶어서 리턴한다
테스트
* 다른 특이한 조건이 없어서 해피패스 1개만 해도 될것 같다
"""