import argparse
from pathlib import Path

from helium import get_driver, go_to, kill_browser, start_firefox
from selenium.webdriver import FirefoxOptions

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("slide_path_or_directory_name")
    parser.add_argument("output_path", nargs="?", type=Path)
    parser.add_argument("--is_long_title", action="store_true")
    args = parser.parse_args()

    script_path = Path(__file__).resolve()
    project_root = script_path.parent.parent
    if not args.slide_path_or_directory_name.endswith(".html"):
        # Case: slide directory name only
        slide_directory = (
            project_root
            / "build"
            / "revealjs"
            / args.slide_path_or_directory_name
        )
        slides = list(slide_directory.glob("*.html"))
        assert len(slides) == 1, str(slides)
        slide_html_path = slides[0]
    else:
        # Case: slide path
        slide_html_path = Path(args.slide_path_or_directory_name).resolve()
    slide_page_url = slide_html_path.as_uri()
    # タイトルが長い場合は2枚めを使う運用をしている
    if args.is_long_title:
        slide_page_url += "#/1"

    if not args.output_path:
        args.output_path = (
            project_root
            / "docs"
            / "_images"
            / "ogps"
            / f"{slide_html_path.stem}.png"
        )

    options = FirefoxOptions()
    options.add_argument("--width=800")
    options.add_argument("--height=485")  # ブラウザウィンドウ上部が85px分ある

    start_firefox(options=options, headless=True)
    go_to(slide_page_url)  # TODO: #/1 のようにページの指定を追加可能に
    get_driver().save_screenshot(str(args.output_path))
    kill_browser()
