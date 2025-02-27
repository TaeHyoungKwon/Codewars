from typing import TypeVar, Generic, Type

T = TypeVar('T')

class Choose(Generic[T]):
    @classmethod
    def of(cls, type_: Type[T], v1: T, v2: T) -> T:
        """타입을 명시적으로 지정할 수 있는 제네릭 메서드
        
        Args:
            type_ (Type[T]): 명시적 타입
            v1 (T): 첫 번째 값
            v2 (T): 두 번째 값
        
        Returns:
            T: 사용자 입력이 0이면 v1, 아니면 v2를 반환
        """
        print(f"Type: {type_.__name__}, Values: {v1}, {v2}")
        result = int(input())
        return v1 if result == 0 else v2


if __name__ == "__main__":
    # 자바스러운 방식으로 사용
    print(Choose.of(int, 1, 0))
    print(Choose.of(str, "hello", "world"))
    print(Choose.of(float, 1.5, 2.5))