import re
import unittest


class FileNameExtractor:
    @staticmethod
    def extract_file_name(dirty_file_name: str) -> str:
        searched = re.search(r"\d+_([a-zA-Z_]+\.\w+)", dirty_file_name)
        return searched.group(1)


class TestFileNameExtractor(unittest.TestCase):
    def test_extract_file_name(self):
        ext = FileNameExtractor()
        self.assertEqual(
            ext.extract_file_name(dirty_file_name="1231231223123131_FILE_NAME.EXTENSION.OTHEREXTENSION"),
            "FILE_NAME.EXTENSION",
        )


    def test_extract_file_name_with_edge_case_2(self):
        ext = FileNameExtractor()
        self.assertEqual(
            ext.extract_file_name(dirty_file_name="9201144____AiOymFAxCIt.2H1.s2vq1329A8w7pY4U_tQEr"),
            "___AiOymFAxCIt.2H1",
        )


"""
문제
- 규칙이 있는 string에서 원하는 파일이름과 확장자를 뽑아낸다.
해결
- 정규표현식을 이용해서 내가 원하는 문자열을 뽑아낸다.
조건
1. 숫자로 시작한다(date를 나타냄)
2. underscore가 뒤따른다
3. extension과 함께 filename를 가진다
4. 끝에 추가적인 extension 이 붙는다
절차
1. "숫자_" 형태로 된 부분은 제외한다
2. "문자열_" 로 된 형태를 "." 이 나올 때까지 해서 파일 이름으로 뽑는다
3. 이후의 "문자열" 을 "."이 나오기전까지 뽑아서 확장자로 인식한다.
4. 문자열과 확장자를 . 으로 join 한다

"""