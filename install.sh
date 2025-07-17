#!/bin/sh

set -e

poetry install
poetry build
pipx install dist/*.whl --force
