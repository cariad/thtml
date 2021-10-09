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

## 👋 Hello!

**Hello!** I'm [Cariad Eccleston](https://cariad.io) and I'm an independent/freelance software engineer. If my work has value to you, please consider [sponsoring](https://github.com/sponsors/cariad/).

If you ever raise a bug, request a feature or ask a question then mention that you're a sponsor and I'll respond as a priority. Thank you!
