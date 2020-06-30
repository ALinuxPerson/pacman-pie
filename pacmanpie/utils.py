from typing import ItemsView, Any, Optional, IO, Text, NoReturn
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
            2, f"{self.prog}: An error occurred while trying to parse the arguments.\n"
               f"{message}"
        )


def _generate_variable_expression(name: str, value: Any) -> str:
    value = f"'{value}'" if isinstance(str, value) else value
    return f"{name}={value}"


def generate_repr(self) -> str:
    class_name: str = self.__class__.__name__
    class_items: ItemsView[str, Any] = self.__dict__.items()
    return \
        f"<{class_name} object: {' '.join(_generate_variable_expression(name, value) for name, value in class_items if not name.startswith('_'))}>"
