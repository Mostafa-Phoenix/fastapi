#!/bin/bash

# Activate the virtual environment
source .venv/bin/activate

# Check if the virtual environment was activated successfully
if [[ -z "$VIRTUAL_ENV" ]]; then
  echo "Error: Virtual environment activation failed."
  exit 1
fi

# Start the Uvicorn server with --reload
uvicorn app:app --reload --host 0.0.0.0 --port "$PORT" &

# Instructions on how to make the port public in Project IDX
echo "========================================================="
echo "1. The backend server is running on port: $PORT"
echo "2. Open the 'IDX' panel (left sidebar)."
echo "3. Expand the 'Backend Ports' section."
echo "4. Find port $PORT in the list."
echo "5. Click the 'lock' icon next to the port to 'Make Public'."
echo "6. use the created url to make connection with the frontend"
echo "========================================================="

wait
