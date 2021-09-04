from typing import List, Tuple

from thtml import Scope


def get_render_cases() -> List[Tuple[str, Scope, str]]:
    """Returns (body, scope, expect)."""
    return [
        (
            "foo\nbar",
            Scope.DOCUMENT,
            """<!doctype html><html><head><meta charset="utf-8" /><meta name="viewport" content="width=device-width, initial-scale=1" /><title>cariad/thtml</title><meta name="author" content="cariad/thtml" /></head><body><style type="text/css">.thtml { font-family: monospace; } .thtml .fg-red { color: #f00; } .thtml .fg-green { color: #0f0; }</style><pre class="nohighlight thtml"><code>foo\nbar</code></pre></body></html>""",
        ),
        (
            "foo\nbar",
            Scope.FRAGMENT,
            """<style type="text/css">.thtml { font-family: monospace; } .thtml .fg-red { color: #f00; } .thtml .fg-green { color: #0f0; }</style><pre class="nohighlight thtml"><code>foo\nbar</code></pre>""",
        ),
    ]
