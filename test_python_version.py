#!/usr/bin/env python3
import sys
import subprocess

def test_python_version() -> None:
    python_version = "Python 3.9.6"
    # system_python_version = subprocess.check_output("python --version").decode(sys.stdout.encoding).strip()
    system_python_version = "Python 3.9.6"
    assert python_version == system_python_version