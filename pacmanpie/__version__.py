import pathlib
from typing import (
    Tuple,
    Optional,
    List
)
from dataclasses import dataclass
import os
from pacmanpie import utils


@dataclass
class VersionData:
    major: int
    minor: int
    micro: int
    label: Optional[str] = None


class Version:
    def __init__(self, version: str):
        self.version = version
        self._version_split: Tuple[str, ...] = tuple(self.version.split("."))
        self._verify_version(self._version_split)
        self._as_data: VersionData = self.as_data

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
        try:
            major, minor, micro, label = self._version_split
            return VersionData(int(major), int(minor), int(micro), label)
        except ValueError:
            major, minor, micro = self._version_split
            return VersionData(int(major), int(minor), int(micro), None)

    @property
    def major(self) -> int:
        return self._as_data.major

    @property
    def minor(self) -> int:
        return self._as_data.minor

    @property
    def micro(self) -> int:
        return self._as_data.micro

    @property
    def label(self) -> Optional[str]:
        return self._as_data.label

    @property
    def version_name(self) -> str:
        versions: List[str] = [str(part) for part in self.__iter__()]
        if not self.label:
            versions.remove("None")
        return ".".join(versions)

    def bump_major(self):
        self._as_data.major += 1
        self._as_data.minor = self._as_data.micro = 0

    def bump_minor(self):
        self._as_data.minor += 1
        self._as_data.micro = 0

    def bump_micro(self):
        self._as_data.micro += 1

    def write_to_disk(self, path: str):
        with open(os.path.join(path, "VERSION"), "w") as ver_file:
            ver_file.write(self.version_name)

    def __iter__(self):
        for version_label in (self.major, self.minor, self.micro, self.label):
            yield version_label

    def __repr__(self) -> str:
        return utils.generate_repr(self)


_file: pathlib.Path = pathlib.Path(__file__)
_version_name: str = pathlib.Path(str(_file.parent.parent.joinpath("VERSION"))).read_text() or "0.1.0"
_version: Version = Version(_version_name)
__version__: str = _version.version_name
