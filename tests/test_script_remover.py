"""
Tests for the ScriptRemover class.
"""

import io
import unittest
from pathlib import Path
from unittest.mock import patch

from remover.rm_output import ScriptRemover


class TestScriptRemover(unittest.TestCase):
    """Unit tests for ScriptRemover."""

    def setUp(self) -> None:
        self.remover = ScriptRemover()
        self.artifacts = [Path("build"), Path("dist"), Path("node_modules")]

    def test_remove_output_non_nt(self) -> None:
        """Test script generation on non-Windows platforms (includes shebang)."""
        # Force os.name to something other than 'nt' to check shebang
        with patch("os.name", "posix"):
            with patch("sys.stdout", new=io.StringIO()) as fake_out:
                result = self.remover.remove(self.artifacts)
                output = fake_out.getvalue()

        # Check shebang
        self.assertTrue(output.startswith("#!/bin/sh\n"))

        # Check rm commands (should be sorted)
        expected_commands = ['rm -rf "build"', 'rm -rf "dist"', 'rm -rf "node_modules"']
        for cmd in expected_commands:
            self.assertIn(cmd, output)

        # Check that they are in order (sorting)
        lines = [line for line in output.split("\n") if line.startswith("rm -rf")]
        self.assertEqual(lines, expected_commands)

        # Check result
        self.assertTrue(result.success)
        self.assertEqual(result.removed, sorted(self.artifacts))

    def test_remove_output_nt(self) -> None:
        """Test script generation on Windows (omits shebang)."""
        # Force os.name to 'nt' to check shebang omission
        with patch("os.name", "nt"):
            with patch("sys.stdout", new=io.StringIO()) as fake_out:
                result = self.remover.remove(self.artifacts)
                output = fake_out.getvalue()

        # Check shebang omission
        self.assertFalse(output.startswith("#!/bin/sh"))

        # Check rm commands
        expected_commands = ['rm -rf "build"', 'rm -rf "dist"', 'rm -rf "node_modules"']
        for cmd in expected_commands:
            self.assertIn(cmd, output)

        # Check result
        self.assertTrue(result.success)
        self.assertEqual(result.removed, sorted(self.artifacts))

    def test_remove_empty_list(self) -> None:
        """Test script generation with no artifacts."""
        with patch("sys.stdout", new=io.StringIO()) as fake_out:
            result = self.remover.remove([])
            output = fake_out.getvalue()

        # If no artifacts, it might still print shebang if not on NT
        # but no rm commands
        self.assertNotIn("rm -rf", output)
        self.assertTrue(result.success)
        self.assertEqual(result.removed, [])


if __name__ == "__main__":
    unittest.main()
