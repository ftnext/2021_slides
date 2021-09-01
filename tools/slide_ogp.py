import argparse
from pathlib import Path

from helium import get_driver, go_to, kill_browser, start_firefox
from selenium.webdriver import FirefoxOptions

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("slide_directory_name")
    args = parser.parse_args()

    script_path = Path(__file__).resolve()
    project_root = script_path.parent.parent
    slide_directory = (
        project_root / "build" / "revealjs" / args.slide_directory_name
    )
    slides = list(slide_directory.glob("*.html"))
    assert len(slides) == 1, str(slides)
    slide_html_path = slides[0]

    ogp_path = (
        project_root
        / "docs"
        / "_images"
        / "ogps"
        / f"{args.slide_directory_name}.png"
    )

    options = FirefoxOptions()
    options.add_argument("--width=800")
    options.add_argument("--height=485")  # ブラウザウィンドウ上部が85px分ある

    start_firefox(options=options, headless=True)
    go_to(f"file://{slide_html_path}")  # TODO: #/1 のようにページの指定を追加可能に
    get_driver().save_screenshot(str(ogp_path))
    kill_browser()
