#!/bin/bash

cd /home/ryan/lyecar

# Check if "venv" directory exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate the virtual environment
source venv/bin/activate