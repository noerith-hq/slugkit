# slugkit

**slugkit** turns any text into a clean, URL-friendly slug. It has no dependencies, ships type hints, and handles accented and Vietnamese text out of the box.

!!! info "This is a sample project"
    slugkit exists to demonstrate an open-source repository with versioned documentation on GitHub Pages. Copy it as a starting point for your own project.

## At a glance

```python
from slugkit import slugify

slugify("Xin chào, Việt Nam!")        # 'xin-chao-viet-nam'
slugify("Hello World", separator="_") # 'hello_world'
```

- **No dependencies.** Pure standard library.
- **Unicode aware.** Accents are stripped; `đ`, `ß`, `ø` and friends are transliterated.
- **Predictable truncation.** `max_length` cuts at a word boundary.
- **Typed.** Ships `py.typed`.

## Where to next

- [Getting started](getting-started.md): install slugkit and run your first example.
- [Usage](guide/usage.md): separators, length limits, and the command line.
- [API reference](reference/api.md): every public function.
- [Contributing](contributing.md): set up a development environment.
