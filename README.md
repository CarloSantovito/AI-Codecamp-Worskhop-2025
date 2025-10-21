# AI-Codecamp-Worskhop-2025

You’ll practice a plan → implement → test → review loop using AI assistants (Copilot, Gemini Code Assist, Gemini CLI).

## Prerequisites
- Python 3.11+
- Node 18+ (for Gemini CLI, optional)
- VS Code recommended (Python, Pytest, Black extensions)

### Python version
This workshop was tested with **Python 3.11 or newer**.

If `python --version` shows something older:
- **macOS / Linux:**  
  ```bash
  brew install python@3.11   # or sudo apt install python3.11


## Setup
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest -q
