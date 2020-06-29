import pyalpm as alpm
import argparse
import sys
from typing import List

parser = argparse.ArgumentParser(
    description="pacman-pie: a pythonic implementation of pacman",
    prog="pacman-pie"
)


def parse_args(args: List[str] = None) -> argparse.Namespace:
    if args is None:
        args = sys.argv[1:]

if __name__ == '__main__':
    parse_args()
