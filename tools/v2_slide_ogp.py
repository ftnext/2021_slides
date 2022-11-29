import argparse
from pathlib import Path
from urllib.parse import urlparse

from helium import get_driver, go_to, kill_browser, start_firefox
from selenium.webdriver import FirefoxOptions


def format_as_uri(string_for_slide: str) -> str:
    """
    >>> format_as_uri("http://example.com/slide.html")
    'http://example.com/slide.html'

    Case: slide path
    >>> expected = f"file://{Path.cwd() / 'build/revealjs/slide.html'}"
    >>> expected == format_as_uri("build/revealjs/slide.html")
    True

    Case: slide directory name only （doctestはルートで実行）
    >>> expected = f"file://{Path.cwd() / 'build/revealjs/ainouta/recommend_as_best.html'}"
    >>> expected == format_as_uri("ainouta")
    True
    """
    parsed = urlparse(string_for_slide)
    if parsed.scheme in ("http", "https"):
        return string_for_slide
    if string_for_slide.endswith(".html"):
        slide_path = Path(string_for_slide).resolve()
        return slide_path.as_uri()

    script_path = Path(__file__).resolve()
    project_root = script_path.parent.parent
    slide_directory = project_root / "build" / "revealjs" / string_for_slide
    slides = list(slide_directory.glob("*.html"))
    assert len(slides) == 1, str(slides)
    return slides[0].as_uri()


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
    parser.add_argument(
        "slide", help="URL, local file path or local directory name"
    )
    parser.add_argument("output_path", type=Path)
    args = parser.parse_args()

    uri = format_as_uri(args.slide)
    take_screenshot(uri, str(args.output_path))
