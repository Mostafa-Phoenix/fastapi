#!/bin/bash
#
# This script displays a directory tree while excluding directories
# like .venv, .idx, and libraries.
#
# Usage: ./tree_script.sh [directory]
# If no directory is provided, it defaults to the current directory.

# Check if 'tree' is installed
if ! command -v tree &> /dev/null; then
    echo "Error: 'tree' command not found. Please install it first."
    exit 1
fi

# Use the first argument as the directory, default to current directory if not provided.
TARGET_DIR="${1:-.}"

# Exclude patterns: adjust as needed. The -I option accepts a pattern with
# names separated by | (pipe). Here we exclude .venv, .idx, and libraries directories.
EXCLUDE_PATTERN=".venv|.idx|libraries"

# Run tree with the exclusion pattern
tree -I "${EXCLUDE_PATTERN}" "${TARGET_DIR}"
