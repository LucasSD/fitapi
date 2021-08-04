"""One command to run Coverage"""
set -e  # Configure shell to exit if one command fails
coverage erase
coverage run -m pytest
coverage report