import pathlib
from typing import Tuple, Optional, List
from dataclasses import dataclass
import os


@dataclass
class VersionData:
    """The final serialized version data.

    Args:
        major (int): The major part of a version e.g. >>> 0 <<< .1.0.label
        minor (int): The minor part of a version e.g. 0. >>> 1 <<< .0.label
        micro (int): The micro part of a version e.g. 0.1. >>> 0 <<< .label
        label (Optional[str]): The (optional) label part of a version e.g. 0.1.0. >>> label <<<

    Examples:
        The VersionData class can be initalized using the following:

        >>> version_data = VersionData(  # this doesn't have to be used like this
        ... major=0,
        ... minor=1,
        ... micro=0,
        ... label="label"  # optional, can be removed
        ... )
        >>> print(version_data)
        VersionData(major=0, minor=1, micro=0, label='label')
        >>> version_data = VersionData(0, 1, 0)  # with no direct reference and label
        >>> print(version_data)
        VersionData(major=0, minor=1, micro=0, label=None)
    """

    major: int
    minor: int
    micro: int
    label: Optional[str] = None


class Version:
    """A portable way to store version data.

    Attributes:
        version (str): The version number in the format ($MAJOR.$MINOR.$MICRO) or ($MAJOR.$MINOR.$MICRO.$LABEL).

    Examples:
        The Version class may be used properly using the following:

        >>> Version("0.1.0")  # correct way
        <Version object: version=0.1.0>
        >>> Version("dcdvcdv")  # incorrect way
        Traceback (most recent call last):
        IndexError: expected 3 values to convert to a version object, got 1
    """

    def __init__(self, version: str):
        """The initialization of Version.

        Args:
            version: The version number in the format ($MAJOR.$MINOR.$MICRO) or ($MAJOR.$MINOR.$MICRO.$LABEL).
        """
        self._version = version
        self._verify_version(self._version_split)
        self._as_data: VersionData = self.as_data

    @property
    def version(self) -> str:
        return self._version

    @property
    def _version_split(self) -> Tuple[str, ...]:
        return tuple(self._version.split("."))

    @staticmethod
    def _verify_version(version_split: Tuple[str, ...]):
        if len(version_split) > 4 or len(version_split) < 3:
            raise IndexError(
                f"expected 3 values to convert to a version object, got {len(version_split)}"
            )
        for version_num in version_split[:3]:
            if not version_num.isdigit():
                raise TypeError(f"value {version_num} must resemble a digit")

    @property
    def as_data(self) -> VersionData:
        """Converts the version string to a VersionData object for easier reading.

        Returns:
            VersionData: The version string casted to a VersionData object.

        Notes:
            The other private _as_data variable is only used for easier manipulation and reading of as_data.

        Examples:
            You can use the as_data method properly by following these examples:

            >>> version = Version("0.1.0")
            >>> version.as_data  # without label
            VersionData(major=0, minor=1, micro=0, label=None)
            >>> version = Version("0.1.0.label")
            >>> version.as_data # with label
            VersionData(major=0, minor=1, micro=0, label='label')
        """
        try:
            major, minor, micro, label = self._version_split
            return VersionData(int(major), int(minor), int(micro), label)
        except ValueError:
            major, minor, micro = self._version_split
            return VersionData(int(major), int(minor), int(micro), None)

    @property
    def major(self) -> int:
        """Gets the major part of VersionData generated by as_data.

        Returns:
            int: The major value.

        Examples:
            You can get the major value using these examples:

            >>> version = Version("0.1.0")
            >>> version.major
            0
        """
        return self._as_data.major

    @property
    def minor(self) -> int:
        """Gets the minor part of VersionData generated by as_data.

        Returns:
            int: The minor value.

        Examples:
            You can get the minor value using these examples:

            >>> version = Version("0.1.0")
            >>> version.minor
            1
        """
        return self._as_data.minor

    @property
    def micro(self) -> int:
        """Gets the micro part of VersionData generated by as_data.

        Returns:
            int: The micro value.

        Examples:
            You can get the micro value using these examples:

            >>> version = Version("0.1.0")
            >>> version.micro
            0
                """
        return self._as_data.micro

    @property
    def label(self) -> Optional[str]:
        """Gets the optional label part of VersionData generated by as_data.

        Returns:
            Optional[str]: Depends on whether or not a label was given to the version argument.

        Examples:
            You can get the optional label value using these examples:

            >>> version = Version("0.1.0")
            >>> version.label  # without label
            >>> # nothing should appear!
            >>> version = Version("0.1.0.label")
            >>> version.label  # with label
            'label'
        """
        return self._as_data.label

    @property
    def name(self) -> str:
        """Parses and returns the version name from as_data.

        Returns:
            str: The full version name.

        Examples:
            You can get the version name using the following:

            >>> version = Version("0.1.0")
            >>> version.name  # without label
            '0.1.0'
            >>> version = Version("0.1.0.label")
            >>> version.name  # with label
            '0.1.0.label'
        """
        versions: List[str] = [str(part) for part in self.__iter__()]
        if not self.label:
            versions.remove("None")
        return ".".join(versions)

    def bump_major(self):
        """Bumps the major version part by one.

        Examples:
            You can bump the major version part using the following:

            >>> version = Version("0.1.0")
            >>> version.name  # with the major value not bumped
            '0.1.0'
            >>> version.bump_major()  # bumped major value
            >>> version.name  # with the major value bumped
            '1.0.0'
        """
        self._as_data.major += 1
        self._as_data.minor = self._as_data.micro = 0
        self._version = self.name

    def bump_minor(self):
        """Bumps the minor version part by one.

        Examples:
            You can bump the minor version part using the following:

            >>> version = Version("0.1.0")
            >>> version.name  # with the minor value not bumped
            '0.1.0'
            >>> version.bump_minor()  # bumped minor value
            >>> version.name  # with the minor value bumped
            '0.2.0'
        """
        self._as_data.minor += 1
        self._as_data.micro = 0
        self._version = self.name

    def bump_micro(self):
        """Bumps the micro version part by one.

        Examples:
            You can bump the micro version part using the following:

            >>> version = Version("0.1.0")
            >>> version.name  # with the micro value not bumped
            '0.1.0'
            >>> version.bump_micro()  # bumped micro value
            >>> version.name  # with the micro value bumped
            '0.1.1'
        """
        self._as_data.micro += 1
        self._version = self.name

    def write_to_disk(self, path: str = "."):
        """Writes the version_name to disk.

        Args:
            path (str): The path in which to write the version name to. Default is '.'

        Examples:
            >>> import tempfile
            >>> import os
            >>> import pathlib
            >>> version = Version("0.1.0.label")
            >>> with tempfile.TemporaryDirectory():
            ...     version.write_to_disk(".")
            ...     assert "VERSION" in os.listdir()
            ...     assert pathlib.Path("VERSION").read_text() == "0.1.0.label"
            ...     os.remove("VERSION")

        Returns:
            None
        """
        with open(os.path.join(path, "VERSION"), "w") as ver_file:
            ver_file.write(self.name)

    def __iter__(self):
        for version_label in (self.major, self.minor, self.micro, self.label):
            yield version_label

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} object: version={self.version}>"


_file: pathlib.Path = pathlib.Path(__file__)
_version_name: str = pathlib.Path(
    str(_file.parent.parent.joinpath("VERSION"))
).read_text() or "0.1.0"
_version: Version = Version(_version_name)
__version__: str = _version.name
