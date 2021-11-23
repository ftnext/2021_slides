"""Car class

ref: 『`スラスラわかるJava <https://www.shoeisha.co.jp/book/detail/9784798130798>`_』
"""


class Car:
    """
    >>> car = Car()
    >>> car.speed_up(60)
    60
    >>> car.speed_down(20)
    40
    """

    def __init__(self) -> None:
        self.speed = 0

    def speed_up(self, value: int) -> int:
        self.speed += value
        return self.speed

    def speed_down(self, value: int) -> int:
        self.speed -= value
        return self.speed
