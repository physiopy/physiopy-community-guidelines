"""Just to get a version."""

import os, sys

sys.path.insert(0, os.path.abspath(os.path.pardir))
from _version import get_versions

__version__ = get_versions()["version"]
del get_versions
