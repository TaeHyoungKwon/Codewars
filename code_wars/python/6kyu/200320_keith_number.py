import unittest
from collections import deque


def is_keith_number(n):
    queue = deque()
    initial_list = [int(ele) for ele in str(n)]
    queue.extend(initial_list)

    result = sum(initial_list)
    cnt = 1

    if len(str(n)) == 1:
        return False

    while result <= n:
        queue.append(result)
        if result == n:
            return cnt
        cnt += 1
        result = result * 2 - queue.popleft()

    return False


class TestKeithNumber(unittest.TestCase):
    def test_should_return_3_when_given_n_is_14(self):
        n = 14
        actual = is_keith_number(n)
        self.assertEqual(actual, 3)

    def test_should_return_false_when_sum_of_n_is_less_than_10(self):
        n = 4
        actual = is_keith_number(n)
        self.assertEqual(actual, False)

    def test_login_should_be_same_between_login_user_and_user_when_login_succeed(self):
        # Given: Set user
        # When: Call login with user
        # Then: user should be login_user
        pass
    
    def test_login_should_be_not_same_between_login_user_and_user_when_login_failed(self):
        # Given: Set user
        # When: Call login with different user
        # Then: user should not be login_user
        pass

    def test_login_should_return_404_not_found_when_user_is_not_found(self):
        # Given: Set user
        # When: Call login with user is not found in DB
        # Then: login shold return 404_not_found

    def test_login_should_return_401_unauthorized_when_password_is_not_match(self):
        # Given: Set user
        # When: 패스워드가 일치하지 않는 user 호출
        # Then: 로그인 메서드는 401_unauthorized를 리턴