from argparse import ArgumentParser

from thtml.version import get_version


def cli_entry() -> None:
    parser = ArgumentParser(
        prog=f"thtml v{get_version()}",
        description="Converts text to HTML.",
    )
    args = parser.parse_args()
    print(args)


if __name__ == "__main__":
    cli_entry()
