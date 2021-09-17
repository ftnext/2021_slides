.. role:: raw-html(raw)
    :format: html

========================================================================================================================
Helium - Cool Python!
========================================================================================================================

:Event: はんなりPython #43
:Presented: 2021/09/17 nikkie

このLTでは
============================================================

    ブラウザ操作自動化ライブラリHeliumを、 **書き方を工夫** 🆒して使ったことについて共有します

お前、誰よ
============================================================

* Python大好き **にっきー** （:raw-html:`<i class="fab fa-twitter"></i>` `@ftnext <https://twitter.com/ftnext>`_ / :raw-html:`<i class="fab fa-github"></i>` `@ftnext <https://github.com/ftnext>`_）
* Python歴もうじき4年。株式会社ユーザベースのデータサイエンティスト（NLPer）
* アニメも大好き。最近好きな挨拶「ういっす✌️」🐙

お前、誰よ：PyCon JP 2021 座長🇨🇭
============================================================

.. raw:: html

    <iframe width="640" height="480" src="https://2021.pycon.jp/" title="PyCon JP 2021 Webサイト"></iframe>

PyCon JP 2021（ **10/15(金), 16(土)** ）、チケット販売中！🎫🙏
------------------------------------------------------------------------------------------------

* https://pyconjp.connpass.com/event/221241/ （申込300名(60%)超え🎉）
* 早期購入特典🍕、まだ間に合う！🇲🇬

LT：Helium - Cool Python!
========================================================================================================================

まずは導入

先日のLT⚡️
------------------------------------------------------------------------------------------------

.. raw:: html

    <iframe width="800" height="480" src="https://ftnext.github.io/2021_slides/pycharity_Sep_lt/automate_connpass_with_helium.html#/1"
        title="週に数回connpassのイベントを作るPyCon JPスタッフは、Heliumを使って自動化しました（Python Charity Talks in Japan 2021.09 LT）"></iframe>

Helium
------------------------------------------------

* **ブラウザ操作自動化** ライブラリ
* Seleniumのラッパーで、 非常に簡単に書ける！💫（次へ⏬）
* :raw-html:`<i class="fab fa-github"></i>` https://github.com/mherrmann/selenium-python-helium (2650 star)

こんなに簡単です🍰
------------------------------------------------

.. code-block:: python
    :linenos:

    from helium import *
    start_chrome("google.com")  # 1. Chrome立ち上げ、「helium」についてGoogle検索
    write("helium selenium github")
    press(ENTER)
    click("mherrmann/helium")  # 検索結果の中からクリック
    go_to("github.com/login")  # 2. 別の例：GitHubにログイン
    write("username", into="Username")
    write("password", into="Password")
    click("Sign in")
    kill_browser()  # Chrome終了

https://github.com/mherrmann/selenium-python-helium/blob/master/docs/cheatsheet.md

PyCon JP スタッフでよくやる作業を自動化
------------------------------------------------

* 先日のLTでは、指定したconnpassイベントのコピー（デモしました）
* **今日デモします** ：connpassから参加者情報CSVのダウンロード

Heliumを使う中で感じた😖
========================================================================================================================

1. 繰り返し書くコードがある
2. スクリプトで例外が送出されたときにブラウザのウィンドウが残る

それぞれ、詳しい説明 👉 解決策 の順で話します

Heliumを使う中で感じた2点は解決済み🙌
------------------------------------------------

* **Pythonの知識** を使って解決。共有していきます
* 解決方法＝カッコいいPythonの書き方✨
* おことわり：ブラウザはFirefoxです（Chromeについても途中言及します）

.. include:: decorator.rst.txt

閑話休題：販売中はチケット🎫だけでなく
========================================================================================================================

https://pyconjp.connpass.com/event/221241/

.. raw:: html

    </section>
    <section >

.. raw:: html

    <blockquote class="twitter-tweet"><p lang="ja" dir="ltr">PyCon JP 2021 参加者Tシャツ発売!<br>PyCon JP 2021は、参加者向けTシャツはオンラインで購入できる形にしました!<br>9月28日（火）23:59まではお安く手に入れることが出来ます！<br>この機会に是非どうぞ。 <a href="https://twitter.com/hashtag/pyconjp?src=hash&amp;ref_src=twsrc%5Etfw">#pyconjp</a><a href="https://t.co/8UJwyF2J46">https://t.co/8UJwyF2J46</a><a href="https://t.co/Siq0xkSFtN">https://t.co/Siq0xkSFtN</a> <a href="https://t.co/QI9K4FGNAt">pic.twitter.com/QI9K4FGNAt</a></p>&mdash; PyCon JP (@pyconjapan) <a href="https://twitter.com/pyconjapan/status/1438115871973466114?ref_src=twsrc%5Etfw">September 15, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

.. include:: context_manager.rst.txt

まとめ🌯：Helium - Cool Python!
========================================================================================================================

PyCon JP 2021 チケットお願いします🐦🍕🙏
------------------------------------------------

https://pyconjp.connpass.com/event/221241/

🍕は **9/20（月・祝）まで** （まだ知らない方に教えてあげてください）

Heliumを使う中で感じた2点😖をカッコいいPythonの書き方で解決🙌
------------------------------------------------------------------------------------------------

1. 繰り返し書くコードがある 👉 **デコレータ** で繰り返し ``start_firefox`` を書かない
2. スクリプトで例外が送出されたときにブラウザのウィンドウが残る 👉 **コンテキストマネージャ** でどんなときも ``kill_browser``

ご清聴ありがとうございました
------------------------------------------------

紹介したデコレータやコンテキストマネージャはヘルパーとしてPyPIで公開予定です

References & Appendixが続きます（よろしければどうぞ！）

References
========================================================================================================================

* 説明できなかった ``wraps``
* コンテキストマネージャ
* デコレータの最終形

説明できなかった ``wraps``
------------------------------------------------

.. raw:: html

    <iframe width="800" height="480" src="https://ftnext.github.io/2021_slides/rakus_Aug_pythontips/about_decorators.html"
        title="デコレータについて（ラクス Python Tips LT会 vol.2 (2021/08)）"></iframe>

コンテキストマネージャ
------------------------------------------------

.. raw:: html

    <iframe width="800" height="480" src="https://ftnext.github.io/2021_slides/rakus_Feb_pythontips/about_yield.html"
        title="yield について（ラクス Python Tips LT会 (2021/02)）"></iframe>

デコレータの最終形
------------------------------------------------

.. raw:: html

    <iframe width="800" height="480" src="https://ftnext.github.io/2021_slides/pysuruga_Aug/decorator_like_dataclass.html#/1"
        title="@dataclass のような、 () を付けても付けなくてもいいデコレータはどう作る？（Python駿河 勉強会 #28 (2021/08)）"></iframe>

Appendix：loginもデコレータにする
========================================================================================================================

* PyCon JP スタッフのconnpass操作自動化をいくつも書いて
* connpassにログインするコードを繰り返す

connpassにログインするコード
------------------------------------------------

.. code-block:: python
    :linenos:

    go_to("connpass.com/login")
    write(os.getenv("CONNPASS_USERNAME"), into="ユーザー名")
    write(os.getenv("CONNPASS_PASSWORD"), into="パスワード")
    click("ログインする")

    wait_until(Text("あなたのイベント").exists)

ログインするコードをデコレータに
------------------------------------------------

.. code-block:: python
    :linenos:

    def logged_in(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            go_to("connpass.com/login")
            write(os.getenv("CONNPASS_USERNAME"), into="ユーザー名")
            write(os.getenv("CONNPASS_PASSWORD"), into="パスワード")
            click("ログインする")

            wait_until(Text("あなたのイベント").exists)
            
            func(*args, **kwargs)

        return wrapper

📣 2つのデコレータは以下の順
------------------------------------------------

.. code-block:: python
    :linenos:

    @using_firefox
    @logged_in
    def automate():
        # connpassにログインが必要な退屈なブラウザ操作を代わりにやってくれる処理

2つのデコレータの実行順は **外側から**
------------------------------------------------

1. ``logged_in`` で ``automate`` の実行前後にコードを追加
2. ``logged_in`` が返した関数の実行前後に ``using_firefox`` でコードを追加

これにより、 ``start_firefox`` が **一番最初に呼ばれる**

EOF
============================================================
