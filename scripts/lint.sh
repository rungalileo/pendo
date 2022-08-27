#!/bin/sh -ex

mypy pendo tests
flake8 pendo tests
black pendo tests --check
isort pendo tests scripts --check-only
