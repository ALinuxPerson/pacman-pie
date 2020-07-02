# -*- coding: utf-8 -*-
"""This module will be the main module to be used for cli."""
import pyalpm as libalpm
import argparse
import sys
from typing import List
from pacmanpie.__version__ import __version__ as version
from pacmanpie import levels


_version_string: str = f"""pacman-pie {version} - pyalpm {libalpm.version()}

[bold yellow3] .--.
[bold yellow3]/ _.-' .-.  .-.  .-. 
[bold yellow3]\\  '-. '-'  '-'  '-'  
[bold yellow3] '--'

[italic]This program comes with ABSOLUTELY NO WARRANTY;
[italic]This is free software, and you are welcome to redistribute it
[italic]under certain conditions."""


def _parser() -> argparse.ArgumentParser:
    """The argument parser.

    Returns:
        Argument parser
    """
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description="pacman-pie: a pythonic implementation of pacman", prog="pacman-pie"
    )
    parser.add_argument(
        "-V",
        "--version",
        action="store_true",
        help="show program's version number and exit",
    )
    parser.add_argument(
        "-b",
        "--dbpath",
        help="specify an alternative database location",
        default="/var/lib/pacman",
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="enable debug output"
    )
    return parser


def _parse_args(
    parser: argparse.ArgumentParser, args: List[str] = None
) -> argparse.Namespace:
    """The parsed arguments. Converted to a function for testing.

    Args:
        parser: The argument parser.
        args: The arguments given. Usually comes from sys.argv.

    Returns:
        The arguments.
    """
    return parser.parse_args(args or sys.argv[1:])


def main(arguments: List[str] = None) -> None:
    """The main entry point.

    Args:
        arguments: The arguments given. Usually comes from sys.argv.

    Returns:
        Nothing will be returned.
    """
    parser: argparse.ArgumentParser = _parser()
    args: argparse.Namespace = _parse_args(parser, arguments or sys.argv[1:])
    if args.version:
        levels.info(_version_string)
