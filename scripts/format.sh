#!/bin/sh -ex

# Sort imports one per line, so autoflake can remove unused imports
isort --force-single-line-imports pendo tests scripts

autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place pendo tests scripts --exclude=__init__.py
black pendo tests scripts
isort pendo tests scripts
