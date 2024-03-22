#!/bin/zsh

echo "Checking Python Dependencies..."
# Try to find pypy3 and python3
DEFAULT_PYTHON =""
if command -v python3 &>/dev/null; then
    DEFAULT_PYTHON="python3"
else
    echo "NO PYTHON ENVIRONMENT ON YOUR COMPUTER"
    echo "PLEASE SEE README.md FOR INSTRUCTIONS"
    exit
fi

echo "Installing Python Dependencies..."
$DEFAULT_PYTHON -m pip install -r requirements.txt