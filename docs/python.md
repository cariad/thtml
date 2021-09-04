# Python usage

Import `render` and pass in the string to convert to HTML.

```python
from thtml import render

html = render("Hello, world!")
print(html)
```

By default, `render()` will return an entire HTML document. To return only a fragment -- say, to insert into your own `<body>` element -- pass a `Scope`.

```python
from thtml import render, Scope

html = render("Hello, world!", scope.FRAGMENT)
print(html)
```
