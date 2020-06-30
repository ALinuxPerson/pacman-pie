# -*- coding: utf-8 -*-
"""This module will be the main module to be used for cli."""
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
    """The argument parser. Delegated to a function for testing.

    Args:
        args (List[str]): The arguments given. Usually comes from sys.argv.

    Returns:
        argparse.Namespace: The arguments.
    """
    if args is None:
        args = sys.argv[1:]
    parser.add_argument(
        "-V",
        "--version",
        action="store_true",
        help="show program's version number and exit"
    )
    parser.add_argument(
        "-b",
        "--dbpath",
        help="specify an alternative database location",
        default="/var/lib/pacman"
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="enable debug output"
    )
    return parser.parse_args(args)


def main(args: List[str] = None):
    """The main entry point.

    Args:
        args (List[str]): The arguments given. Usually comes from sys.argv.

    Returns:
        None: nothing will be returned.
    """
    if args is None:
        args = sys.argv[1:]
    parsed: argparse.Namespace = parse_args(args)
    if parsed.version:
        levels.info(_version_string)


if __name__ == '__main__':
    main()
