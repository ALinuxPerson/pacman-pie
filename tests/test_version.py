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

import os
import pathlib
import pytest
from contextlib import contextmanager
from typing import Type, List, Optional, Tuple
from pacmanpie.__version__ import Version, VersionData
import random
import string


def generate_string(minimum_chars: int = 4, maximum_chars: int = 8) -> str:
    """Generates a random string of lowercase and uppercase characters.
    
    Args:
        minimum_chars: The minimum amount of characters to be returned.
        maximum_chars: The maximum amount of characters to be returned.

    Returns:
        The random string.
    """
    return "".join(
        random.choice(string.ascii_lowercase)
        for _ in range(minimum_chars, maximum_chars)
    )


def generate_version_string(
    minimum_version: int = 0,
    maximum_version: int = 100,
    add_label: Optional[bool] = None,
) -> str:
    """Generates a random version string that can be parsed by Version.

    Args:
        minimum_version: The minimum version number.
        maximum_version: The maximum version number.
        add_label: Whether or not a label part will be added to the version string.

    Raises:
        ValueError: If the minimum_version argument is lower than zero.

    Returns:
        A version string.
    """
    add_label = add_label or random.choice([True, False])
    if minimum_version < 0:
        raise ValueError(f"value {minimum_version} must be >= 0")

    def gen_value():
        return random.randint(minimum_version, maximum_version)

    if add_label:
        return f"{gen_value()}.{gen_value()}.{gen_value()}.{generate_string()}"
    return f"{gen_value()}.{gen_value()}.{gen_value()}"


# noinspection PyBroadException
@contextmanager
def not_raises(
    exceptions: Tuple[Type[Exception], ...], message: Optional[str] = None,
):
    """Checks if a test doesn't raise an exception.

    Args:
        exceptions: The exception.
        message: The (optional) message. Can have {exc_names} variable.

    Returns:
        Nothing will be returned.
    """
    exception_names: List[str] = [exception.__name__ for exception in exceptions]
    message = (message or "Test should've not raised {exc_names} exception(s)").format(
        exc_names=" or ".join(exception_names)
    )
    try:
        yield
    except exceptions:
        pytest.fail(message)


def test_if_version_successful() -> None:
    """
    Notes:
        This can fail if Version raises an IndexError or a TypeError.

    Returns:
        Nothing will be returned.
    """
    with not_raises((IndexError, TypeError)):
        Version("0.1.0")


@pytest.mark.parametrize("version_string", ["7.2", "4", ""])
def test_if_less_than_three_digits_raises_index_error(version_string: str) -> None:
    """
    Notes:
        This can fail if Version doesn't raise an IndexError regardless if there are 3 or less digits passed.

    Args:
        version_string: The version string.

    Returns:
        Nothing will be returned.
    """
    with pytest.raises(IndexError):
        Version(version_string)


@pytest.mark.parametrize(
    "version_string", ["major.minor.micro", "major.minor.micro.label"]
)
def test_if_letters_raises_type_error(version_string: str) -> None:
    """
    Notes:
        This can fail if Version doesn't raise a TypeError regardless if there are letters in the string outside the
        label.

    Args:
        version_string: The version string.

    Returns:
        Nothing will be returned.
    """
    with pytest.raises(TypeError):
        Version(version_string)


@pytest.mark.parametrize(
    "version_string", [generate_version_string() for _ in range(10)]
)
def test_if_given_version_is_the_same_as_version_property(version_string: str) -> None:
    """
    Notes:
        This can fail if the version string passed to Version isn't the same as the version property.

    Args:
        version_string: The version string.

    Returns:
        Nothing will be returned.
    """
    version: Version = Version(version_string)
    assert version.version == version_string


@pytest.mark.parametrize(
    "version_string,version_data",
    [
        ("12.7.2", VersionData(major=12, minor=7, micro=2)),
        ("98.2.16.alpha", VersionData(major=98, minor=2, micro=16, label="alpha")),
    ],
)
def test_if_version_as_data_checks_out(
    version_string: str, version_data: VersionData
) -> None:
    """
    Notes:
        This can fail if the passed version_data argument isn't the same as the version.as_data data.

    Args:
        version_string: The version string.
        version_data: The version data.

    Returns:
        Nothing will be returned.
    """
    version: Version = Version(version_string)
    assert version.as_data == version_data


@pytest.mark.parametrize(
    "version_string", [generate_version_string() for _ in range(10)]
)
def test_if_major_value_is_correct(version_string: str) -> None:
    """
    Notes:
        This can fail if the version object major value isn't the same as the actual major value.

    Args:
        version_string: The version string.

    Returns:
        Nothing will be returned.
    """
    version: Version = Version(version_string)
    actual_major_value: int = int(version_string.split(".")[0])
    assert version.major == actual_major_value


@pytest.mark.parametrize(
    "version_string", [generate_version_string() for _ in range(10)]
)
def test_if_minor_value_is_correct(version_string: str) -> None:
    """
    Notes:
        This can fail if the version object minor value isn't the same as the actual minor value.

    Args:
        version_string: The version string.

    Returns:
        Nothing will be returned.
    """
    version: Version = Version(version_string)
    actual_minor_value: int = int(version_string.split(".")[1])
    assert version.minor == actual_minor_value


@pytest.mark.parametrize(
    "version_string", [generate_version_string() for _ in range(10)]
)
def test_if_micro_value_is_correct(version_string: str) -> None:
    """
    Notes:
        This can fail if the version object micro value isn't the same as the actual micro value.

    Args:
        version_string: The version string.

    Returns:
        Nothing will be returned.
    """
    version: Version = Version(version_string)
    actual_micro_value: int = int(version_string.split(".")[2])
    assert version.micro == actual_micro_value


@pytest.mark.parametrize(
    "version_string", [generate_version_string(add_label=True) for _ in range(10)]
)
def test_if_label_value_is_correct(version_string: str) -> None:
    """
    Notes:
        This can fail if the version object label value isn't the same as the actual label value.

    Args:
        version_string: The version string.

    Returns:
        Nothing will be returned.
    """
    version: Version = Version(version_string)
    actual_label_value: str = version_string.split(".")[3]
    assert version.label == actual_label_value


@pytest.mark.parametrize(
    "version_string,bumped_major_value_string",
    [("65.54.32", "66.0.0"), ("12.24.34.hjdf", "13.0.0.hjdf")],
)
def test_if_bumped_major_value_is_correct(
    version_string: str, bumped_major_value_string: int
) -> None:
    """
    Notes:
        This test can fail if the newly bumped major value version name isn't the same as the bumped_major_value_string.

    Args:
        version_string: The version string.
        bumped_major_value_string: The bumped major value string.

    Returns:
        Nothing will be returned.
    """
    version: Version = Version(version_string)
    version.bump_major()
    assert version.name == bumped_major_value_string


@pytest.mark.parametrize(
    "version_string,bumped_minor_value_string",
    [("72.70.68", "72.71.0"), ("1.2.4.eight", "1.3.0.eight")],
)
def test_if_bumped_minor_value_is_correct(
    version_string: str, bumped_minor_value_string: int
) -> None:
    """
    Notes:
        This test can fail if the newly bumped minor value version name isn't the same as the bumped_minor_value_string.

    Args:
        version_string: The version string.
        bumped_minor_value_string: The bumped minor value string.

    Returns:
        Nothing will be returned.
    """
    version: Version = Version(version_string)
    version.bump_minor()
    assert version.name == bumped_minor_value_string


@pytest.mark.parametrize(
    "version_string,bumped_micro_value_string",
    [("13.26.39", "13.26.40"), ("70.63.67.micro", "70.63.68.micro")],
)
def test_if_bumped_micro_value_is_correct(
    version_string: str, bumped_micro_value_string: int
) -> None:
    """
    Notes:
        This test can fail if the newly bumped micro value version name isn't the same as the bumped_micro_value_string.

    Args:
        version_string: The version string.
        bumped_micro_value_string: The bumped micro value string.

    Returns:
        Nothing will be returned.
    """
    version: Version = Version(version_string)
    version.bump_micro()
    assert version.name == bumped_micro_value_string


@pytest.mark.parametrize(
    "version_string", [generate_version_string() for _ in range(10)]
)
def test_writing_to_disk(version_string: str) -> None:
    """
    Notes:
        This test can fail if either:
        a.) The file that should've been created by write_to_disk doesn't exist, or
        b.) The text generated by write_to_disk is not equal to the version string.

    Args:
        version_string: The version string.

    Returns:
        Nothing will be returned.
    """
    version: Version = Version(version_string)
    path: str = os.path.join(".", "VERSION")
    version.write_to_disk()
    with not_raises(
        (FileNotFoundError,),
        f"The path {path} doesn't exist, it should've been created by write_to_disk.",
    ):
        assert pathlib.Path(path).read_text() == version_string
        os.remove(path)
