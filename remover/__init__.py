"""
Build artifact removers.
"""

from .base_delete import BaseRemover
from .direct_delete import DirectRemover
from .rm_output import ScriptRemover

__all__ = ["BaseRemover", "DirectRemover", "ScriptRemover"]
