# Opsætning og kørsel

[English](Setup-and-Run) · **Dansk** · [Bahasa Malaysia](Setup-and-Run-ms)

## Krav

Python 3.13 eller nyere. Flask er kun nødvendigt til webforelæsningerne (det valgfrie tillæg `web`); pytest ligger i tillægget `dev`.

## Opret og brug et lokalt `.venv`

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

macOS og Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Kør serveren

```bash
flask --app flask_day_54.presentation.hello run
python -m flask_day_54.presentation.hello
```

Åbn `http://127.0.0.1:5000/` og stop serveren med `Ctrl+C`.

## Kør testene

```bash
python -m pytest
```

## Hvad vi fik ud af det

- Én gentagelig måde at starte på fra en ren udgave af koden: et lokalt `.venv`, en opdateret pip og en redigerbar installation.
- To måder at starte Flask-serveren på og en testsuite, der kører uden en browser.
