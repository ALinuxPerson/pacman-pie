#  pacman-pie: A pythonic implementation of Arch Linux's pacman using pyalpm.
#  Copyright (C) 2020  ALinuxPerson
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
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
    root: argparse.ArgumentParser = argparse.ArgumentParser(
        description="pacman-pie: a pythonic implementation of pacman", prog="pacman-pie"
    )
    subparser = root.add_subparsers(prog="operations")
    root.add_argument(
        "-V",
        "--version",
        action="store_true",
        help="show program's version number and exit",
    )
    root.add_argument(
        "--config", help="specify an alternate config file"
    )  # TODO: implement config files, all alternative locations will be stored here
    root.add_argument(
        "-v", "--verbose", action="store_true", help="enable debug output"
    )
    root.add_argument(
        "--support", help="give debug information, then exit", action="store_true"
    )
    root.add_argument(
        "--no-confirm",
        help="bypass question messages, will automatically be true",
        action="store_true",
    )
    root.add_argument("--confirm", help="override --no-confirm", action="store_true")
    root.add_argument(
        "--disable-timeout", help="disables the download timeout", action="store_true"
    )

    transcation: argparse.ArgumentParser = argparse.ArgumentParser(add_help=False)
    transcation.add_argument(
        "-d", "--no-deps", help="skip dependency version checks", action="store_true",
    )
    transcation.add_argument(
        "--assume-installed",
        help="add fake package 'package' with version 'version'. format is $PACKAGE=$VERSION",
    )
    transcation.add_argument(
        "--dbonly", action="store_true", help="adds/removes the database entry only"
    )

    database: argparse.ArgumentParser = subparser.add_parser(
        name="database",
        description="operate on the package database",
        help="operate on the package database",
    )
    query: argparse.ArgumentParser = subparser.add_parser(
        name="query",
        description="query the package database",
        help="query the package database",
    )
    remove: argparse.ArgumentParser = subparser.add_parser(
        name="remove",
        description="remove package(s) from the system",
        help="remove package(s) from the system",
        parents=[transcation],
    )
    sync: argparse.ArgumentParser = subparser.add_parser(
        name="sync",
        description="synchronize packages",
        help="synchronize packages",
        parents=[transcation],
    )
    deptest: argparse.ArgumentParser = subparser.add_parser(
        name="deptest", description="check dependencies", help="check dependencies"
    )
    upgrade: argparse.ArgumentParser = subparser.add_parser(
        name="upgrade",
        description="upgrade or add package(s) to the system",
        help="upgrade or add package(s) to the system",
        parents=[transcation],
    )
    files: argparse.ArgumentParser = subparser.add_parser(
        name="files",
        description="query the files database",
        help="query the files database",
    )
    return root


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
