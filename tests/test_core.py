import pytest

from slugkit import is_slug, slugify


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Hello World", "hello-world"),
        ("  Hello,   World!  ", "hello-world"),
        ("Xin chào, Việt Nam!", "xin-chao-viet-nam"),
        ("Đường Đê", "duong-de"),
        ("Straße Café", "strasse-cafe"),
        ("already-a-slug", "already-a-slug"),
        ("snake_case and CamelCase", "snake-case-and-camelcase"),
        ("100% pure", "100-pure"),
        ("!!!", ""),
        ("", ""),
    ],
)
def test_slugify(text, expected):
    assert slugify(text) == expected


def test_custom_separator():
    assert slugify("Hello World", separator="_") == "hello_world"
    assert slugify("Hello World", separator="--") == "hello--world"


@pytest.mark.parametrize(
    ("max_length", "expected"),
    [
        (5, "a"),
        (6, "a-very"),
        (10, "a-very"),
        (11, "a-very-long"),
        (16, "a-very-long"),
        (17, "a-very-long-title"),
    ],
)
def test_max_length_cuts_at_word_boundary(max_length, expected):
    assert slugify("A very long title", max_length=max_length) == expected


def test_max_length_truncates_first_word_when_needed():
    assert slugify("extraordinary title", max_length=5) == "extra"


def test_slugify_rejects_empty_separator():
    with pytest.raises(ValueError, match="separator"):
        slugify("x", separator="")


def test_slugify_rejects_bad_max_length():
    with pytest.raises(ValueError, match="max_length"):
        slugify("x", max_length=0)


@pytest.mark.parametrize("text", ["hello", "hello-world", "a1-b2-c3", "2026"])
def test_is_slug_true(text):
    assert is_slug(text)


@pytest.mark.parametrize(
    "text", ["", "Hello", "hello world", "-hello", "hello-", "hello--world", "héllo"]
)
def test_is_slug_false(text):
    assert not is_slug(text)


def test_is_slug_custom_separator():
    assert is_slug("hello_world", separator="_")
    assert not is_slug("hello-world", separator="_")


def test_is_slug_rejects_empty_separator():
    with pytest.raises(ValueError, match="separator"):
        is_slug("x", separator="")
