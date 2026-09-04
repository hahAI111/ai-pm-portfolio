$ErrorActionPreference = "Stop"

python -m unittest discover -s "ai-seller-growth-copilot/app" -p "test_*.py"
python -m unittest discover -s "marketplace-opportunity-dashboard/app" -p "test_*.py"
python -m unittest discover -s "ai-seller-support-automation/app" -p "test_*.py"
