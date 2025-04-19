Write-Host "🧠 Setting up GitGPT in editable mode..."

# Create virtual environment if it doesn't exist
if (-not (Test-Path "venv")) {
    python -m venv venv
}

# Activate and install in editable mode
.\venv\Scripts\Activate.ps1
pip install -U pip
pip install -e .

Write-Host "✅ GitGPT is installed in editable mode."
Write-Host "Run it with: gitgpt"
