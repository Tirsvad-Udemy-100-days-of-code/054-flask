# Setup and Run

**English** · [Dansk](Setup-and-Run-da) · [Bahasa Malaysia](Setup-and-Run-ms)

## Requirements

Python 3.13 or newer. Flask is only needed for the web lectures (the optional `web` extra); pytest is in the `dev` extra.

## Create and use a local `.venv`

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

macOS and Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Run the server

```bash
flask --app flask_day_54.presentation.hello run
python -m flask_day_54.presentation.hello
```

Open `http://127.0.0.1:5000/` and stop the server with `Ctrl+C`.

## Run the tests

```bash
python -m pytest
```

## What we gained

- One repeatable way to start from a clean checkout: a local `.venv`, an upgraded pip and an editable install.
- Two ways to start the Flask server, and a test suite that runs without a browser.
