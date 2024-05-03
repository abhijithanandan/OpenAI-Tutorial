#!/bin/bash

# This script is used to setup the local development environment for open-AI SDK

python -m venv openai-env
source openai-env/bin/activate
pip install --upgrade openai

# Read the .env file and set the environment variables

if [ -f .env ]; then
  export "$(cat .env | xargs)"
fi