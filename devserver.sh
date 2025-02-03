#!/bin/bash

# Activate the virtual environment
source .venv/bin/activate

# Check if the virtual environment was activated successfully
if [[ -z "$VIRTUAL_ENV" ]]; then
  echo "Error: Virtual environment activation failed."
  exit 1
fi

# Start the Uvicorn server with --reload
uvicorn app:app --reload --host 0.0.0.0 --port "$PORT"
