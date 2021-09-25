from io import StringIO

from thtml.cli import write_html
from thtml.options import Scope


def test_write_html() -> None:
    writer = StringIO()
    write_html(text="\033[1mHello, world!\033[22m", scope=Scope.FRAGMENT, writer=writer)
    assert (
        writer.getvalue()
        == """<style type="text/css">@import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@400&display=swap'); @import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:ital,wght@0,700;1,700&display=swap'); .thtml { font-family: var(--default-font); letter-spacing: 0.03rem; background: var(--black); color: var(--white); width: max-content; padding: 2rem; border-radius: 1rem; --black: #000; --default-font: 'Roboto Mono'; --white: #CCC; } .thtml-code { font-family: inherit; } .weight-heavy { font-weight: 700; }</style><pre class="nohighlight thtml"><code class="thtml-code"><span class="weight-heavy">Hello, world!</span><span class="weight-normal"></span></code></pre>"""
    )
