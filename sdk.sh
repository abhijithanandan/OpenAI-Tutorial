#!/bin/bash

# This script is used to setup the local development environment for open-AI SDK

python -m venv openai-env
source openai-env/bin/activate
pip install --upgrade openai

# Read the .env file

if [ -f .env ]; then
  export "$(cat .env | xargs)"
fi

# Set the OPENAI_API_KEY
export OPENAI_API_KEY=$OPENAI_API_KEY


