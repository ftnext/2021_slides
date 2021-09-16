"""Cool helium code with context manager.

Always kill browser, even if an exception is raised.
"""

import os
from contextlib import contextmanager

from helium import (
    Text,
    click,
    go_to,
    kill_browser,
    start_firefox,
    wait_until,
    write,
)


@contextmanager
def using_firefox():
    start_firefox()
    try:
        yield
    finally:
        kill_browser()


if __name__ == "__main__":
    with using_firefox():
        go_to("connpass.com/login")
        write(os.getenv("CONNPASS_USERNAME"), into="ユーザー名")
        write(os.getenv("CONNPASS_PASSWORD"), into="パスワード")
        click("ログインする")

        wait_until(Text("あなたのイベント").exists)
