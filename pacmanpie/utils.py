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

from typing import Optional, IO, Text, NoReturn
from rich import print
import argparse
import sys


class RichArgumentParser(argparse.ArgumentParser):
    def _print_message(self, message: str, file: Optional[IO[str]] = ...) -> None:  # type: ignore
        if message:
            print(message, file=file or sys.stderr)

    def error(self, message: Text) -> NoReturn:
        self.print_usage(sys.stderr)
        self.exit(
            2,
            f"{self.prog}: An error occurred while trying to parse the arguments.\n"
            f"{message}",
        )
