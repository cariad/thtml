# Python usage

Import `write_html` then pass in the string to convert to HTML and a string writer:

```python
from thtml import write_html

with open("hello.html", "w") as writer:
    write_html("\033[1mHello, world!\033[22m", writer)
```

By default, `write_html` will generate an entire HTML document. To generate just a fragment:

```python
from thtml import write_html, Scope

with open("hello.html", "w") as writer:
    write_html("\033[1mHello, world!\033[22m", writer, scope=Scope.FRAGMENT)
```

To use a custom [theme](theme.md):

```python
from thtml import write_html, Theme

theme: Theme = {...}

with open("hello.html", "w") as writer:
    write_html("\033[1mHello, world!\033[22m", writer, theme=theme)
```
