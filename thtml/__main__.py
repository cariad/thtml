from argparse import ArgumentParser
from sys import stdin, stdout
from tempfile import NamedTemporaryFile
from time import sleep
from webbrowser import open as open_web

from naughtty import NaughTTY

from thtml import get_version
from thtml.cli import write_html
from thtml.options import Scope


def cli_entry() -> None:
    parser = ArgumentParser(description="Converts text to HTML.", add_help=False)

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
        "-t",
        "--theme",
        help="path to custom theme YAML file",
    )

    parser.add_argument(
        "--version",
        action="store_true",
        help="shows the version",
    )

    args, command = parser.parse_known_args()

    if args.version:
        print(get_version())
        return

    if command:
        ntty = NaughTTY(command)
        ntty.execute()
        body = ntty.output

    else:
        body = stdin.read()

    if args.open:
        with NamedTemporaryFile("a+") as temp:
            write_html(
                text=body,
                scope=Scope(args.scope),
                writer=temp,
                theme=args.theme,
            )
            open_web(f"file://{temp.name}")
            # Give the browser a chance to open the file before we delete it:
            sleep(1)
            return

    write_html(
        text=body,
        scope=Scope(args.scope),
        writer=stdout,
        theme=args.theme,
    )


if __name__ == "__main__":
    cli_entry()
