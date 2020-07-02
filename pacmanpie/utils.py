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
