from abc import ABC, abstractmethod
from pathlib import Path
from typing import Iterable


class BaseRemover(ABC):
    """Base class for all removers."""

    @abstractmethod
    def remove(self, artifacts: Iterable[Path]) -> None:
        """Remove the given artifacts."""
