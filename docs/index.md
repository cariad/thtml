# thtml

`thtml` is a CLI tool and Python package for converting text to HTML.

## Installation

`thtml` requires Python 3.8 or later.

```bash
pip install thtml
```

## Command line usage

Pipe text into `thtml` via stdin to convert to HTML:

```bash
echo "Hello, world!" | thtml
```

```text
<!doctype html><html>...</html>
```

To open the result in the default browser, add the `-o` or `--open` argument:

```bash
echo "Hello, world!" | thtml --open
```

By default, `thtml` will return an entire HTML document. To return only a fragment to insert into your own `<body>` element, pass `--scope fragment`:

```bash
echo "Hello, world!" | thtml --scope fragment
```

```text
<style type="text/css">...</pre>
```

## Python usage

Import `render()` and pass in the string to convert to HTML:

```python
from thtml import render

html = render("Hello, world!")
print(html)
```

```text
<!doctype html><html>...</html>
```

By default, `render()` will return an entire HTML document. To return only a fragment to insert into your own `<body>` element, pass a scope:

```python
from thtml import render, Scope

html = render("Hello, world!", scope.FRAGMENT)
print(html)
```

```text
<style type="text/css">...</pre>
```
