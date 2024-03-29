.. role:: raw-html(raw)
    :format: html

============================================================
デコレータについて
============================================================

:Event: ラクス Python Tips LT会 vol.2
:Presented: 2021/08/05 nikkie

❓ Question（チャットお願いします🙏）
============================================================

ふだん **デコレータ** 使ってますか？

- ガッツリ💪
- たまに😃
- 初耳！👂

お前、誰よ
============================================================

* Python大好き **にっきー** （:raw-html:`<i class="fab fa-twitter"></i>` `@ftnext <https://twitter.com/ftnext>`_ / :raw-html:`<i class="fab fa-github"></i>` `@ftnext <https://github.com/ftnext>`_）
* Python歴3年半。データサイエンティストにしてNLPer
* *Py* thon *Con* ference JP 2021 座長🇨🇭
* **tips**: Python界隈では *自己紹介のエイリアス* が「お前、誰よ」（`ルーツ <https://www.ianlewis.org/jp/pycon-mini-jp>`_）

お前、誰よ（承前）
------------------------------------------------

.. raw:: html

    <blockquote class="twitter-tweet"><p lang="ja" dir="ltr">我が名はにっきー。アニメ大好き🥰この夏はアニメ映画がアツい！！<br>竜とそばかすの姫🐉、サイダーのように言葉が湧き上がる🥤、映画大好きポンポさん🎦、かくしごと👩‍🎨、きんモザ and so on！<br>しかしここ数日都内は感染者数3000人突破。外出しづらい。めっちゃ見たい！けどリスクとるか悩む。ぐおおお🤨</p>&mdash; nikkie 📣PyCon JP 2021 スタッフ募集中！ (@ftnext) <a href="https://twitter.com/ftnext/status/1421319212081942528?ref_src=twsrc%5Etfw">July 31, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

今回のテーマは「デコレータ」
============================================================

デコレータ
------------------------------------------------

* 語弊を恐れずに言えば、 **関数を返す関数**
* 「関数が関数を返すってどういうこと？」🤨
* 👉 関数の基本から見ていきましょう

お品書き：デコレータについて
------------------------------------------------

* Pythonの関数
* デコレータ
* より便利なデコレータを書くために

お品書き：デコレータについて
------------------------------------------------

* **Pythonの関数**
* デコレータ
* より便利なデコレータを書くために

.. include:: python_functions.rst.txt

.. include:: decorators.rst.txt

.. include:: more_decorators.rst.txt

🌯まとめ：デコレータについて
============================================================

* デコレータ＝関数を返す関数。 **処理を追加** できる
* 実装の鍵は、クロージャ・ ``*args, **kwargs`` ・ ``functools.wraps``
* ``nonlocal`` や引数を取るデコレータでより高機能に！

ご清聴ありがとうございました
------------------------------------------------

**Enjoy** development with decorators!

References、**Appendix** が続きます（よろしければどうぞ！）

References 1/2
============================================================

* 『`Effective Python 第2版 <https://www.oreilly.co.jp/books/9784873119175/>`_』3章関数（特に以下）

  * 項目21 クロージャが変数スコープとどう関わるかを把握しておく
  * 項目22 可変長位置引数を使って、見た目をすっきりさせる
  * 項目26 functools.wrapsを使って関数デコレータを定義する

References 2/2
------------------------------------------------

* The Global Dev Study #4 - FastAPI / Python

  * `YouTube <https://youtu.be/Ly3ZUDqAsL8>`_
  * `Source code <https://github.com/reuven/Forkwell-2021-July-6>`_

* PyCon JP 2020 「`詳解デコレータ <https://pycon.jp/2020/timetable/?id=203944>`_」

Appendix 作成中
============================================================

EOF
============================================================
