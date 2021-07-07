"""『現場で役立つシステム設計の原則』（増田 亨）を参考にした値オブジェクト実装例"""

from __future__ import annotations

import re
from collections.abc import Iterable
from dataclasses import dataclass
from typing import ClassVar


@dataclass(frozen=True)
class RaceHorseName:
    """カタカナの馬名を表すクラス

    >>> rice = RaceHorseName("ライスシャワー")
    >>> rice2 = RaceHorseName("ライスシャワー")
    >>> rice == rice2
    True

    不変

    >>> rice.value = "ミホノブルボン"
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<string>", line 4, in __setattr__
    dataclasses.FrozenInstanceError: cannot assign to field 'value'

    完全コンストラクタ

    >>> RaceHorseName("ラ")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: 不正: 2 文字未満
    >>> RaceHorseName("トッテモライスシャワー")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: 不正: 9 文字超
    >>> RaceHorseName("らイスシャワー")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: 不正: カタカナではない文字
    >>> RaceHorseName("ライスshower")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: 不正: カタカナではない文字
    >>> RaceHorseName("ラヰスシャワー")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: 不正: 使用禁止文字 ('ヰ', 'ヱ') を含む
    """

    value: str
    MIN_LENGTH: ClassVar[int] = 2
    MAX_LENGTH: ClassVar[int] = 9
    INVALID_CHARACTERS: ClassVar[Iterable[str]] = ("ヰ", "ヱ")

    def __init__(self, value: str):
        # 完全コンストラクタとして実装
        length = len(value)
        if length < self.MIN_LENGTH:
            raise ValueError(f"不正: {self.MIN_LENGTH} 文字未満")
        if length > self.MAX_LENGTH:
            raise ValueError(f"不正: {self.MAX_LENGTH} 文字超")
        if not self.is_katakana_only(value):
            raise ValueError("不正: カタカナではない文字")
        if self.does_include_invalid_characters(value):
            raise ValueError(f"不正: 使用禁止文字 {self.INVALID_CHARACTERS} を含む")
        object.__setattr__(self, "value", value)

    @staticmethod
    def is_katakana_only(string: str) -> bool:
        return bool(re.fullmatch(r"[\u30A0-\u30FF]+", string))

    @classmethod
    def does_include_invalid_characters(cls, string: str) -> bool:
        return any(c in string for c in cls.INVALID_CHARACTERS)
