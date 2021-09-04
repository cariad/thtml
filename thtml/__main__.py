from argparse import ArgumentParser
from sys import stderr, stdin
from tempfile import NamedTemporaryFile
from time import sleep
from webbrowser import open as open_web

from thtml import render
from thtml.options import Scope
from thtml.version import get_version


def cli_entry() -> None:
    parser = ArgumentParser(description="Converts text to HTML.")
    parser.add_argument(
        "file",
        help="optional file to read (default is stdin)",
        nargs="?",
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

    args = parser.parse_args()

    if args.version:
        print(get_version())
        exit(0)

    if args.file:
        try:
            with open(args.file, "r") as f:
                body = f.read()
        except FileNotFoundError:
            print(f"file not found: {args.file}", file=stderr)
            exit(1)
    else:
        body = stdin.read()

    html = render(body=body, scope=Scope(args.scope))

    if args.open:
        with NamedTemporaryFile() as temp:
            with open(temp.name, "w") as file:
                file.write(html)
            open_web(f"file://{temp.name}")
            # Give the browser a chance to open and grab the temporary file
            # before we delete it:
            sleep(1)
    else:
        print(html)


if __name__ == "__main__":
    cli_entry()
