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

from rich.console import Console
import sys

_console: Console = Console(file=sys.stderr)


def info(message: str, no_icon: bool = False):
    for line in message.splitlines():
        _console.print(f" [dark_blue]{'' if no_icon else '[[🛈]]'} [blue]{line}")


def success(message: str, no_icon: bool = False):
    for line in message.splitlines():
        _console.print(f" [dark_green]{'' if no_icon else '[[✓]]'} [green4]{line}")


def warn(message: str, no_icon: bool = False):
    for line in message.splitlines():
        _console.print(f" [yellow]{'' if no_icon else '[[⚠]]'} [yellow3]{line}")


def error(message: str, no_icon: bool = False):
    for line in message.splitlines():
        _console.print(f" [dark_red]{'' if no_icon else '[[✗]]'} [red]{line}")


def debug(message: str):
    for line in message.splitlines():
        _console.log(f"[cyan]🔍 {line}")
