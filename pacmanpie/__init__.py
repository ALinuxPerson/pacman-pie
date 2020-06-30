import pyalpm as alpm
import argparse
import sys
from typing import List
from rich import print
from pacmanpie.__version__ import __version__ as version
import pycman as pacman
from pacmanpie import levels

parser = argparse.ArgumentParser(
    description="pacman-pie: a pythonic implementation of pacman",
    prog="pacman-pie"
)
_version_string: str = f"""pacman-pie version {version}
pyalpm version {alpm.version()}

pacman-pie  Copyright (C) 2020  ALinuxPerson
This program comes with ABSOLUTELY NO WARRANTY;
This is free software, and you are welcome to redistribute it
under certain conditions.
        """


def parse_args(args: List[str] = None) -> argparse.Namespace:
    if args is None:
        args = sys.argv[1:]
    parser.add_argument(
        "-V",
        "--version",
        action="store_true",
        help="show program's version number and exit"
    )
    return parser.parse_args(args)


def main(args: List[str] = None):
    if args is None:
        args = sys.argv[1:]
    parsed: argparse.Namespace = parse_args(args)
    if parsed.version:
        levels.info(_version_string)


if __name__ == '__main__':
    main()
