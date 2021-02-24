============================================================
``yield`` について
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

* 我が名は「にっきー」（Twitter `@ftnext <https://twitter.com/ftnext>`_ / GitHub `@ftnext <https://github.com/ftnext>`_）
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
* ``yield`` 別の使い方（Appendix）

``yield`` の簡単な例
------------------------------------------------

.. code-block:: python
    :linenos:

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

組み込み関数 ``next`` で次の要素を取得
------------------------------------------------

* ``next`` は、*イテレータ* の ``__next__()`` メソッドを呼び出し、次の要素を取得（`ドキュメント <https://docs.python.org/ja/3/library/functions.html#next>`_）

.. code-block:: python

    >>> next(g)  # ジェネレータイテレータの次の要素
    '👩'

``yield`` で一時停止
------------------------------------------------

``next(g)`` で 1行目の ``yield`` で値が返され、**一時停止**

.. code-block:: python
    :linenos:
    :emphasize-lines: 2

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
    :linenos:
    :emphasize-lines: 3

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
    :linenos:
    :emphasize-lines: 4

    def easy_generator():
        yield "👩"
        yield "🐯"
        yield "🐟"  # 👈

次がない時：``StopIteration`` 例外（`ドキュメント <https://docs.python.org/ja/3/library/exceptions.html#StopIteration>`_）
------------------------------------------------

.. code-block:: python

    >>> next(g)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration

ジェネレータイテレータは ``for`` 文で繰り返せる
------------------------------------------------

ジェネレータ **イテレータ**

.. code-block:: python

    >>> for item in easy_generator():
    ...     print(item)
    ...
    👩
    🐯
    🐟

tips: ``StopIteration`` 例外は繰り返しの仕組みに関係（`PyCon JP 2017 トーク <https://www.slideshare.net/shimizukawa/how-does-python-get-the-length-with-the-len-function>`_）

``yield`` について
============================================================

* ``yield`` とは
* ``yield`` よき 👈
* ``yield`` こんなことまで
* ``yield`` 別の使い方（Appendix）

``yield`` 何がいいの？
------------------------------------------------

リストも ``for`` 文で繰り返せる

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

リストの場合と ``yield`` の比較（Appendixで実験）
------------------------------------------------

* リストの場合はすべての要素をメモリに保持する

  * 長くないリストならいいのですが、長くなると・・😢

* ``yield`` は **すべてメモリに展開しない** 👈 tips!

  * 一時停止により、**一度に1つの要素** を処理
  * リストで全要素をメモリに保持するのにかかる時間が ``yield`` では発生しない

例：``yield`` でファイル読み込み
------------------------------------------------

.. code-block:: python
    :linenos:

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

例：``yield`` でファイル読み込み
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
* ``yield`` 別の使い方（Appendix）

別の再開方法
------------------------------------------------

* ``next(g)`` （``g.__next__()``）は、一時停止していた ``yield`` の後から再開
* ``g.send()`` で **値を送って、再開** させられる

  * ``yield`` は送られた値を受け取れる（``value = yield "🐯"``）

値を受け取るようにジェネレータを変更
------------------------------------------------

.. code-block:: python
    :linenos:

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
    :linenos:
    :emphasize-lines: 4

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

    >>> g.send("False")
    '🐟'

.. code-block:: python
    :linenos:
    :emphasize-lines: 4

    def send_example_generator():
        value = "🐯"
        while True:
            value = yield value  # valueに"False"が代入された
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

まとめ：``yield`` について
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

**Enjoy** development with ``yield``!

References、**Appendix** が続きます（よろしければどうぞ！）

References 1/2 ジェネレータ関連
============================================================

* 自身を持ってコードを書こう by 陶山さん（`2020/07 Python Charity Talks <https://pyconjp.connpass.com/event/177586/>`_）

  * `スライド（45枚目） <https://docs.google.com/presentation/d/1qu3zFbzMh3AYhQ3DuDCDKbLlLqIrcklZdzi9fKyZPZQ/edit#slide=id.g7eca55c2c3_0_73>`_ ・ `YouTube <https://youtu.be/o-UBokTvQjE?t=1196>`_

* Generators, coroutines, and nanoservices by Reuven M. Lerner (PyCon Africa 2020)

  * `YouTube <https://youtu.be/tkoaeVS2zRQ>`_ ・ `Blogバージョン <https://lerner.co.il/2020/05/08/making-sense-of-generators-coroutines-and-yield-from-in-python/>`_

* `When to Use a List Comprehension in Python (Choose Generators for Large Datasets) <https://realpython.com/list-comprehension-python/#choose-generators-for-large-datasets>`_
* `PEP 255 -- Simple Generators <https://www.python.org/dev/peps/pep-0255/>`_

References 2/2
------------------------------------------------

* The Enters and Exits of Context Managers by Mason Egger（`2021/02 ChiPy <https://www.meetup.com/ja-JP/_ChiPy_/events/276239528/>`_）

  * `YouTube <https://youtu.be/vQlekAHqpBg?t=2686>`_ ・ `ソースコード <https://github.com/MasonEgger/context-managers-sample-code/blob/main/example08.py>`_

* Pythonはどうやってlen関数で長さを手にいれているの？ by 清水川さん（PyCon JP 2017）

  * `スライド <https://www.slideshare.net/shimizukawa/how-does-python-get-the-length-with-the-len-function>`_ （33枚目から ``for`` の仕組み）・`YouTube <https://youtu.be/aich6wqftkA>`_

Appendix：``yield`` について
============================================================

* ``yield`` 別の使い方（本編に入り切らなかった話題）
* ``yield`` のtips
* 大量の行のファイルを扱う実験

番外編：``yield`` について
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

コード例（『ゼロから作るDeep Learning③』より）
------------------------------------------------

``with`` の中でだけ、``Config`` の属性を書き換え（`18章 <https://github.com/oreilly-japan/deep-learning-from-scratch-3/blob/master/steps/step18.py#L11>`_）

.. code-block:: python
    :linenos:

    @contextlib.contextmanager
    def using_config(name, value):
        old_value = getattr(Config, name)
        setattr(Config, name, value)
        try:
            yield
        finally:
            setattr(Config, name, old_value)

``yield`` のtips
============================================================

* ``yield from <イテレータ>``
* ref: `PEP 380 <https://www.python.org/dev/peps/pep-0380/>`_ Python 3.3〜
* ファイル読み込みの例を次で書き変えます

``yield`` でファイル読み込みの例を書き換え
------------------------------------------------

.. code-block:: python
    :linenos:
    :emphasize-lines: 5

    def practical_generator(file_path):
        with open(file_path) as fh:
            # for row in fh:
            #     yield row
            yield from fh

大量の行のファイルを扱う実験：リストと ``yield``
============================================================

10行を繰り返して行の数が多いファイルを用意

.. code-block:: bash

    $ wc -l many_names_1b.txt  # 10億行！（6.4GB）
     1000000000 many_names_1b.txt

実験環境
------------------------------------------------

* MacBook Pro
* プロセサ 2.3 GHz Intel Core i5、4コア
* メモリ 16GB
* Python 3.9.0

リストを使った場合
------------------------------------------------

.. code-block:: bash

    $ time python compare_speed.py

    real	21m47.461s
    user	5m50.540s
    sys	10m31.005s

``yield`` を使った場合
------------------------------------------------

.. code-block:: bash

    $ time python compare_speed.py

    real	3m42.741s
    user	3m40.157s
    sys	0m2.286s

``time`` コマンドの結果の見方
------------------------------------------------

* user：プログラム自体の処理時間
* sys：プログラムを処理するために、OSが処理をした時間
* ref: https://qiita.com/tossh/items/659e5934e52b38183200

考察
------------------------------------------------

* userを比べると、リストのほうが長い -> 全ての要素を保持する処理の時間と考えられる
* sysを比べると、大きな差 -> プログラム処理で巨大なリストを扱うためにOSの処理が必要になったと考えている

大量の行のファイルの読み込み、``yield`` を試してみては？

EOF
============================================================
