from io import StringIO

from pytest import mark

from thtml.cli import write_html
from thtml.options import Scope


@mark.parametrize(
    "theme, expect",
    [
        (
            "default",
            """<style type="text/css">.thtml { background: #101013; border-radius: 0.5rem; color: var(--white); font-family: Fira Code, Consolas, "Andale Mono WT", "Andale Mono", "Lucida Console", "Lucida Sans Typewriter", "DejaVu Sans Mono", "Bitstream Vera Sans Mono", "Liberation Mono", "Nimbus Mono L", Monaco, "Courier New", Courier, monospace; letter-spacing: 0.03rem; margin-left: auto; margin-right: auto; padding: 2rem; width: max-content; --white: #CCC; --black: #000; } .thtml-code { font-family: inherit; } .foreground-black { border-color: var(--black); color: var(--black); } .foreground-white { border-color: var(--white); color: var(--white); } .foreground-default { border-color: var(--white); color: var(--white); }</style><pre class="nohighlight thtml"><code class="thtml-code"><span class="foreground-black">Black, </span><span class="foreground-white">White!</span><span class="foreground-default"></span></code></pre>""",
        ),
        (
            "google-fonts",
            """<style type="text/css">@import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@400&display=swap'); .thtml { background: #101013; border-radius: 0.5rem; color: var(--white); font-family: var(--default-font); letter-spacing: 0.03rem; margin-left: auto; margin-right: auto; padding: 2rem; width: max-content; --default-font: 'Roboto Mono'; --white: #CCC; --black: #000; } .thtml-code { font-family: inherit; } .foreground-black { border-color: var(--black); color: var(--black); } .foreground-white { border-color: var(--white); color: var(--white); } .foreground-default { border-color: var(--white); color: var(--white); }</style><pre class="nohighlight thtml"><code class="thtml-code"><span class="foreground-black">Black, </span><span class="foreground-white">White!</span><span class="foreground-default"></span></code></pre>""",
        ),
        (
            "plain",
            """<style type="text/css">.thtml { --black: #000; --white: #CCC; } .foreground-black { border-color: var(--black); color: var(--black); } .foreground-white { border-color: var(--white); color: var(--white); } .foreground-default { border-color: var(--white); color: var(--white); }</style><pre class="nohighlight thtml"><code class="thtml-code"><span class="foreground-black">Black, </span><span class="foreground-white">White!</span><span class="foreground-default"></span></code></pre>""",
        ),
    ],
)
def test_write_html(theme: str, expect: str) -> None:
    writer = StringIO()
    write_html(
        text="\033[30mBlack, \033[37mWhite!\033[39m",
        theme=theme,
        scope=Scope.FRAGMENT,
        writer=writer,
    )
    assert writer.getvalue() == expect
