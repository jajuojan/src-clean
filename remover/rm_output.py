import os
from pathlib import Path
from typing import Iterable
from .base_delete import BaseRemover


class ScriptRemover(BaseRemover):
    """Generates a shell script to remove artifacts."""

    def __init__(self, output_file: str = "clean.sh"):
        self.output_file = output_file

    def remove(self, artifacts: Iterable[Path]) -> None:
        sorted_artifacts = sorted(list(artifacts))
        with open(self.output_file, "w", encoding="utf-8") as f:
            if os.name == "nt":
                # For Windows, provide standard rm which works in git bash / wsl / etc.
                f.write("#!/bin/sh\n")
            else:
                f.write("#!/bin/sh\n")
            for artifact in sorted_artifacts:
                f.write(f'rm -rf "{artifact}"\n')
        print(f"\nCreated {self.output_file} with {len(sorted_artifacts)} commands.")
