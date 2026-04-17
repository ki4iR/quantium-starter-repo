#!/bin/bash

# - have to ryn pytest using the venv's Python directly
.venv/Scripts/python.exe -m pytest
TEST_RESULT=$?

if [ $TEST_RESULT -eq 0 ]; then
    echo "All tests passed."
    exit 0
else
    echo "Tests failed."
    exit 1
fi