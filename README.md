# Hashenv Backend Server
[![Better Stack Badge](https://uptime.betterstack.com/status-badges/v1/monitor/2mh89.svg)](https://uptime.betterstack.com/?utm_source=status_badge)

Common server system for multiple services, handles requests and returns output at endpoints. 

## Requirements

- Python 3.11 or newer
- `requirements.txt` contains the needed Python dependencies

## Local setup

1. Create and activate a virtual environment:
   - PowerShell:
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```
   - Command Prompt:
     ```cmd
     python -m venv .venv
     .\.venv\Scripts\activate.bat
     ```
2. Upgrade pip:
   ```powershell
   python -m pip install --upgrade pip
   ```
3. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

## Configuration

Create a `.env` file in the project root or set environment variables before running the app. Example `.env` contents:

```env
HOST=127.0.0.1
PORT=3000
DEBUG=True
DATABASE_URL=your nosql database url here
```

## Run locally

Start the server with:

```powershell
python main.py
```

Then open your browser or API client:

- Root: `http://127.0.0.1:3000/`
- Health: `http://127.0.0.1:3000/health`
- Docs: `http://127.0.0.1:3000/docs`

## Example endpoints

- `GET /` returns project name, version, docs path, and status
- `GET /health` returns `{'status': 'ok'}`
- `POST /base` returns a simple hello payload
- `GET /sum?a=1&b=2` returns the sum of `a` and `b`

