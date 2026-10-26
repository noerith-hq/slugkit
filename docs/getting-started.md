# Getting started

## Requirements

Python 3.10 or newer.

## Install

slugkit is not published to PyPI yet. Install it straight from GitHub:

```bash
pip install "git+https://github.com/noerith-hq/slugkit.git"
```

## Your first slug

```python
from slugkit import slugify, is_slug

title = "10 Tips for Writing Better Docs!"
slug = slugify(title)

print(slug)           # 10-tips-for-writing-better-docs
print(is_slug(slug))  # True
```

!!! tip
    Use [`is_slug`][slugkit.core.is_slug] to validate user-supplied slugs, and [`slugify`][slugkit.core.slugify] to generate them from titles.

## Next steps

Read the [usage guide](guide/usage.md) for the options each function accepts.
