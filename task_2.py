import re
from typing import Any, Generator


def generator_numbers(text: str) -> Generator[Any, Any, Any]:
    pattern = r'\d+.\d+'
    numbers = re.findall(pattern, text)
    for item in numbers:
        yield float(item)


def sum_profit(text: str, generator: callable) -> float:
    return sum([item for item in generator(text)])
