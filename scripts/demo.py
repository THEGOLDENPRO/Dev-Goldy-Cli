"""
Script for quick testing of the cli.
"""
import os
import sys
from pathlib import Path

# Little hack that forces this scripts to always use the dev goldy library from source.
#sys.path.insert(0, str(Path(os.path.split(__file__)[0]).parent))

from DevGoldy.cli import dev_goldy

dev_goldy()