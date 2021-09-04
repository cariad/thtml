from argparse import ArgumentParser

from thtml.version import get_version


def cli_entry() -> None:
    parser = ArgumentParser(description="Converts text to HTML.")
    parser.add_argument(
        "--version",
        action="store_true",
        help="output version then exit",
    )
    args = parser.parse_args()

    if args.version:
        print(get_version())
        exit(0)


if __name__ == "__main__":
    cli_entry()
