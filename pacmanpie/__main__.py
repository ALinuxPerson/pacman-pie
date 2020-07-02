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

from pacmanpie import levels
from typing import List
import pacmanpie
import sys


def _package_exists(package_name: str) -> bool:
    """Checks if a package exists.

    Args:
        package_name: The package name to check.

    Returns:
        True if the package is found, False otherwise.
    """
    try:
        __import__(package_name)
        return True
    except ImportError:
        return False


def _module_error(*package_names: str) -> bool:
    """Used for pretty detection of unknown imports.

    Args:
        *package_names: The package names to pass through _package_exists.

    Returns:
        True if all modules passed are found, False otherwise.
    """
    package: str
    for package in package_names:
        if not _package_exists(package):
            levels.error(
                f"The module {package} doesn't exist. Did you read the instructions in the README.md yet?"
            )
            return False
    else:
        return True


def main(args: List[str] = None) -> None:
    """The main entry point that will be used for setup.py.

    Args:
        args: The arguments to pass to the argument parser.

    Returns:
        Nothing should be returned.
    """
    if _module_error("pyalpm", "pycman"):
        pacmanpie.main(args or sys.argv[1:])


if __name__ == "__main__":
    main()
