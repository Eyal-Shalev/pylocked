#!/usr/bin/env python3

from pathlib import Path
from sys import argv
from textwrap import dedent

from semver import VersionInfo

if __name__ == "__main__":
    assert len(argv) == 2
    ver = VersionInfo.parse(argv[1])
    assert ver.isvalid, f"{argv[1]} is not a valid semver version"

    file_path = Path(__file__)
    project_root = file_path.parent.parent.resolve()
    dst = (project_root / "pylocked" / "_version.py").resolve()
    assert dst.parent.exists() and dst.parent.is_dir(), f"{dst}"

    __tmpl = f"""
        # Generated by {file_path.relative_to(project_root)}. DO NOT EDIT!
        from typing import Final

        __version__: Final[str] = "{ver}"
    """
    dst.write_text(dedent(__tmpl).lstrip())
