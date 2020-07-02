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
