"""
Directly remove build artifacts from the filesystem.
"""

import shutil
from pathlib import Path
from typing import Iterable

from .base_delete import BaseRemover


class DirectRemover(BaseRemover):
    """Removes artifacts directly from the filesystem."""

    def remove(self, artifacts: Iterable[Path]) -> None:
        print("\nDeleting artifacts...")
        for artifact in artifacts:
            try:
                response = input(f"  Remove {artifact}? [y/N] ").lower().strip()
                if response != "y":
                    print(f"  Skipping {artifact}...")
                    continue

                print(f"  Removing {artifact}...")
                if artifact.is_dir():
                    shutil.rmtree(artifact)
                else:
                    artifact.unlink()
            except (OSError, PermissionError) as e:
                print(f"  Error removing {artifact}: {e}")
            except EOFError:
                print("\nInterrupted.")
                break
