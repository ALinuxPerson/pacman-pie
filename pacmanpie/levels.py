from rich.console import Console
import sys

_console: Console = Console(file=sys.stderr)


def info(message: str):
    for line in message.splitlines():
        _console.print(f"[dark_blue]🛈 [blue]{line}")


def success(message: str):
    for line in message.splitlines():
        _console.print(f"[dark_green]‎✓ [green4]{line}")


def warn(message: str):
    for line in message.splitlines():
        _console.print(f"[yellow]⚠ [yellow3]{line}")


def error(message: str):
    for line in message.splitlines():
        _console.print(f"[dark_red]✗ [red]{line}")


def debug(message: str):
    for line in message.splitlines():
        _console.log(f"[cyan]🔍 {line}")
