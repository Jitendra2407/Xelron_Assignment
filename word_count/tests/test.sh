#!/bin/bash
set -e

# Install pytest
pip install pytest

# Run the test script
pytest /tests/test_outputs.py
