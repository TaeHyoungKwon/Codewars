from contextlib import contextmanager
import logging
import unittest


def my_function():
    logging.debug("디버깅 데이터")
    logging.error("이 부분은 오류 로그")
    logging.debug("추가 디버깅 데이터")


@contextmanager
def debug_logging(level):
    logger = logging.getLogger()
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield
    finally:
        logger.setLevel(old_level)


def solution():
    with debug_logging(logging.DEBUG):
        print("* 내부:")
        my_function()

    print("* 외부:")
    my_function()


class TestSolution(unittest.TestCase):
    def test_solution(self):
        solution()
