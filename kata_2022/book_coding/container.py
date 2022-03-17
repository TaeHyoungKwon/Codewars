from typing import ClassVar


class Container:
    g: ClassVar = [0] * 1000  # 연결된 수조 그룹
    n: ClassVar = 1  # 그룹의 실제 크기
    x: ClassVar = 0  # 이 수조에 담긴 물의 양

    def get_amount(self) -> float:
        return self.x

    def add_water(self):
        y = self.x / self.n
        for i in range(self.n):
            self.g[i]["x"] = self.g[i]["x"] + y

    def connect_to(self, c):
        z = (self.x * self.n + c.x * c.n) / (self.n + c.n)

        for i in range(self.n):
            for j in c.n
