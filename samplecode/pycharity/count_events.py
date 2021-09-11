import argparse
import re
from collections import Counter

import jsonlines

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    args = parser.parse_args()

    months = []
    with jsonlines.open(args.input) as f:
        for row in f:
            m = re.match(r"2021/(\d{2})", row["schedule"])
            month = int(m[1])
            months.append(month)

    month_counter = Counter(months)
    for month, count in sorted(
        month_counter.most_common(), key=lambda t: t[0]
    ):
        print(f"{month}月\t{count}")
