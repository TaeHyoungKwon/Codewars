import enum
import unittest


LIST_LENGTH = 3

A_GRADE_SCORE = 90
B_GRADE_SCORE = 80
C_GRADE_SCORE = 70
D_GRADE_SCORE = 60


class NoValue(enum.Enum):
    def __repr__(self):
        return '<%s.%s>' % (self.__class__.__name__, self.name)


class Grade(NoValue):
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    F = 'F'


def get_grade(s1, s2, s3):
    average_score = sum([s1, s2, s3]) // LIST_LENGTH

    if average_score >= A_GRADE_SCORE:
        return Grade.A.value
    elif average_score >= B_GRADE_SCORE:
        return Grade.B.value
    elif average_score >= C_GRADE_SCORE:
        return Grade.C.value
    elif average_score >= D_GRADE_SCORE:
        return Grade.D.value
    else:
        return Grade.F.value


class TestGetGrade(unittest.TestCase):
    def test_should_return_A_when_score_is_90_to_100(self):
        actual = get_grade(95, 90, 93)
        self.assertEqual(actual, Grade.A.value)

    def test_should_return_B_when_score_is_80_to_90(self):
        actual = get_grade(70, 70, 100)
        self.assertEqual(actual, Grade.B.value)

    def test_should_return_C_when_score_is_70_to_80(self):
        actual = get_grade(70, 70, 70)
        self.assertEqual(actual, Grade.C.value)

    def test_should_return_D_when_score_is_60_to_70(self):
        actual = get_grade(60, 60, 70)
        self.assertEqual(actual, Grade.D.value)

    def test_should_return_F_when_score_is_0_to_60(self):
        actual = get_grade(50, 50, 50)
        self.assertEqual(actual, Grade.F.value)
