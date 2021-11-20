.. role:: raw-html(raw)
    :format: html

========================================================================================================================
文に立ち返って再入門するPython
========================================================================================================================

:Event: オープンソースカンファレンス2021 Fukuoka
:Presented: 2021/11/20 nikkie

Zoomのチャットでアンケート
============================================================

ふだんPython書いてますか？

- ガッツリ書いている
- 入門済み
- これから入門

最初にお願い
------------------------------------------------

* **顔出し** 推奨👨‍💼
* **質問・リアクション、お気軽に** どうぞ💬

  * Zoomのチャット中心に拾います

お前、誰よ（≒自己紹介）
============================================================

* Python大好き **にっきー** （:raw-html:`<i class="fab fa-twitter"></i>` `@ftnext <https://twitter.com/ftnext>`_ / :raw-html:`<i class="fab fa-github"></i>` `@ftnext <https://github.com/ftnext>`_）
* Python歴4年。株式会社ユーザベースのデータサイエンティスト（NLPer）
* アニメも大好き。『アイの歌声を聴かせて』はいいぞ！🤖🎤🎼

お前、誰よ
------------------------------------------------

* 10/15, 16開催の **Py** thon **Con** ference JP 2021の座長🇨🇭でした
* ＝PyCon JP 2021の開催に責任を持つ人

PyCon JP（曖昧さ回避）
============================================================

* PyCon JP Associationはイベント PyCon JP 20XXをその年の **座長に委託**
* 座長はスタッフを集めて、イベントを開催
* Associationにもスタッフがいます

PyCon JP AssociationとOSC
------------------------------------------------

* 2019 `Python言語最新情報 <https://github.com/pyconjp/slides/blob/master/osc2019fukuoka/osc2019fukuoka.pdf>`_

  * Pythonのアップデート情報の整理（例：Python 3.7~ dataclass）

* 2020 `Python開発環境の整え方 <https://github.com/pyconjp/slides/blob/master/osc2020fukuoka/osc2020fukuoka.pdf>`_

  * Pythonのインストール、venvなど

2021年のPyCon JP AssociationとOSC
------------------------------------------------

    PyCon JPのスタッフが様々なテーマで発表

https://pyconjp.blogspot.com/2021/03/pycamp-caravan-osc-online-spring-2021.html

PyCon JPスタッフによるOSCでの発表（リンク集） 1/3
------------------------------------------------------------------------------------------------

* `Online/Spring <https://event.ospn.jp/osc2021-online-spring/session/274261>`_

  * 「PyCon JPのスタッフ活動の中でこんなふうにPython使ってます」nikkie
  * 「Python(Dash/Cytoscape)を使ったNetwork Auto Visualization」稲森さん

PyCon JPスタッフによるOSCでの発表（リンク集） 2/3
------------------------------------------------------------------------------------------------

* `Nagoya <https://event.ospn.jp/osc2021-online-nagoya/session/312812>`_

  * 「本番運用を想定したDjango settings.pyの書き方入門」（筒井さん）（`Online/Fall <https://event.ospn.jp/osc2021-online-fall/session/405791>`_ でも）
  * 「あなたの街でもPython広めませんか？」（塚本さん）

PyCon JPスタッフによるOSCでの発表（リンク集） 3/3
------------------------------------------------------------------------------------------------

* `Hokkaido 「Pythonではじめる今風な型プログラミング」（Peacockさん） <https://event.ospn.jp/osc2021-online-do/session/316953>`_
* `Kyoto 「Playwright for PythonではじめるE2Eテスト」（Pep299さん） <https://event.ospn.jp/osc2021-online-kyoto/session/341018>`_
* `Hiroshima 「Batteries included ~ 調査、デバッグに役立つPythonの標準機能 ~」（陶山さん） <https://event.ospn.jp/osc2021-online-hiroshima/session/364728>`_

.. _Fukuoka: https://event.ospn.jp/osc2021-online-fukuoka/session/408197

`Fukuoka`_ （今回）
------------------------------------------------

* 「文に立ち返って再入門するPython」（nikkie）
* 「パッケージ管理ツール poetry が依存関係を解決するアルゴリズムについて」（村上さん）

.. include:: beginning.rst.txt

.. include:: execution.rst.txt

.. include:: expressions.rst.txt

.. include:: statements.rst.txt

.. include:: syntax.rst.txt

まとめ🌯：文に立ち返って再入門するPython 1/3
========================================================================================================================

* Pythonで書かれたファイル（プログラム）は、構文解析器でトークンとなり、パーザに入力される
* トークンレベルで、文について見てきた

まとめ🌯：文に立ち返って再入門するPython 2/3
------------------------------------------------

* Pythonという言語は **式と文** から構成される
* 文の構成要素は、式、または **キーワード** から構成されるもの
* 後者の文のうち、複合文について見てきた（例： ``if`` 文）

まとめ🌯：文に立ち返って再入門するPython 3/3
------------------------------------------------

* 複合文は **節** から構成される
* 節は **ヘッダとスイート** からなる（コロンやインデントの意味！）
* 複合文の定義はリファレンス中にあり、拡張したBNF記法で **簡潔に表されて** いる（``if`` 文をはじめとして読んでみた）

Why 文に立ち返って再入門するPython? に立ち戻ると
------------------------------------------------

* 入門者への説明をきっかけに、 **自分の文法理解を入門書より深めたく** て、言語リファレンスに潜った
* 今回の内容は入門者にはアウトプットできないので、OSCでアウトプット
* 言語リファレンスを読むのは楽しいし、もっと深いところへ潜りたい🤩（発表内容へのフィードバック歓迎です）

ご清聴ありがとうございました
------------------------------------------------

**Enjoy** development with Python!
