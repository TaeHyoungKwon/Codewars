class X:
    pass


class Rectangle:
    """
    오류는 없지만, 잘못된 클래스 형태
    length, width를 초기화 하는 곳이 없음..
    __init__ 을 정의 해주어야 한다
    """

    def area(self):
        return self.length * self.width



if __name__ == "__main__":
    print(X.__class__)  # <class 'type'>
    print(X.__class__.__base__)  # <class 'objects'>
