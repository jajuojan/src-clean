"""
Base scanner interface.
"""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Set


class BaseScanner(ABC):
    """Base class for all build artifact scanners."""

    @abstractmethod
    def scan(self, root_path: Path) -> Set[Path]:
        """
        Scan for build artifacts in the given root path.
        Returns a set of Paths to be removed.
        """
