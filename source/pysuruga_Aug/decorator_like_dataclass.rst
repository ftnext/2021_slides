.. role:: raw-html(raw)
    :format: html

========================================================================================================================
``@dataclass`` のような、 ``()`` を付けても付けなくてもいいデコレータはどう作る?
========================================================================================================================

:Event: Python駿河 勉強会 #28
:Presented: 2021/08/28 nikkie

11月 #pycon_shizu 開催🎉 楽しみですね
============================================================

.. raw:: html

    <blockquote class="twitter-tweet"><p lang="ja" dir="ltr">お久しぶりです。実行委員会です。<br>今年も PyCon mini Shizuoka 2021を開催することが決定しました🎉<br>開催日は 2021/11/20（土）です。</p>&mdash; PyCon Mini Shizuoka (@PyconShizu) <a href="https://twitter.com/PyconShizu/status/1430168021436231680?ref_src=twsrc%5Etfw">August 24, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

お前、誰よ
------------------------------------------------

* Python大好き **にっきー** （:raw-html:`<i class="fab fa-twitter"></i>` `@ftnext <https://twitter.com/ftnext>`_ / :raw-html:`<i class="fab fa-github"></i>` `@ftnext <https://github.com/ftnext>`_）
* Python歴3年半。株式会社ユーザベースのデータサイエンティスト（NLPer）
* アニメも大好き（🌟💫🐙💫🌟　🌲🌳🐲　2️⃣0️⃣0️⃣6️⃣♻️）

お前、誰よ：PyCon JP 2021 座長🇨🇭
------------------------------------------------

.. raw:: html

    <iframe width="640" height="480" src="https://2021.pycon.jp/" title="PyCon JP 2021 Webサイト"></iframe>

PyCon JP 2021、チケット発売開始です！🎫🙏
------------------------------------------------

https://pyconjp.connpass.com/event/221241/

LT本題： ``@dataclass`` のような、 ``()`` を付けても付けなくてもいいデコレータを作りたい
========================================================================================================================

`ドキュメント <https://docs.python.org/ja/3/library/dataclasses.html#dataclasses.dataclass>`_ より、以下の3つは同等
------------------------------------------------------------------------------------------------------------------------------------------------

.. code-block:: python

    @dataclass  # ()を付けない
    class C:
        ...

    @dataclass()  # ()を付ける
    class C:
        ...

    # 引数をデフォルト値で指定
    @dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)
    class C:
        ...

``@dataclass`` のようなデコレータの要件
------------------------------------------------

1. ``@decorator`` と ``@decorator()`` が **同じ**
2. その上で、 **引数も渡せる**

そもそもデコレータとは
============================================================

    別の関数を返す関数で、通常、 @wrapper 構文で関数変換として適用されます（ `用語集 <https://docs.python.org/ja/3/glossary.html#term-decorator>`_ より）

デコレータで関数呼び出しの前後に **追加コード** を実行できる

🚨 デコレータは関数とクラスに付けられる
------------------------------------------------

* 今回 ``()`` を付けても付けなくてもいいデコレータを作りたかった
* そのデコレータは **関数** をデコレートするのに使う
* 実装する上で、知っている範囲から ``@dataclass`` を参考にした

デコレータの書き換え（イメージ）
------------------------------------------------

``@dataclass`` の3つの例について、 *だいたい等価* な書き方（ `参考 <https://docs.python.org/ja/3/reference/compound_stmts.html#class>`_ ）

.. code-block:: python
    :emphasize-lines: 1,5,9

    @dataclass  # C = dataclass(C)
    class C:
        ...

    @dataclass()  # C = dataclass()(C)
    class C:
        ...

    # C = dataclass(init=True, ..., frozen=False)(C)
    @dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)
    class C:
        ...

``@dataclass`` はどう実現している？🔍
============================================================

* CPythonの実装を見てみます（v3.9.6 :raw-html:`<i class="fab fa-github"></i>` `Lib/dataclasses.py <https://github.com/python/cpython/blob/db3ff76da19004f266b62e98a81bdfd322861436/Lib/dataclasses.py#L998>`_ ）

.. code-block:: python
    :linenos:

    def dataclass(cls=None, /, *, init=True, repr=True, eq=True, order=False,
                  unsafe_hash=False, frozen=False):
        
        def wrap(cls):
            return _process_class(cls, init, repr, eq, order, unsafe_hash, frozen)
        
        if cls is None:
            return wrap
        
        return wrap(cls)

:file:`Lib/dataclasses.py` の ``@dataclass`` の実装 1/4
------------------------------------------------------------------------------------------------

.. code-block:: python
    :linenos:
    :emphasize-lines: 2

    # 引数に **デフォルト値** が設定されている
    def dataclass(cls=None, /, *, init=True, repr=True, eq=True, order=False,
                  unsafe_hash=False, frozen=False):
        
        def wrap(cls):
            return _process_class(cls, init, repr, eq, order, unsafe_hash, frozen)
        
        if cls is None:
            return wrap
        
        return wrap(cls)

:file:`Lib/dataclasses.py` の ``@dataclass`` の実装 2/4
------------------------------------------------------------------------------------------------

.. code-block:: python
    :linenos:
    :emphasize-lines: 7

    def dataclass(cls=None, /, *, init=True, repr=True, eq=True, order=False,
                  unsafe_hash=False, frozen=False):
        
        def wrap(cls):
            # クロージャ：外側のスコープ(dataclass)の変数initなどを参照。
            # 外側のスコープ(dataclass)の変数はデコレータの呼び出しで設定される
            return _process_class(cls, init, repr, eq, order, unsafe_hash, frozen)
        
        if cls is None:
            return wrap
        
        return wrap(cls)

:file:`Lib/dataclasses.py` の ``@dataclass`` の実装 3/4
------------------------------------------------------------------------------------------------

.. code-block:: python
    :linenos:
    :emphasize-lines: 8

    def dataclass(cls=None, /, *, init=True, repr=True, eq=True, order=False,
                  unsafe_hash=False, frozen=False):
        
        def wrap(cls):
            return _process_class(cls, init, repr, eq, order, unsafe_hash, frozen)
        
        # @dataclass() や @dataclass(frozen=True) では cls is None
        if cls is None:
            # C = dataclass()(C) 👉 C = wrap(C)
            return wrap
        
        return wrap(cls)

:file:`Lib/dataclasses.py` の ``@dataclass`` の実装 4/4
------------------------------------------------------------------------------------------------

.. code-block:: python
    :linenos:
    :emphasize-lines: 12

    def dataclass(cls=None, /, *, init=True, repr=True, eq=True, order=False,
                  unsafe_hash=False, frozen=False):
        
        def wrap(cls):
            return _process_class(cls, init, repr, eq, order, unsafe_hash, frozen)
        
        if cls is None:
            return wrap
        
        # @dataclass では cls は、デコレータに続いて定義されるクラスを指す
        # C = dataclass(C) 👉 C = wrap(C) となっている
        return wrap(cls)

``@dataclass`` を参考に実装したデコレータ ``@using_firefox``
============================================================

:raw-html:`<i class="fab fa-github"></i>` `copy_existing_event.py <https://github.com/ftnext/connpass-ops-playbook/blob/fed230ef2efbd5b1c0bf03ec18da27403f75f960/examples/copy_existing_event.py>`_

.. code-block:: python
    :linenos:
    :emphasize-lines: 1

    @using_firefox
    @logged_in
    def show_copy_popup(url):
        copy_existing_event(url, human_confirms=True)

`Helium <https://github.com/mherrmann/selenium-python-helium>`_！
------------------------------------------------------------------------------------------------

* **ブラウザ操作** ライブラリ（2600 star）
* Seleniumのラッパーで、 **非常に簡単** に書ける！💫
* 詳しくは `9/11(土) #pycharity <https://pyconjp.connpass.com/event/218154/>`_ のLTで共有します

``@using_firefox``
------------------------------------------------

* ブラウザ（Firefox）を起動する処理 ``helium.start_firefox`` は必ず呼ぶ
* デコレータで実装して、関数呼び出しの前に必ず追加できる！🤩
* さらに ``@using_chrome`` でデコレータを変えたら起動するブラウザも変わる実装🆒

``@using_firefox(options=...)``
------------------------------------------------

* ``helium.start_firefox`` に ``selenium.webdriver.FirefoxOptions`` を渡したい

  * 例：ダウンロードのポップアップを出さないようにFirefoxを設定する

* 1つのデコレータ ``@using_firefox`` で実現したく今回取り組んだ

``@using_firefox(options=...)`` の例
------------------------------------------------

:raw-html:`<i class="fab fa-github"></i>` `download_participants_csv.py <https://github.com/ftnext/connpass-ops-playbook/blob/fed230ef2efbd5b1c0bf03ec18da27403f75f960/examples/download_participants_csv.py>`_

.. code-block:: python
    :linenos:
    :emphasize-lines: 1

    @using_firefox(options=options)
    @logged_in
    def download(url):
        download_latest_participants_csv(url)

``@dataclass`` にならって実装
------------------------------------------------

.. code-block:: python
    :linenos:
    :emphasize-lines: 5

    def using_firefox(func=None, /, *, options=None):
        def middle(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                start_firefox(options=options)  # 関数呼び出し前に追加したかった！
                func(*args, **kwargs)

            return wrapper

        if func is None:
            return middle

        return middle(func)

``@using_firefox()`` でデコレートしたとき（ ``()`` を付けて）
------------------------------------------------------------------------------------------------

.. code-block:: python
    :linenos:
    :emphasize-lines: 4

    def using_firefox(func=None, /, *, options=None):
        # middle の定義は省略

        if func is None:
            # f = using_firefox()(f) 👉 f = middle(f)
            return middle

        return middle(func)

``@using_firefox`` でデコレートしたとき（ ``()`` を付けないで）
------------------------------------------------------------------------------------------------

.. code-block:: python
    :linenos:
    :emphasize-lines: 8

    def using_firefox(func=None, /, *, options=None):
        # middle の定義は省略

        if func is None:
            return middle
        
        # f = using_firefox(f) 👉 f = middle(f)
        return middle(func)

まとめ🌯： ``@dataclass`` のような、 ``()`` を付けても付けなくてもいいデコレータはどう作る?
========================================================================================================================

PyCon JP 2021 チケットお願いします🐦🍕🙏
------------------------------------------------

https://pyconjp.connpass.com/event/221241/

``()`` を付けても付けなくてもいいデコレータの作り方
------------------------------------------------------------------------------------------------

* 第1引数 ``func`` / ``cls`` の **デフォルト値** を ``None`` にする
* ``func`` / ``cls`` の値で **分岐**

``()`` を付けても付けなくてもいいデコレータの作り方（承前）
------------------------------------------------------------------------------------------------

* ``func`` / ``cls`` の値で分岐

  * ``None`` なら、クラス/関数を引数に受け取る **関数** を返す（ ``()`` 付きに対応）
  * ``None`` でないなら、クラス/関数を引数に受け取る関数に ``func`` / ``cls`` を渡した **返り値** を返す（ ``()`` なしに対応）

クラス/関数を引数に受け取る関数
------------------------------------------------

* 実装には **クロージャ** を利用
* この関数の中で、 **デコレータの引数を参照** して実装する
* クロージャ： *functions that refer to variables from the scope in which they were defined* （『Effective Python second edition』Item 21 p.84）

ご清聴ありがとうございました
------------------------------------------------

**Enjoy** development with decorators!

References、 **Appendix** が続きます（よろしければどうぞ！）

References：直近のデコレータ関連アウトプット⚡️
============================================================

.. raw:: html

    <iframe width="800" height="480" src="https://ftnext.github.io/2021_slides/rakus_Aug_pythontips/about_decorators.html" title="デコレータについて（ラクス Python tips LT）"></iframe>

Appendix
============================================================

* 位置専用・キーワード専用引数
* ``@dataclass`` ようなデコレータの別の例
* ``print`` を仕込んで ``decorator()(f)`` 呼び出し順を確認

位置専用・キーワード専用引数
============================================================

* ``def using_firefox(func=None, /, *, options=None):``
* ``options`` は ``options=...`` と指定する必要がある（位置引数として指定できない 🙅‍♂️ ``using_firefox(func, options)``）
* ``func`` は位置専用引数（🙅‍♂️ ``using_firefox(func=f)``）

位置専用引数 in Pythonチュートリアル
------------------------------------------------

    *位置専用* の場合、引数の順序が重要であり、キーワードで引数を渡せません。 位置専用引数は ``/`` （スラッシュ）の前に配置されます。

https://docs.python.org/ja/3/tutorial/controlflow.html#positional-only-parameters

キーワード専用引数 in Pythonチュートリアル
------------------------------------------------

    引数をキーワード引数で渡す必要があることを示す *キーワード専用* として引数をマークするには、引数リストの最初の *キーワード専用* 引数の直前に ``*`` を配置します。

https://docs.python.org/ja/3/tutorial/controlflow.html#keyword-only-arguments

別の例
============================================================

.. literalinclude:: ../../samplecode/decorators/with_parenthesis_or_not_decorators.py
    :language: python
    :pyobject: once_per_minutes
    :linenos:

別の例のコンテキスト
------------------------------------------------

* 引数を取るデコレータの例：呼び出しはN分に1回（詳しくはReferencesのスライドをどうぞ）
* 今回の内容をもとに、 **引数を取らない使い方もできる** ように拡張した

別の例を実行
------------------------------------------------

.. doctest を通す（デコレータは除いた実装）
    >>> def calculate_bmi(height_m, weight_kg):
    ...     return weight_kg / height_m / height_m
    >>> calculate_bmi1 = calculate_bmi2 = calculate_bmi3 = calculate_bmi

実行環境 Python 3.9.4

.. code-block:: python

    >>> calculate_bmi1(1.58, 46)
    18.426534209261334
    >>> # calculate_bmi1(1.58, 46)  # Raise RunTooOftenError
    >>> calculate_bmi2(1.58, 46)
    18.426534209261334
    >>> # calculate_bmi2(1.58, 46)  # Raise RunTooOftenError
    >>> calculate_bmi3(1.58, 46)
    18.426534209261334
    >>> calculate_bmi3(1.58, 46)
    18.426534209261334

``print`` を仕込んで ``decorator()(f)`` 呼び出し順を確認
============================================================

.. literalinclude:: ../../samplecode/decorators/parenthesis_experiment.py
    :language: python
    :pyobject: decorator
    :linenos:

(1) ``()`` なしでデコレート
------------------------------------------------

.. code-block:: python

    >>> @decorator  # doctest: +SKIP
    ... def f1(): ...
    ...
    decorator start: func=<function f1 at 0x1092a9a60> n=1  # funcにf1が渡っている
    decorator end
    middle start  # middle(func) を返したことによる実行
    middle end

(2) ``()`` を付け、デフォルト値でデコレート
------------------------------------------------

.. code-block:: python

    >>> @decorator()  # doctest: +SKIP
    ... def f2(): ...
    ...
    decorator start: func=None n=1
    decorator end
    middle start  # f2 = middle(f2) 部分
    middle end

寄り道： ``middle`` が返っている 1/2
------------------------------------------------

.. code-block:: python

    >>> decorator()  # doctest: +SKIP
    decorator start: func=None n=1
    decorator end
    <function decorator.<locals>.middle at 0x1092ba280>  # decorator() の返り値

寄り道： ``middle`` が返っている 2/2
------------------------------------------------

.. code-block:: python

    >>> def f(): ...
    ...
    >>> decorator()(f)  # doctest: +SKIP
    decorator start: func=None n=1
    decorator end
    middle start
    middle end
    <function decorator.<locals>.middle.<locals>.wrapper at 0x1092ba430>
    >>> f2  # decorator()(f) と同様に wrapper  # doctest: +SKIP
    <function decorator.<locals>.middle.<locals>.wrapper at 0x1092ba550>

(3) ``()`` を付け、値も指定してデコレート
------------------------------------------------

.. code-block:: python

    >>> @decorator(n=3)  # doctest: +SKIP
    ... def f3(): ...
    ...
    decorator start: func=None n=3  # nは渡した値
    decorator end
    middle start
    middle end

``print`` で確認した呼び出し順
============================================================

* (1)~(3)の3例とも **出力されるメッセージは同様**
* つまり ``()`` の有無によらず、関数がデコレートされている
* 分岐の実装により ``()`` の有無によらず、関数がデコレートされる

EOF
============================================================
