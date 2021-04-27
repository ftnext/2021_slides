.. role:: raw-html(raw)
    :format: html

============================================================
object活用ことはじめ 〜dataclassと特殊メソッド〜
============================================================

:Event: Pythonエンジニア勉強会
:Presented: 2021/04/27 nikkie

❓ Question（チャット💬 お願いします🙏）
============================================================

1. dataclass使ったことありますか？
2. 「特殊メソッド」ピンと来ますか？

はじめに
============================================================

* Python界隈では *自己紹介のエイリアス* が「お前、誰よ」（`ルーツ <https://www.ianlewis.org/jp/pycon-mini-jp>`_） **活用ください！**

お前、誰よ
------------------------------------------------

* 我が名は **にっきー** （:raw-html:`<i class="fab fa-twitter"></i>` `@ftnext <https://twitter.com/ftnext>`_ / :raw-html:`<i class="fab fa-github"></i>` `@ftnext <https://github.com/ftnext>`_）
* **Python歴3年半** ほど。現在は `ユーザベース <https://www.wantedly.com/projects/622337>`_ 所属のデータサイエンティスト
* Love anime!!（＠　🎺🎷🔥　🌲🌳🐲　🐴🍚🚿　👩‍🎨🐯🐟）

    ペアプロ・TDDでPython書いて、日々楽しく働いています😃

Pythonエンジニア勉強会（この勉強会）
------------------------------------------------

    「Python」について、活用ユーザーが集まり最新トレンド共有やLTを行う勉強会イベント

https://tech-street.connpass.com/event/210087/

Pythonの最新トレンドが共有される他の勉強会イベント
------------------------------------------------------------------------------------------------

* Pythonのカンファレンス **PyCon JP**
* YouTube `PyCon JP 2020 アーカイブ動画 <https://youtube.com/playlist?list=PLMkWB0UjwFGkgC4eCjltRKD1HS_eups9A>`_
* nikkieはPyCon JP 2021 **座長** 🇨🇭です。`スタッフ募集中 <https://pyconjp.blogspot.com/2021/01/2021-staff-application-start.html>`_！📣🙏

LTするので宣伝させてください🙏
------------------------------------------------

* `みんなのPython勉強会 6/9(水) <https://startpython.connpass.com/event/210169/>`_ は登壇者公募中！（`フォーム <https://forms.gle/iAquB7bJ8Jjm9XAJ6>`_）
* トークテーマは『**あなたのオススメPython本**』📚
* 持ち時間は **10分** で、短くてもOK

ここから本題：object活用ことはじめ 〜dataclassと特殊メソッド〜
========================================================================================================================

1. dataclass使ったことありますか？
2. 「特殊メソッド」ピンと来ますか？

→ nikkieはこれらを活用し始められて、Python書くのがすごく **楽しい** ！😆

おことわり
------------------------------------------------

* Python活用事例や最新トレンドではありません🙇‍♂️（私も知りたい！）
* Pythonを活用するために **Pythonの裏側を知りましょう**
* この話が「当たり前」という人は、Pythonを活用できていると思います！
* 動作環境：Python 3.9.4

補注：Python活用事例が聞きたかったという方へ
------------------------------------------------

nikkieの過去のアウトプットから

* PyCon Taiwan 2020で発表 `PyCon JP スタッフ活動でのPython活用事例 <https://docs.google.com/presentation/d/1uVMYiCewRAVITS7-uw0J9u9F3LTj0w--_vWmzLGr4so/edit?usp=sharing>`_ （英語）
* 2020年Remote.pyで発表「`Pythonで自動化スクリプトを作るときに考えていること <https://docs.google.com/presentation/d/1YP03-0THNmWLdqIi_hrcgi-k7y_2G7jj5iWXf973Ew4/edit?usp=sharing>`_」

目次：object活用ことはじめ 〜dataclassと特殊メソッド〜
------------------------------------------------------------------------------------------------

* Pythonのobject
* objectどうしが「等しい」
* 特殊メソッドでobjectを反復できる

object活用ことはじめ 〜dataclassと特殊メソッド〜
============================================================

* **Pythonのobject**
* objectどうしが「等しい」
* 特殊メソッドでobjectを反復できる

objectとは
------------------------------------------------

    Python における オブジェクト (object) とは、**データ** を抽象的に表したものです。

`Python 言語リファレンス - 3. データモデル - 3.1 . オブジェクト、値、および型 <https://docs.python.org/ja/3/reference/datamodel.html#objects-values-and-types>`_ （強調は引用者による）

大事なことなので、2回
------------------------------------------------

    Python プログラムにおける **データ** は全て、オブジェクトまたはオブジェクト間の関係として表されます。

`Python 言語リファレンス - 3. データモデル - 3.1 . オブジェクト、値、および型 <https://docs.python.org/ja/3/reference/datamodel.html#objects-values-and-types>`_ （強調は引用者による）

補注：オブジェクト指向とは無関係です
------------------------------------------------

* Pythonのオブジェクト(object) ＝ **データ** という話をしています
* 示唆を与えてくださったブログ：`オブジェクト指向という言葉を使わずともコードは書ける <https://essay.zopfco.de/entry/2020/12/12/231752>`_

用語集でobjectを引く
------------------------------------------------

    状態 (**属性** や値) と定義された振る舞い (**メソッド**) をもつ全てのデータ

https://docs.python.org/ja/3/glossary.html#term-object （強調は引用者による）

用語集でobjectを引く 続き
------------------------------------------------

    もしくは、全ての 新スタイルクラス の究極の **基底クラス** のこと。

.. code-block:: python
    :linenos:

    class SomeClass:  # クラスはobjectを継承している
        pass

小まとめ🥟：Pythonのobjectは2重の意味合い
------------------------------------------------

* 属性とメソッドを持つ **データ**
* どんなクラスも ``object`` を継承（究極の **基底クラス**）

👉 ここからはPythonにおけるデータの *振る舞い* について話していきます

object活用ことはじめ 〜dataclassと特殊メソッド〜
============================================================

* Pythonのobject
* **objectどうしが「等しい」**
* 特殊メソッドでobjectを反復できる

❓ Question（チャット💬 お願いします🙏）
============================================================

次のデータ（馬🐴の名を表すobject）は等しい？

.. code-block:: python

    >>> class RaceHorseName:
    ...     """競走馬の名前を表す"""
    ...     def __init__(self, value):
    ...         self.value = value
    >>> rice = RaceHorseName("ライスシャワー")
    >>> rice2 = RaceHorseName("ライスシャワー")
    >>> rice == rice2  # doctest: +SKIP

次のデータ（object）は等しい？ - 🙅‍♀️ （ぶっぶー）
------------------------------------------------------------------------------------------------

馬の名は、等しくない

.. code-block:: python

    >>> rice.value == rice2.value  # value属性の値は等しい
    True
    >>> rice is rice2  # オブジェクトは同一ではない
    False
    >>> rice == rice2
    False

比較演算子 ``==``
------------------------------------------------

    ``x==y`` は ``x.__eq__(y)`` を呼び出します

https://docs.python.org/ja/3/reference/datamodel.html#object.__eq__

``__eq__`` メソッド？
------------------------------------------------

* ``RaceHorseName`` には実装していない
* **究極の基底クラス** ``object`` が ``__eq__`` を持つ
* その実装は ``True if x is y else NotImplemented`` （`ドキュメント <https://docs.python.org/ja/3/reference/datamodel.html#object.__eq__>`_）

``is``：同一性の比較
------------------------------------------------

    ``x is y`` は、 x と y が **同じオブジェクトを指す** とき、かつそのときに限り真になります。 オブジェクトの同一性は id() 関数を使って判定されます。

https://docs.python.org/ja/3/reference/expressions.html#is （強調は引用者による）

.. code-block:: python

    >>> rice is rice  # オブジェクトは同一
    True

小まとめ🥟：等しくなかった理由
------------------------------------------------

* ``rice == rice2`` は、オブジェクトの *同一性* を比較する結果になった
* ``rice`` と ``rice2`` は **別々のオブジェクトを指す** ので、``False``
* （組み込み関数 ``id`` で、別々のオブジェクトを指していることを確認できます）

「等しい」は作れる！
============================================================

* ``value`` 属性の **値が等しい** とき、**データ（object）は等しく** したい（ライスシャワーはライスシャワー）
* 👉 ``__eq__`` メソッドを ``RaceHorseName`` クラスで実装する（``object`` の ``__eq__`` を **オーバーライド**）

``__eq__`` メソッド オーバーライド
------------------------------------------------

.. code-block:: python

    >>> class RaceHorseName:
    ...     def __init__(self, value):
    ...         self.value = value
    ...     def __eq__(self, other):
    ...         if not isinstance(other, self.__class__):
    ...             return NotImplemented  # 👉 Appendix
    ...         return self.value == other.value

``__eq__`` メソッド オーバーライド
------------------------------------------------

.. code-block:: python

    >>> rice = RaceHorseName("ライスシャワー")
    >>> rice2 = RaceHorseName("ライスシャワー")
    >>> rice == rice2  # value属性が等しいときに、データとして等しくできた
    True
    >>> rice is rice2
    False

「等しい」はもっと簡単に作れる：dataclass
------------------------------------------------

.. code-block:: python

    >>> from dataclasses import dataclass
    >>> @dataclass
    ... class RaceHorseName:
    ...     value: str
    >>> rice = RaceHorseName("ライスシャワー")
    >>> rice2 = RaceHorseName("ライスシャワー")
    >>> rice == rice2
    True

``@dataclasses.dataclass``
------------------------------------------------
    
* 「dataclass使ったことありますか？」はこれを指していました
* クラスに付けるデコレータ（`用語集 <https://docs.python.org/ja/3/glossary.html#term-decorator>`_）
* ``RaceHorseName`` クラスに ``__eq__`` を作り、``object`` の ``__eq__`` をオーバーライド

補注：以下2つのデコレータの機能は同じ (👉 Appendix)
------------------------------------------------------------------------------------------------

.. code-block:: python

    @dataclass
    class RaceHorseName1:
        ...
    
    @dataclass()
    class RaceHorseName2:
        ...

``@dataclasses.dataclass`` の ``eq`` 引数
------------------------------------------------

    ``eq``: (デフォルトの)真の場合、 __eq__() メソッドが生成されます。このメソッドはクラスの比較を、そのクラスの **フィールドからなるタプルを比較** するように行います。
    比較する2つのインスタンスのクラスは同一でなければなりません。

https://docs.python.org/ja/3/library/dataclasses.html#dataclasses.dataclass （強調は引用者による）

``@dataclasses.dataclass`` によって
------------------------------------------------

* ``RaceHorseName`` クラスに **__eq__メソッドが作られた**
* この ``__eq__`` では、クラスが同じことと ``(self.value, )`` を比較
* 👉 **クラスが同じで、上記タプルが等しい** ので、``rice == rice2`` は ``True`` と評価された

.. 確認用
    >>> (rice.value, ) == (rice2.value, )
    True

小まとめ🥟：「等しい」の作り方
------------------------------------------------

* クラスに ``__eq__`` メソッドを実装して、``object`` の ``__eq__`` をオーバーライドすればいい
* ``@dataclasses.dataclass`` でクラスをデコレートすると ``__eq__`` メソッドが作られて、**少ない記述で済む** 🙌

object活用ことはじめ 〜dataclassと特殊メソッド〜
============================================================

* Pythonのobject
* objectどうしが「等しい」
* **特殊メソッドでobjectを反復できる**

特殊メソッド
------------------------------------------------

* ``__eq__`` などのメソッドのこと（`特殊メソッド名一覧 <https://docs.python.org/ja/3/reference/datamodel.html#specialnames>`_）
* 究極の基底クラス ``object`` で定義されていて、**オーバーライド** することで **データの振る舞いをカスタマイズ** できる
* マジックメソッド、ダンダーメソッドとも呼ばれる（👉 Appendix）

例：反復できるobjectを作りたい
------------------------------------------------

``RaceHorseName`` クラスのデータをいくつも持たせられるクラス ``RaceHorseNames``

.. code-block:: python

    rice = RaceHorseName("ライスシャワー")
    bourbon = RaceHorseName("ミホノブルボン")
    names = RaceHorseNames([rice, bourbon])
    for name in names:
        print(f"{name.value}さん、こんにちは")

反復できるobjectの作り方
------------------------------------------------

* 今回は **Sequence というクラスを継承** して、特殊メソッドをオーバーライドして作成
* ``for`` 文で繰り返したいだけであれば、Iterable（`用語集 <https://docs.python.org/ja/3/glossary.html#term-iterable>`_）になればいいので、他の特殊メソッドをオーバーライドしてもできます

用語集より「シーケンス」
============================================================

リスト、タプル、文字列もシーケンス

    整数インデクスによる効率的な要素アクセスを ``__getitem__()`` 特殊メソッドを通じてサポートし、長さを返す ``__len__()`` メソッドを定義した iterable です

https://docs.python.org/ja/3/glossary.html#term-sequence

反復できるobjectの作り方
------------------------------------------------

* 以下の特殊メソッドを実装

  * ``__len__``
  * ``__getitem__``

* オススメ：**抽象基底クラスを継承** する

抽象基底クラスを継承して反復できるobjectを作る
------------------------------------------------

* ``collections.abc.Sequence`` を継承する
* 継承することで、``__len__``、``__getitem__`` の **実装が強制される**
* オススメ理由：実装する特殊メソッドを覚えておくより、継承する抽象基底クラスを覚えておくほうが覚える量が少ない（※個人の見解です）

補注：実装が強制される様子
------------------------------------------------

.. code-block:: python

    >>> from collections.abc import Sequence
    >>> @dataclass
    ... class RaceHorseNames(Sequence):
    ...     names: list[RaceHorseName]  # 👉 Appendix
    >>> names = RaceHorseNames([])
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: Can't instantiate abstract class RaceHorseNames with abstract methods __getitem__, __len__

``__len__``
------------------------------------------------

    **オブジェクトの長さ** を 0 以上の整数で返さなければなりません。

https://docs.python.org/ja/3/reference/datamodel.html#object.__len__ （強調は引用者による）

``__len__`` を実装
------------------------------------------------

.. code-block:: python

    >>> @dataclass
    ... class RaceHorseNames(Sequence):
    ...     names: list[RaceHorseName]
    ...     # リストnamesの長さをオブジェクトの長さとする
    ...     def __len__(self):
    ...         return len(self.names)

``__getitem__``
------------------------------------------------

    self[key] の値評価 (evaluation) を実現するために呼び出されます。
    シーケンスの場合、**キーとして整数とスライスオブジェクトを受理** できなければなりません。

    https://docs.python.org/ja/3/reference/datamodel.html#object.__getitem__ （強調は引用者による）

``__getitem__`` を実装
------------------------------------------------

.. code-block:: python

    >>> @dataclass
    ... class RaceHorseNames(Sequence):
    ...     names: list[RaceHorseName]
    ...     # -- __len__ は省略 --
    ...     # namesはリストなので、整数もスライスも受け付けられる
    ...     def __getitem__(self, key):
    ...         if isinstance(key, slice):
    ...             return self.__class__(self.names[key])
    ...         return self.names[key]

.. RaceHorseNamesクラスの全容
    >>> @dataclass
    ... class RaceHorseNames(Sequence):
    ...     names: list[RaceHorseName]
    ...     def __getitem__(self, key):
    ...         if isinstance(key, slice):
    ...             return self.__class__(self.names[key])
    ...         return self.names[key]
    ...     def __len__(self):
    ...         return len(self.names)

反復できるobjectを実装！🙌
------------------------------------------------

.. code-block:: python

    >>> rice = RaceHorseName("ライスシャワー")
    >>> bourbon = RaceHorseName("ミホノブルボン")
    >>> names = RaceHorseNames([rice, bourbon])
    >>> for name in names:
    ...     print(f"{name.value}さん、こんにちは")
    ライスシャワーさん、こんにちは
    ミホノブルボンさん、こんにちは

小まとめ🥟：特殊メソッドでobjectを反復できる
------------------------------------------------

* クラスに **__len__、__getitem__** を実装した
* **Sequence を継承** することで、実装が強制される（推奨納言）
* Pythonのデータ (object) の振る舞いのカスタマイズの一例

まとめ🌯：object活用ことはじめ 〜dataclassと特殊メソッド〜
============================================================

* Pythonのobjectはデータであり、究極の基底クラス
* ``object`` が持つ **特殊メソッドをオーバーライド** して、データの振る舞いをカスタマイズ 😆

  * **@dataclass** で特殊メソッド作成
  * 抽象基底クラスを継承して特殊メソッド実装

ご清聴ありがとうございました
------------------------------------------------

**Enjoy** development with ``object``!

References、**Appendix** が続きます（よろしければどうぞ！）

References
============================================================

* PyCon JP 2017 `Pythonはどうやってlen関数で長さを手にいれているの？ <https://www.slideshare.net/shimizukawa/how-does-python-get-the-length-with-the-len-function>`_

  * このLTと特に関係するのは、スライド43。このトーク自体オススメです

* 『`ゼロから作るDeep Learning ❸――フレームワーク編 <https://www.oreilly.co.jp/books/9784873119069/>`_』

  * ``__call__`` , ``__add__`` , ``__radd__`` が紹介されていて興味を持ちました

.. include:: appendix.rst.txt
