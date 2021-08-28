"""Based on call_limit_decorators.py"""

import time
from functools import wraps


class RunTooOftenError(Exception):
    pass


def once_per_minutes(func=None, /, *, n=1):
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

    if func is None:
        return middle

    return middle(func)


def calculate_bmi(height_m, weight_kg):
    return weight_kg / height_m / height_m


# Parameter func is calculate_bmi1
@once_per_minutes
def calculate_bmi1(height_m, weight_kg):
    return calculate_bmi(height_m, weight_kg)


# Parameter func is None
@once_per_minutes()
def calculate_bmi2(height_m, weight_kg):
    return calculate_bmi(height_m, weight_kg)


# Parameter func is None (another case)
@once_per_minutes(n=0)
def calculate_bmi3(height_m, weight_kg):
    return calculate_bmi(height_m, weight_kg)
