.. role:: raw-html(raw)
    :format: html

============================================================
the app runner Streamlit Season✨
============================================================

:Event: みんなのPython勉強会 #72
:Presented: 2021/08/11🎋 nikkie

❓ Question（Slidoへ🙏）
============================================================

https://bit.ly/stapy72question

.. figure:: ../_static/stapy_Aug_app_runner/202108_stapy_slido_qrcode.png
    :width: 50%

❓ Question：Streamlitを
------------------------------------------------

* 初めて聞いた
* 聞いたことある
* 触ったことある
* 使っている

このトーク：the app runner Streamlit Season✨
------------------------------------------------

* Streamlit初めて聞いた方向け
* デモ & ハンズオンでStreamlitを **体験**
* 目標：Streamlitの概要を掴む

話すこと
------------------------------------------------

* Streamlitの特徴3点（3つの原則として紹介）
* おまけ：Streamlitの限界

話さないこと
------------------------------------------------

* 網羅的な説明はしません
* 代わりに、網羅している学習リソースを紹介します

一緒に体験するために ``pip install streamlit`` お願いします！
------------------------------------------------------------------------------------------------

環境構築は **自身の慣れた方法で** 行ってください（ ``pipenv`` など）

お前の環境、どうなってんのよ
------------------------------------------------------------------------------------------------

* Python 3.8.6

  * Requires: Python >=3.6 なので 3.9 でも動作するかも（未検証）

* Streamlit, version 0.86.0

  * 2021/08/06 リリース版🚀

お前、誰よ
============================================================

* Python大好き **にっきー** （:raw-html:`<i class="fab fa-twitter"></i>` `@ftnext <https://twitter.com/ftnext>`_ / :raw-html:`<i class="fab fa-github"></i>` `@ftnext <https://github.com/ftnext>`_）
* Python歴3年半
* 仕事で楽しく書いています（データサイエンティストにしてNLPer）

お前、誰よ（承前）
------------------------------------------------

* みんなのPython勉強会4代目LT王子🤴・スタッフ
* PyCon JP 2021 座長🇨🇭

お前、誰よ（趣味）
------------------------------------------------

.. raw:: html

    <blockquote class="twitter-tweet"><p lang="ja" dir="ltr">我が名はにっきー。アニメ大好き🥰この夏はアニメ映画がアツい！！<br>竜とそばかすの姫🐉、サイダーのように言葉が湧き上がる🥤、映画大好きポンポさん🎦、かくしごと👩‍🎨、きんモザ and so on！<br>しかしここ数日都内は感染者数3000人突破。外出しづらい。めっちゃ見たい！けどリスクとるか悩む。ぐおおお🤨</p>&mdash; nikkie 📣PyCon JP 2021 スタッフ募集中！ (@ftnext) <a href="https://twitter.com/ftnext/status/1421319212081942528?ref_src=twsrc%5Etfw">July 31, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

TODO Question：Streamlitを の確認！
------------------------------------------------

みなさん、進捗どうですか？ ``pip install streamlit``
------------------------------------------------------------------------------------------------

❓ Question（再度Slidoへ🙏）
============================================================

https://bit.ly/stapy72question

.. figure:: ../_static/stapy_Aug_app_runner/202108_stapy_slido_qrcode.png
    :width: 50%

❓ Question：PyCon JP 2021に
------------------------------------------------

* 参加予定
* しないかな
* ってなんすか？

PyCon JPって、何よ
------------------------------------------------

* *Py* thon *Con* ference JP
* 日本最大のPython祭り

PyCon JP 2021 10/15(金)・16(土)開催
------------------------------------------------

https://2021.pycon.jp/

.. raw:: html

    <iframe width="640" height="480" src="https://2021.pycon.jp/" title="PyCon JP 2021 Webサイト"></iframe>

PyCon JP 2021 10/15(金)・16(土)開催
------------------------------------------------

* 座長が `6月末時点の全てをお話し <https://pyconjp.blogspot.com/2021/07/hybrid-pyconjp-2021-plan-june.html>`_ 済み
* 8/9にプロポーザルを採択（ `採択速報 <https://pyconjp.blogspot.com/2021/08/pyconjp-2021-proposal-selection.html>`_）
* `スポンサー1ヶ月前まで募集中 <https://pyconjp.blogspot.com/2021/05/pycon-jp-2021_01988973482.html>`_ ！ `スタッフも <https://pyconjp.blogspot.com/2021/01/2021-staff-application-start.html>`_

TODO Question：PyCon JP 2021に の確認！
------------------------------------------------

Python学び始めでも、うどんと海ー苔ー（Don't worry）
------------------------------------------------------------------------------------------------

Djangoのカンファレンス（7月開催）公式さんの言

.. raw:: html

    <blockquote class="twitter-tweet"><p lang="ja" dir="ltr">まったく問題ありませんよ！トークの内容も幅広いので。もし当日「内容難しいかな」と感じられた場合も「こういうことができるんだ」とキーワードだけお持ち帰りいただければ十分と思います。</p>&mdash; django-ja (@django_ja) <a href="https://twitter.com/django_ja/status/1397830929024905216?ref_src=twsrc%5Etfw">May 27, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 

完了しましたか？ ``pip install streamlit``
------------------------------------------------

.. include:: introduction/whats_streamlit.rst.txt

.. include:: introduction/demo_app.rst.txt

.. include:: principles/getting_started.rst.txt

.. include:: principles/interaction.rst.txt

.. include:: principles/cache.rst.txt

.. include:: limitation.rst.txt

.. include:: resources.rst.txt

まとめ🌯：the app runner Streamlit Season✨
============================================================

* Streamlitは機械学習分野で注目される **プロトタイピングツール**
* ハンズオンを通して3つの原則を共有
* Webアプリかの考察から、あくまでプロトタイピング

再掲 Streamlit Principles
============================================================

1. **Pythonスクリプト**、是れ即ちアプリ
2. 値変わらば、 **最新の値** を変数に代入してスクリプトを **再実行**
3. スクリプトを再実行する方針ゆえ、 **キャッシュ利用を指定** すべし

Streamlit「とびっきりの魔法をかけてあげるわ！」
------------------------------------------------

* **Pythonスクリプトを書くだけ** でインタラクティブなアプリになる
* スクリプトをGitHubで公開して、Streamlit sharingで指定するだけの **簡単デプロイ**

Streamlit「とびっきりの魔法をかけてあげるわ！」承前
------------------------------------------------------------------------------------------------

* :command:`streamlit run URL` コピペすら不要という、こんなに簡単なスクリプトの共有方法がかつてあっただろうか
* **キャッシュ！** スクリプトを何度も再実行しているので、積極利用しましょう

最後に Special thanks
------------------------------------------------

* 社内の勉強会でフィードバックくださった皆さま
* 前哨戦のおかげで資料引き締まりました！

ご清聴ありがとうございました
------------------------------------------------

**Enjoy** magical Streamlit Season!

Appendix
============================================================

* Scrapboxで発表準備
* https://scrapbox.io/nikkie-memos/Streamlit 以下

EOF
============================================================
