============================================================
[ドラフト版] ``yield`` について
============================================================

:Event: ラクス Python Tips LT会
:Presented: 2021/02/25 nikkie

❓ Question（チャットお願いします🙏）
============================================================

ふだん ``yield`` 使ってますか？

- ガッツリ💪
- たまに😃
- 初耳！👂

お前、誰よ
============================================================

* ハンドルネーム「にっきー」（Twitter `@ftnext <https://twitter.com/ftnext>`_ / GitHub `@ftnext <https://github.com/ftnext>`_）
* Python歴3年。データサイエンティストなう
* Love anime!!（＠　🎺🎷🔥　🌈　🏔🏕　👩‍🎨🐯🐟）
* tips: Python界隈では **自己紹介のエイリアス** が「お前、誰よ」（`ルーツ <https://www.ianlewis.org/jp/pycon-mini-jp>`_）

お前、誰よ × tips
------------------------------------------------

関わっているPythonコミュニティ

* 毎月第2水曜の `みんなのPython勉強会 <https://startpython.connpass.com/>`_
* Pythonのカンファレンス PyCon JP の `アーカイブ <https://youtube.com/playlist?list=PLMkWB0UjwFGkgC4eCjltRKD1HS_eups9A>`_

PyCon JP 2021座長です。`スタッフ募集中 <https://pyconjp.blogspot.com/2021/01/2021-staff-application-start.html>`_！📣

LT：``yield`` について
============================================================

Python Tipsと聞いて、浮かんだネタの1つが ``yield`` でした

* ``yield`` とは
* ``yield`` よき
* ``yield`` こんなことまで
* ``yield`` 別の使い方

``yield`` について
============================================================

* ``yield`` とは 👈
* ``yield`` よき
* ``yield`` こんなことまで
* ``yield`` 別の使い方

``yield`` の簡単な例
------------------------------------------------

.. code-block:: python

    def easy_generator():
        yield "👩"
        yield "🐯"
        yield "🐟"

用語「ジェネレータ」
------------------------------------------------

* ``yield`` を使った **関数** （`用語集 <https://docs.python.org/ja/3/glossary.html#term-generator>`_）
* 例：先の関数 ``easy_generator`` もジェネレータ

.. doctestを通すための下準備
    >>> def easy_generator():
    ...     yield "👩"
    ...     yield "🐯"
    ...     yield "🐟"

もう一つの用語「ジェネレータイテレータ」
------------------------------------------------

* ジェネレータ関数の **返り値** （`用語集 <https://docs.python.org/ja/3/glossary.html#term-generator-iterator>`_）

.. code-block:: python

    >>> g = easy_generator()  # gはジェネレータイテレータ
    >>> type(g)
    <class 'generator'>

次の要素を取得 ``next``
------------------------------------------------

* 組み込み関数 ``next`` は、*イテレータ* の ``__next__()`` メソッドを呼び出し、次の要素を取得（`ドキュメント <https://docs.python.org/ja/3/library/functions.html#next>`_）

.. code-block:: python

    >>> next(g)  # ジェネレータイテレータの次の要素
    '👩'

``yield`` で一時停止
------------------------------------------------

``next(g)`` で 1行目の ``yield`` で値が返され、**一時停止**

.. code-block:: python

    def easy_generator():
        yield "👩"  # 👈
        yield "🐯"
        yield "🐟"

再開 & 一時停止
------------------------------------------------

.. code-block:: python

    >>> next(g)  # 次の要素
    '🐯'

.. code-block:: python

    def easy_generator():
        yield "👩"
        yield "🐯"  # 👈
        yield "🐟"

再度 再開 & 一時停止
------------------------------------------------

.. code-block:: python

    >>> next(g)  # 次の要素
    '🐟'

.. code-block:: python

    def easy_generator():
        yield "👩"
        yield "🐯"
        yield "🐟"  # 👈

次がない時： ``StopIteration`` 例外（`ドキュメント <https://docs.python.org/ja/3/library/exceptions.html#StopIteration>`_）
------------------------------------------------

.. code-block:: python

    >>> next(g)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration

``for`` 文で繰り返せる
------------------------------------------------

返り値はジェネレータ **イテレータ**

.. code-block:: python

    >>> for item in easy_generator():
    ...     print(item)
    ...
    👩
    🐯
    🐟

tips: ``StopIteration`` 例外は繰り返しの仕組みに関係

``yield`` について
============================================================

* ``yield`` とは
* ``yield`` よき 👈
* ``yield`` こんなことまで
* ``yield`` 別の使い方

``yield`` 何がいいの？
------------------------------------------------

リストでも繰り返せる

.. code-block:: python

    def return_list():
        return ["👩", "🐯", "🐟"]

.. doctestを通すための下準備
    >>> def return_list():
    ...     return ["👩", "🐯", "🐟"]

.. code-block:: python

    >>> for item in return_list():
    ...     print(item)
    ...
    👩
    🐯
    🐟

リストの場合と ``yield`` の比較
------------------------------------------------

* リストの場合は要素をすべてメモリに保持する（長くなると・・😢）
* ``yield`` は **すべてメモリに展開しない** 👈 tips!

  * リストのメモリ展開にかかる時間が ``yield`` ではかからない

例： ``yield`` でファイル読み込み
------------------------------------------------

.. code-block:: python

    def practical_generator(file_path):
        with open(file_path) as fh:
            for row in fh:
                yield row

例：長いファイル
------------------------------------------------

たくさんの行をもつファイル（``example.txt``）があります

.. code-block:: txt

    Kumiko
    Haduki
    Sapphire
    Reina
    :

.. doctestを通すための下準備
    >>> def practical_generator(file_path):
    ...     with open(file_path) as fh:
    ...         for row in fh:
    ...             yield row

例： ``yield`` でファイル読み込み
------------------------------------------------

.. code-block:: python

    >>> g = practical_generator("example.txt")
    >>> for member in g:
    ...     print(member.rstrip())  # 右側に付く \n を除く
    ...
    Kumiko
    Haduki

``yield`` について
============================================================

* ``yield`` とは
* ``yield`` よき
* ``yield`` こんなことまで 👈
* ``yield`` 別の使い方

別の再開方法
------------------------------------------------

* ``next(g)`` （``g.__next__()``）は、一時停止していた ``yield`` の後から再開
* ``g.send()`` で **値を送って、再開** させられる

  * ``yield`` は値を受け取れる（``value = yield "🐯"``）

値を受け取るようにジェネレータを変更
------------------------------------------------

.. code-block:: python

    def send_example_generator():
        value = "🐯"
        while True:
            value = yield value
            if not value:
                break
            else:
                value = "🐟"

.. doctestを通すための下準備
    >>> def send_example_generator():
    ...     value = "🐯"
    ...     while True:
    ...         value = yield value
    ...         if not value:
    ...             break
    ...         else:
    ...             value = "🐟"

``send`` メソッド
------------------------------------------------

.. code-block:: python

    >>> g = send_example_generator()
    >>> g.send(None)  # 開始するときはNoneを送る（next(g)でも開始）
    '🐯'

``value`` の初期値 🐯 が返った

``send`` メソッド
------------------------------------------------

.. code-block:: python

    >>> g.send(1)
    '🐟'

.. code-block:: python

    def send_example_generator():
        value = "🐯"
        while True:
            value = yield value  # valueに1が代入された
            if not value:
                break
            else:
                value = "🐟"

``send`` メソッド
------------------------------------------------

.. code-block:: python

    >>> g.send("hoge")
    '🐟'

.. code-block:: python

    def send_example_generator():
        value = "🐯"
        while True:
            value = yield value  # valueに"hoge"が代入された
            if not value:  # bool(value)がFalseならジェネレータ実行は終了
                break
            else:
                value = "🐟"

``send`` メソッド
------------------------------------------------

.. code-block:: python

    >>> bool([])
    False
    >>> g.send([])  # ジェネレータ実行を止める
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration

``yield`` について
============================================================

* ``yield`` とは
* ``yield`` よき
* ``yield`` こんなことまで
* ``yield`` 別の使い方 👈

ジェネレータを ``with`` と一緒に使える
------------------------------------------------

* ``contextlib.contextmanager`` デコレータをジェネレータに付ける（`ドキュメント <https://docs.python.org/ja/3/library/contextlib.html#contextlib.contextmanager>`_）
* tips: コンテキストマネージャ＝ ``with`` と一緒に使える（`用語集 <https://docs.python.org/ja/3/glossary.html#term-context-manager>`_）

コンテキストマネージャになったジェネレータ
------------------------------------------------

.. code-block:: python

    @contextlib.contextmanager
    def contextmanager_generator():
        # withのブロックに入る前の処理（__enter__）
        
        yield  # 値を返したときは as で受け取れる

        # withのブロックを抜けた直後の処理（__exit__）

コード例（『ゼロから作るDeep Learning③』`18章 <https://github.com/oreilly-japan/deep-learning-from-scratch-3/blob/master/steps/step18.py#L11>`_ より）
------------------------------------------------

``with`` の中でだけ、``Config`` の属性を書き換え

.. code-block:: python

    @contextlib.contextmanager
    def using_config(name, value):
        old_value = getattr(Config, name)
        setattr(Config, name, value)
        try:
            yield
        finally:
            setattr(Config, name, old_value)

まとめ： ``yield`` について
============================================================

* ``yield`` を使った関数＝ **ジェネレータ**
* **一時停止** & （値を送って） **再開**
* ジェネレータの返り値はジェネレータ *イテレータ*
* リストを使って繰り返す場合と比べると、全要素をメモリに展開しないため **省メモリ・省時間**

このLTで扱ったtips
------------------------------------------------

* Python界隈では **自己紹介のエイリアス** が「お前、誰よ」
* ``StopIteration`` 例外は繰り返しの仕組みに関係
* コンテキストマネージャ＝ ``with`` と一緒に使えるオブジェクト

ご清聴ありがとうございました
------------------------------------------------

よろしければ Appendix もどうぞ

``yield`` について
============================================================

TODO
