# from typing import TypeGuard, Union

# def is_string(x: object) -> TypeGuard[str]:
#     return isinstance(x, str)

# def process_value_custom_check(x: int | str) -> None:
#     if isinstance(x, str):
#         assert isinstance(x, str)  # mypy에게 타입을 명시적으로 알림
#         print(x.upper())  # 오류 없음
#     else:
#         print(x + 1)  # 오류 없음

# process_value_custom_check("hello")
# process_value_custom_check(123)


from typing import Optional

def is_none(x: Optional[str]) -> bool:
    return x is None

def handle_value(x: Optional[str]) -> None:
    if is_none(x):
        print("No value!")
        return
    # 여기서는 x가 None이 아님을 확정
    # 정적 분석기는 x를 'str'로 간주
    print(x.upper())  # OK

handle_value("hello")
handle_value(None)
