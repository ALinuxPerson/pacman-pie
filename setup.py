from pacmanpie.__version__ import __version__ as version
import setuptools

setuptools.setup(
    name="pacman-pie",
    author="ALinuxPerson",
    description="A pythonic implementation of Arch Linux's pacman using pyalpm.",
    version=version,
    entry_points={"console_scripts": ["ppacman=pacmanpie.__main__:main"]},
)
