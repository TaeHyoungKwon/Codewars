import abc
from dataclasses import dataclass


@dataclass
class BaseAlien:
    antenna: int
    eyes: int

    @abc.abstractmethod
    def is_valid(self):
        raise NotImplemented


@dataclass
class TroyMartian(BaseAlien):
    ...

    def is_valid(self):
        return self.antenna >= 3 and self.eyes <= 4


@dataclass
class VladSaturnian(BaseAlien):
    ...

    def is_valid(self):
        return self.antenna <= 6 and self.eyes >= 2


@dataclass
class GraemeMercurian(BaseAlien):
    ...

    def is_valid(self):
        return self.antenna <= 2 and self.eyes <= 3


ALIEN_DATACLASSES = [TroyMartian, VladSaturnian, GraemeMercurian]


def solution(antenna: int, eyes: int) -> str:
    return "\n".join(
        alien_dataclass.__name__
        for alien_dataclass in ALIEN_DATACLASSES
        if alien_dataclass(antenna, eyes).is_valid()
    )


if __name__ == "__main__":
    antenna = int(input())
    eyes = int(input())
    print(solution(antenna, eyes))
