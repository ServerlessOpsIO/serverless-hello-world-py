import os
import sys

# NOTE: Hack so we can test against local functions without installing them
# into the venv as pytest expects
#
# ref: https://github.com/pytest-dev/pytest/issues/2421#issuecomment-403724503
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

