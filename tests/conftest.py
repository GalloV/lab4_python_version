"""
Pytest configuration file.
This runs before tests are collected and sets up the Python path.
"""
import sys
from pathlib import Path

# Add src directory to Python path
src_dir = Path(__file__).resolve().parent.parent / "src"
sys.path.insert(0, str(src_dir))