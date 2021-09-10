import argparse
import logging
import time
from urllib.parse import urlencode
from urllib.request import urlopen

import jsonlines
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO)


def scrape_html(url):
    with urlopen(url) as res:
        raw_html = res.read()
    return raw_html


def parse_html_body(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup.body


def clean_schedule(raw_schedule):
    r"""
    >>> clean_schedule("\n終了\n      2021/09/10（金） 20:00〜\n      \n\n")
    '2021/09/10（金） 20:00〜'
    """
    return raw_schedule.strip().removeprefix("終了").lstrip()


def parse_event(soup):
    events = soup.find_all("div", "group_event_list")
    for event in events:
        if event.find("span", "label_status_event").text == "開催前":
            continue
        title = event.find("p", "event_title").text
        if not title.startswith("PyCon JP 2021"):
            continue
        raw_schedule = event.find("p", "schedule").text
        schedule = clean_schedule(raw_schedule)
        yield {"title": title, "schedule": schedule}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("group_event_url")
    parser.add_argument("output")
    args = parser.parse_args()

    has_next_page = True
    page = 1
    with jsonlines.open(args.output, "w") as fout:
        while has_next_page:
            url = f"{args.group_event_url}?{urlencode({'page': page})}"
            raw_html = scrape_html(url)
            logging.info("Scraped: %s", url)

            body = parse_html_body(raw_html)
            for event in parse_event(body):
                if not event["schedule"].startswith("2021"):
                    has_next_page = False
                    break
                fout.write(event)
            time.sleep(5)
            page += 1
