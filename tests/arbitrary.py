import random
from string import ascii_letters
from typing import Callable, Sequence


def arbitrary_string() -> str:
    """Arbitrary string generator."""
    str_len = random.randint(1, 1000)
    return "".join([random.choice(ascii_letters) for _ in range(str_len)])


def not_in(
    arbitrary_fn: Callable,
    existing_values: Sequence,
    n: int = 100,
) -> list:
    """Generate n values that are not in existing_values."""
    res = []
    for _ in range(n):
        s = arbitrary_fn()
        while s in existing_values:
            s = arbitrary_fn()
        res.append(s)
    return res
