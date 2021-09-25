# Python usage

Import `write_html` then pass in the string convert to HTML and the `Scope` of the document to generate.

```python
from thtml import write_html, Scope

with open("hello.html", "w") as writer:
    write_html(
        "\033[1mHello, world!\033[22m",
        Scope.DOCUMENT,
        writer,
    )
```
