# thtml

[![CircleCI](https://circleci.com/gh/cariad/thtml/tree/main.svg?style=shield)](https://circleci.com/gh/cariad/thtml/tree/main) [![codecov](https://codecov.io/gh/cariad/thtml/branch/main/graph/badge.svg?token=a55OVLgAO1)](https://codecov.io/gh/cariad/thtml) [![Documentation Status](https://readthedocs.org/projects/thtml/badge/?version=latest)](https://thtml.readthedocs.io/en/latest/?badge=latest)

`thtml` (**t**o **HTML**) is a CLI tool and Python package for converting text to HTML.

For example, to pipe a command through `thtml`:

```bash
ls -al --color | thtml
```

```html
<!doctype html><html>...</html>
```

Include `--open` to send the HTML directly to your default browser:

```bash
ls -al --color | thtml --open
```

![Directory listing passed through thtml](https://github.com/cariad/thtml/raw/main/docs/ls.png)

Full documentation: [thtml.readthedocs.io](https://thtml.readthedocs.io)

## Installation

`thtml` requires Python 3.8 or later.

```bash
pip install thtml
```

## CLI usage

Pipe your command's output to `thtml`:

```bash
COMMAND | thtml
```

If your command needs to run in a pseudo-terminal to emit formatting escape codes:

```bash
thtml COMMAND
```

By default, `thtml` will write the HTML to stdout. To send the HTML to your default browser:

```bash
COMMAND | thtml --open
```

By default, `thtml` will generate an entire HTML document. To return only a fragment:

```bash
COMMAND | thtml --scope fragment
```

Full documentation: [thtml.readthedocs.io](https://thtml.readthedocs.io)

## Python usage

```python
from thtml import write_html

with open("hello.html", "w") as writer:
    write_html("\033[1mHello, world!\033[22m", writer)
```

Full documentation: [thtml.readthedocs.io](https://thtml.readthedocs.io)

## 👋 Hello!

**Hello!** I'm [Cariad Eccleston](https://cariad.io) and I'm an independent/freelance software engineer. If my work has value to you, please consider [sponsoring](https://github.com/sponsors/cariad/).

If you ever raise a bug, request a feature or ask a question then mention that you're a sponsor and I'll respond as a priority. Thank you!
