# Usage

=== "Python"

    ```python
    from slugkit import slugify

    slugify("Hello, World!")  # 'hello-world'
    ```

=== "Command line"

    ```console
    $ slugkit "Hello, World!"
    hello-world
    ```

    The same command is available as `python -m slugkit`.

## Changing the separator

```python
slugify("Hello World", separator="_")   # 'hello_world'
slugify("Hello World", separator="")    # raises ValueError
```

On the command line use `-s` / `--separator`:

```console
$ slugkit -s _ "Hello World"
hello_world
```

## Limiting the length

`max_length` never cuts a word in half, unless the very first word is already too long.

```python
slugify("A very long article title", max_length=12)  # 'a-very-long'
slugify("extraordinary title", max_length=5)         # 'extra'
```

On the command line use `-m` / `--max-length`.

## Non-ASCII text

Accents are removed, and letters without an ASCII decomposition are transliterated.

| Input | Output |
|---|---|
| `Xin chào, Việt Nam!` | `xin-chao-viet-nam` |
| `Đường Đê` | `duong-de` |
| `Straße Café` | `strasse-cafe` |

!!! warning "Scripts without a Latin form"
    Characters that cannot be reduced to ASCII, such as Chinese or Arabic, are dropped. A string made only of such characters produces an empty slug.

## Validating slugs

```python
from slugkit import is_slug

is_slug("hello-world")  # True
is_slug("Hello World")  # False
```
