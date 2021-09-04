from argparse import ArgumentParser
from io import BytesIO
from os import read
from pty import spawn
from sys import stdin
from tempfile import NamedTemporaryFile
from time import sleep
from webbrowser import open as open_web

from thtml import render
from thtml.options import Scope


def cli_entry() -> None:
    parser = ArgumentParser(description="Converts text to HTML.", add_help=False)
    parser.add_argument(
        "-c",
        "--command",
        help="command",
        action="store_true",
    )

    parser.add_argument(
        "-o",
        "--open",
        action="store_true",
        help="opens the output in the default browser",
    )

    parser.add_argument(
        "-s",
        "--scope",
        choices=[Scope.DOCUMENT.value, Scope.FRAGMENT.value],
        default=Scope.DOCUMENT.value,
        help="output an entire HTML document (default) or fragment",
    )

    parser.add_argument(
        "--version",
        action="store_true",
        help="shows the version",
    )

    args, extras = parser.parse_known_args()

    if args.command:
        with BytesIO() as script:

            def read_chunk(fd: int) -> bytes:
                data = read(fd, 1024)
                script.write(data)
                return data

            # Executive decision: we don't support passing stdin to child.
            spawn(extras, read_chunk)
            script.flush()
            script.seek(0)
            body = script.read().decode("UTF-8")

    else:
        body = stdin.read()

    html = render(body=body, scope=Scope(args.scope))

    print(html)

    if args.open:
        with NamedTemporaryFile() as temp:
            with open(temp.name, "w") as file:
                file.write(html)
            open_web(f"file://{temp.name}")
            # Give the browser a chance to open and grab the temporary file
            # before we delete it:
            sleep(1)


if __name__ == "__main__":
    cli_entry()
