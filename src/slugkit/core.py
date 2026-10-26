"""Core slug helpers."""

from __future__ import annotations

import re
import unicodedata

# Letters that NFKD normalization cannot decompose into an ASCII base letter.
_TRANSLITERATIONS = str.maketrans(
    {
        "đ": "d",
        "Đ": "D",
        "ß": "ss",
        "æ": "ae",
        "Æ": "AE",
        "ø": "o",
        "Ø": "O",
        "ł": "l",
        "Ł": "L",
    }
)

_NON_ALNUM = re.compile(r"[^a-z0-9]+")


def _check_separator(separator: str) -> None:
    if not separator:
        raise ValueError("separator must not be empty")


def slugify(text: str, separator: str = "-", max_length: int | None = None) -> str:
    """Convert text into a lowercase, ASCII-only, URL-friendly slug.

    Accents are stripped, every run of characters other than letters and digits
    becomes a single separator, and leading or trailing separators are dropped.

    Args:
        text: The text to convert.
        separator: String placed between words. Must not be empty.
        max_length: Maximum length of the result. The slug is cut at a word
            boundary; only when the first word alone is longer than this limit
            is that word truncated.

    Returns:
        The slug, which is an empty string if `text` has no letters or digits.

    Raises:
        ValueError: If `separator` is empty or `max_length` is less than 1.

    Example:
        ```python
        >>> slugify("Xin chào, Việt Nam!")
        'xin-chao-viet-nam'
        >>> slugify("Hello World", separator="_")
        'hello_world'
        >>> slugify("A very long article title", max_length=12)
        'a-very-long'
        ```
    """
    _check_separator(separator)
    if max_length is not None and max_length < 1:
        raise ValueError("max_length must be at least 1")

    decomposed = unicodedata.normalize("NFKD", text.translate(_TRANSLITERATIONS))
    ascii_text = decomposed.encode("ascii", "ignore").decode("ascii").lower()
    words = [word for word in _NON_ALNUM.split(ascii_text) if word]

    if max_length is None:
        return separator.join(words)

    slug = ""
    for word in words:
        candidate = f"{slug}{separator}{word}" if slug else word
        if len(candidate) > max_length:
            break
        slug = candidate
    if not slug and words:
        slug = words[0][:max_length]
    return slug


def is_slug(text: str, separator: str = "-") -> bool:
    """Check whether text is already a valid slug.

    A valid slug consists of lowercase ASCII letters and digits, with single
    separators between words and none at the start or end.

    Args:
        text: The text to check.
        separator: The word separator the slug is expected to use.

    Returns:
        True if `text` is a valid slug, False otherwise.

    Raises:
        ValueError: If `separator` is empty.

    Example:
        ```python
        >>> is_slug("hello-world")
        True
        >>> is_slug("Hello World")
        False
        ```
    """
    _check_separator(separator)
    pattern = rf"[a-z0-9]+(?:{re.escape(separator)}[a-z0-9]+)*"
    return re.fullmatch(pattern, text) is not None
