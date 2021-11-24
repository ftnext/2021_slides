"""Dog class

ref: https://docs.python.org/ja/3/tutorial/classes.html#class-and-instance-variables
"""

import random


class Dog:
    """
    >>> random.seed(0)

    >>> dog = Dog("ラテ")
    >>> dog.add_trick("寝返り")
    >>> dog.add_trick("死んだふり")
    >>> dog.trick()
    '死んだふり'
    """

    def __init__(self, name: str) -> None:
        self.name = name
        self.tricks = []  # 犬が覚えた芸をリスト（＝配列）で表す

    def add_trick(self, trick: str) -> None:
        """犬に芸を覚えさせる"""
        self.tricks.append(trick)

    def trick(self) -> str:
        if not self.tricks:
            raise ValueError("覚えている芸がありません。add_trickして覚えさせてください")
        return random.choice(self.tricks)
