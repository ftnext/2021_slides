.. role:: raw-html(raw)
    :format: html

============================================================
私が初めてコードでコントリビュートしたときの話
============================================================

:Event: ラクス OSS LT会 vol.2
:Presented: 2021/08/18 nikkie

お前、誰よ
============================================================

* Python大好き **にっきー** （:raw-html:`<i class="fab fa-twitter"></i>` `@ftnext <https://twitter.com/ftnext>`_ / :raw-html:`<i class="fab fa-github"></i>` `@ftnext <https://github.com/ftnext>`_）
* Python歴3年半。データサイエンティストにしてNLPer

Python Conference JP 2021 座長🇨🇭
------------------------------------------------

.. raw:: html

    <iframe width="640" height="480" src="https://2021.pycon.jp/" title="PyCon JP 2021 Webサイト"></iframe>

2月の vol.1 でもLTしました⚡️
------------------------------------------------

.. raw:: html

    <iframe width="640" height="480" src="https://ftnext.github.io/2021_slides/rakus_Feb_oss/not_only_code_but_various_contributions.html" title="コードだけじゃない！いろいろなコントリビュート"></iframe>

アニメも好きです😍
------------------------------------------------

* 1つ挙げると『ハイキュー!!』🏐（ `あらすじ <https://alu.jp/series/%E3%83%8F%E3%82%A4%E3%82%AD%E3%83%A5%E3%83%BC%EF%BC%81%EF%BC%81>`_）
* ブロッカー月島（ツッキー）のエピソードが好き

ツッキーが言われるセリフ
------------------------------------------------

    それがお前がバレーにハマる瞬間だ（木兎さん）

実は今回のタイトルも意識しました

TODO：イチ推しのツッキーエピソードはYouTubeで見られます！！
------------------------------------------------------------------------------------------------

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/ycfEo598B5c" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

それがお前がバレーにハマる瞬間だ
------------------------------------------------

* このLT「私が初めてコードでコントリビュートしたときの話」
* 言い換えると、nikkieにとっての **OSSにハマる瞬間** の話

お品書き
------------------------------------------------

* 初めてコードでコントリビュートした事例紹介
* 振り返り：なぜコントリビュートできたか

LT「私が初めてコードでコントリビュートしたときの話」
------------------------------------------------

* **初めてコードでコントリビュートした事例紹介**
* 振り返り：なぜコントリビュートできたか

質問：PythonライブラリHeliumを知っていますか？
============================================================

Helium
------------------------------------------------

* :raw-html:`<i class="fab fa-github"></i>` https://github.com/mherrmann/selenium-python-helium
* できること：ブラウザ操作自動化
* Seleniumのラッパーで、 **非常に簡単** に書ける！💫

It's me!😎
------------------------------------------------

.. figure:: ../_static/rakus_Aug_oss/202108helium_contributor_nikkie.png

https://github.com/mherrmann/selenium-python-helium/graphs/contributors

経緯：ときは2020年5月
------------------------------------------------

* connpassから `参加一覧をCSV形式で<https://help.connpass.com/organizers/event-admin.html>`_ 定期的にダウンロード。自動化したい
* ブラウザ自動化が簡単に書けるHeliumを知っていた
* Google Chromeで試したら、サクッとダウンロードできた！🙌

普段遣いはFirefox
------------------------------------------------

* Chromeと同じコードでは動かない😢
* ダウンロードの確認ポップアップのため

これのことです、Firefoxの確認ポップアップ
------------------------------------------------

.. figure:: ../_static/rakus_Aug_oss/202108firefox_download_popup.png

確認ポップアップ抑制したい
------------------------------------------------

* Seleniumでの抑制例が見つかる ``options.setPreference()``

  * https://stackoverflow.com/a/36309735

* Heliumではどうやる？ Issueを見てみる🔍

Ability to set download directory and disable download or open popup using Firefox
------------------------------------------------------------------------------------------------

https://github.com/mherrmann/selenium-python-helium/issues/19

`Ownerのコメント <https://github.com/mherrmann/selenium-python-helium/issues/19#issuecomment-617803108>`_
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    Helium lets you supply ChromeOptions to start_chrome since the last release. Maybe something similar could be added for Firefox?

    I won't have time to implement this. But I will be happy to merge a PR that does it.

Ownerのコメント意訳
------------------------------------------------

* Heliumは最新のリリース(v3.0.2)で ``start_chrome`` 関数に ``ChromeOptions`` を提供できるようになった。おそらくFirefoxについても同様のものを加えられるんじゃないか
* 実装している時間がない。でも、それをするPRは喜んでマージするよ

手元のFirefoxだけでも動かせれば
------------------------------------------------

* ``start_chrome`` のコードを見てみる（ならって ``start_firefox`` をハックしようとした）
* 「 **あ、これ実装できるかも** 」

（環境構築でハマりつつも）できた！🙌
------------------------------------------------

* https://github.com/mherrmann/selenium-python-helium/pull/22/files
* Helium v3.0.3 としてリリースされた

LT「私が初めてコードでコントリビュートしたときの話」
------------------------------------------------

* 初めてコードでコントリビュートした事例紹介
* **振り返り：なぜコントリビュートできたか**
