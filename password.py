"""This module generates complex passwords."""

from typing import Generator
from random import sample
from string import ascii_letters, digits, punctuation

def password_generator() -> Generator[str, None, None]:

    """Returns complex 16-character passwords using python
generator"""

    characters = ascii_letters + digits + punctuation

    while True:
        yield ''.join(sample(characters, 16))
