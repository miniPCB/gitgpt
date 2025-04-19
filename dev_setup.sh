#!/bin/bash
echo "🧠 Setting up GitGPT in editable mode..."

# Create venv if needed
if [ ! -d "venv" ]; then
  python3 -m venv venv
fi

# Activate venv and install in editable mode
source venv/bin/activate
pip install -U pip
pip install -e .

echo "✅ GitGPT is installed in editable mode."
echo "Run it with: gitgpt"
