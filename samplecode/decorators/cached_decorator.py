import functools
import time


def cache_enabled(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = kwargs["number"]
        if key in cache:
            return cache[key]
        retval = func(*args, **kwargs)
        cache[key] = retval
        return retval

    return wrapper


@cache_enabled
def get_api(number):
    """外部のAPIへのリクエスト送信のような時間のかかる処理を単純化しています"""
    time.sleep(2)
    return number + 1


if __name__ == "__main__":
    for i in [1, 2, 1, 2, 3]:
        # 2回めの1と2の呼び出しではキャッシュが使われるので2秒待たない
        print("-" * 10)
        print(get_api(number=i))
        print("-" * 10)
