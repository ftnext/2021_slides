"""Ref: https://github.com/reuven/Forkwell-2021-July-6/blob/main/Forkwell%20-%202021-July-6.ipynb"""

import time
from functools import wraps


class RunTooOftenError(Exception):
    pass


def once_per_minute(func):
    last_ran_at = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal last_ran_at
        current_time = time.time()
        if current_time - last_ran_at < 60:
            raise RunTooOftenError(
                f"Wait longer before running {func.__name__}"
            )
        last_ran_at = current_time
        value = func(*args, **kwargs)
        return value

    return wrapper


def once_per_minute_with_parenthesis():
    def middle(func):
        last_ran_at = 0

        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal last_ran_at
            current_time = time.time()
            if current_time - last_ran_at < 60:
                raise RunTooOftenError(
                    f"Wait longer before running {func.__name__}"
                )
            last_ran_at = current_time
            value = func(*args, **kwargs)
            return value

        return wrapper

    return middle


def once_per_n_minutes(n):
    def middle(func):
        last_ran_at = 0

        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal last_ran_at
            current_time = time.time()
            if current_time - last_ran_at < n * 60:
                raise RunTooOftenError(
                    f"Wait longer before running {func.__name__}"
                )
            last_ran_at = current_time
            value = func(*args, **kwargs)
            return value

        return wrapper

    return middle


def calculate_bmi(height_m, weight_kg):
    return weight_kg / height_m / height_m


@once_per_minute
def calculate_bmi1(height_m, weight_kg):
    return calculate_bmi(height_m, weight_kg)


@once_per_n_minutes(0)
def calculate_bmi2(height_m, weight_kg):
    return calculate_bmi(height_m, weight_kg)


@once_per_n_minutes(n=3)
def calculate_bmi3(height_m, weight_kg):
    return calculate_bmi(height_m, weight_kg)


@once_per_minute_with_parenthesis()
def calculate_bmi4(height_m, weight_kg):
    return calculate_bmi(height_m, weight_kg)
