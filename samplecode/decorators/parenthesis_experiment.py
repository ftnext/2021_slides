def decorator(func=None, /, *, n=1):
    print(f"decorator start: {func=} {n=}")

    def middle(func):
        print("middle start")

        def wrapper(*args, **kwargs):
            print(f"wrapper start: {args=}, {kwargs=}")
            func(*args, **kwargs)
            print("wrapper end")

        print("middle end")
        return wrapper

    print("decorator end")
    if func is None:
        return middle

    return middle(func)
