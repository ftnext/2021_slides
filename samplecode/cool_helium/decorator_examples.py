"""Cool helium code with decorator.

You don't have to write `start_firefox` every time.

Usage:

$ python -i decorator_examples.py

>>> search_helium_repository()
>>> kill_browser()
>>> login_connpass()
>>> kill_browser()
"""

import os
from functools import wraps

from helium import (
    ENTER,
    Text,
    click,
    go_to,
    kill_browser,
    press,
    start_firefox,
    wait_until,
    write,
)


def using_firefox(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_firefox()
        func(*args, **kwargs)

    return wrapper


@using_firefox
def search_helium_repository():
    """HeliumのGitHubレポジトリを検索して移動する"""
    go_to("google.com")
    write("helium selenium github")
    press(ENTER)
    click("Selenium-python but lighter: Helium - GitHub")


@using_firefox
def login_connpass():
    """connpassにログインする（ユーザー名とパスワードは環境変数を想定）"""
    go_to("connpass.com/login")
    write(os.getenv("CONNPASS_USERNAME"), into="ユーザー名")
    write(os.getenv("CONNPASS_PASSWORD"), into="パスワード")
    click("ログインする")

    wait_until(Text("あなたのイベント").exists)
