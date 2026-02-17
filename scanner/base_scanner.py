"""
Base scanner interface.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import Set


@dataclass(frozen=True)
class Artifact:
    """Represents a build artifact."""

    path: Path
    type: str


class BaseScanner(ABC):
    """Base class for all build artifact scanners."""

    @abstractmethod
    def scan(self, root_path: Path) -> Set[Artifact]:
        """
        Scan for build artifacts in the given root path.
        Returns a set of Artifacts to be removed.
        """
