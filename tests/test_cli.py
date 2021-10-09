from io import StringIO

from thtml.cli import write_html
from thtml.options import Scope


def test_write_html() -> None:
    writer = StringIO()
    write_html(text="\033[1mHello, world!\033[22m", scope=Scope.FRAGMENT, writer=writer)
    assert (
        writer.getvalue()
        == """<style type="text/css">.thtml { background: #101013; border-radius: 0.5rem; color: var(--white); font-family: Fira Code, Consolas, "Andale Mono WT", "Andale Mono", "Lucida Console", "Lucida Sans Typewriter", "DejaVu Sans Mono", "Bitstream Vera Sans Mono", "Liberation Mono", "Nimbus Mono L", Monaco, "Courier New", Courier, monospace;; letter-spacing: 0.03rem; margin-left: auto; margin-right: auto; padding: 2rem; width: max-content; --white: #CCC; } .thtml-code { font-family: inherit; } .weight-heavy { font-weight: bold; }</style><pre class="nohighlight thtml"><code class="thtml-code"><span class="weight-heavy">Hello, world!</span></code></pre>"""
    )
