import argparse
from pathlib import Path

from helium import get_driver, go_to, kill_browser, start_firefox
from selenium.webdriver import FirefoxOptions


def take_screenshot(url, save_path):
    options = FirefoxOptions()
    options.add_argument("--width=800")
    options.add_argument("--height=485")  # ブラウザウィンドウ上部が85px分ある

    start_firefox(options=options, headless=True)
    go_to(url)
    get_driver().save_screenshot(save_path)
    kill_browser()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("output_path", type=Path)
    args = parser.parse_args()

    take_screenshot(args.url, str(args.output_path))
