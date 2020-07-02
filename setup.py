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

from pacmanpie.__version__ import __version__ as version
import setuptools

setuptools.setup(
    name="pacman-pie",
    author="ALinuxPerson",
    description="A pythonic implementation of Arch Linux's pacman using pyalpm.",
    version=version,
    entry_points={"console_scripts": ["ppacman=pacmanpie.__main__:main"]},
)
