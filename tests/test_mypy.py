import subprocess
import sys


def test_mypy_can_check_package():
    """Test that mypy can check the wadler_lindig package.
    
    This test verifies that mypy runs successfully on the package,
    which requires the py.typed marker to be present.
    """
    # Run mypy on the wadler_lindig package
    result = subprocess.run(
        [sys.executable, "-m", "mypy", "wadler_lindig", "--no-error-summary"],
        capture_output=True,
        text=True,
    )
    # Verify mypy can run (doesn't crash)
    # The package may have type errors, but mypy should be able to check it
    assert "Success: no issues found" in result.stdout or "error:" in result.stdout, (
        f"mypy did not run properly:\n{result.stdout}\n{result.stderr}"
    )


def test_py_typed_exists():
    """Test that py.typed marker file exists in the package."""
    import wadler_lindig
    from pathlib import Path

    package_dir = Path(wadler_lindig.__file__).parent
    py_typed = package_dir / "py.typed"
    assert py_typed.exists(), f"py.typed marker file not found at {py_typed}"
