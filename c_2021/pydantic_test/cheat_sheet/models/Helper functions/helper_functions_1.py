from datetime import datetime

from pydantic import BaseModel, ValidationError


class User(BaseModel):
    id: int
    name = "John Doe"
    signup_ts: datetime = None


if __name__ == "__main__":
    """
    parse_obj
    * __init__ 메소드와 비슷한 역할을 한다
    * 다른 점은 오직 dict로 만 넘겨야 하고, 그렇지 않으면 ValidationError를 일으킨다
    """
    m = User.parse_obj({"id": 123, "name": "James"})
    print(m)
    # id=123 signup_ts=None name='James'

    try:
        User.parse_obj(["not", "a", "dict"])
    except ValidationError as e:
        print(e)
        """
        1 validation error for User
        __root__
        User expected dict not list (type=type_error)
        """

    m = User.parse_raw('{"id": 123, "name": "James"}')
    print(m)
    # id=123 signup_ts=None name='James'
    """
    parse_raw 작성 해야함
    """
