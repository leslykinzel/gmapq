#!/bin/sh

set -e

rm -rf dist/

poetry install
poetry build
pipx install dist/*.whl --force
