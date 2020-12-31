import unittest
from unittest.mock import mock_open, patch

from design_pattern.srp.srp import Bookshelf, BookshelfFileIO


class TestBookshelf(unittest.TestCase):
    def test_development_book_with_add_book(self):
        # Given: 책 3권을 책꽂이에 추가한다
        book_shelf = Bookshelf()
        book_shelf.add("refactoring")
        book_shelf.add("clean_code")
        book_shelf.add("clean_coder")

        # When: 책꽂이 꽂힌 전체 책 목록을 출력하면
        actual = book_shelf.all_list()

        # Then: 실제 값은 expected와 같아야 한다
        expected = "1: refactoring\n2: clean_code\n3: clean_coder"
        self.assertEqual(actual, expected)

    def test_development_book_with_remove_book(self):
        # Given: 책 3권을 책꽂이에 추가한다
        bookshelf = Bookshelf()
        bookshelf.add("refactoring")
        bookshelf.add("clean_code")
        bookshelf.add("clean_coder")
        # And: clean_coder 책을 제외한다
        bookshelf.remove("clean_coder")

        # When: 책꽂이 꽂힌 전체 책 목록을 출력하면
        actual = bookshelf.all_list()

        # Then: 실제 값은 expected와 같아야 한다
        expected = "1: refactoring\n2: clean_code"
        self.assertEqual(actual, expected)

    def test_bookshelf_with_save(self):
        # Given: 책 3권을 책꽂이에 추가한다
        bookshelf = Bookshelf()
        bookshelf.add("refactoring")
        bookshelf.add("clean_code")
        bookshelf.add("clean_coder")
        # And: File IO 사용을 위한 인스턴스를 추가한다
        io = BookshelfFileIO()

        # When: 책꽂이 꽂힌 전체 책 목록을 파일로 저장하면
        open_mock = mock_open()
        with patch("builtins.open", open_mock):
            io.save_to_file(bookshelf, "book_list.txt")

        # Then: 텍스트 파일에 저장된 값을 불러왔을 때, expected와 같아야 한다
        open_mock.assert_called_once_with("book_list.txt", "w")
        expected = "1: refactoring\n2: clean_code\n3: clean_coder"
        open_mock.return_value.write.assert_called_once_with(expected)
