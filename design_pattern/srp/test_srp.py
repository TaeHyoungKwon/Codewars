import unittest
from unittest.mock import mock_open, patch

from design_pattern.srp.srp import Bookshelf, BookshelfFileIO


class BookshelfTestMixin:
    def setUp(self) -> None:
        super().setUp()
        self.book_shelf = Bookshelf()
        self.book_shelf.add("refactoring")
        self.book_shelf.add("clean_code")
        self.book_shelf.add("clean_coder")


class TestBookshelf(BookshelfTestMixin, unittest.TestCase):
    def test_development_book_with_add_book(self):
        self.assertEqual(self.book_shelf.all_list(), "1: refactoring\n2: clean_code\n3: clean_coder")

    def test_development_book_with_remove_book(self):
        # Given: 기존 책 목록에서 clean_coder 책을 제외한다
        self.book_shelf.remove("clean_coder")

        # When: 책꽂이 꽂힌 전체 책 목록을 출력하면
        actual = self.book_shelf.all_list()

        # Then: 실제 값은 expected와 같아야 한다
        self.assertEqual(actual, "1: refactoring\n2: clean_code")


class TestBookshelfFielIO(BookshelfTestMixin, unittest.TestCase):
    def test_bookshelf_with_save(self):
        # Given: File IO 사용을 위한 인스턴스를 추가한다
        io = BookshelfFileIO()

        # When: 책꽂이 꽂힌 전체 책 목록을 파일로 저장하면
        open_mock = mock_open()
        with patch("builtins.open", open_mock):
            io.save_to_file(self.book_shelf, "book_list.txt")

        # Then: 텍스트 파일에 저장된 값을 불러왔을 때, expected와 같아야 한다
        open_mock.assert_called_once_with("book_list.txt", "w")
        expected = "1: refactoring\n2: clean_code\n3: clean_coder"
        open_mock.return_value.write.assert_called_once_with(expected)

    def test_bookshelf_with_load(self):
        # Given: File IO 사용을 위한 인스턴스를 추가한다
        io = BookshelfFileIO()
        expected = "1: refactoring\n2: clean_code\n3: clean_coder"

        # When: 책꽂이 꽂힌 전체 책 목록을 파일로 저장하면
        open_mock = mock_open(read_data=expected)
        with patch("builtins.open", open_mock):
            actual = io.load_to_file("book_list.txt")

        # Then: 텍스트 파일에 저장된 값을 불러왔을 때, expected와 같아야 한다
        self.assertEqual(actual, expected)
