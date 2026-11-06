# Persediaan dan Jalankan

[English](Setup-and-Run) · [Dansk](Setup-and-Run-da) · **Bahasa Malaysia**

## Keperluan

Python 3.13 atau lebih baharu. Flask hanya diperlukan untuk kuliah web (tambahan `web` yang pilihan); pytest terdapat dalam tambahan `dev`.

## Cipta dan gunakan `.venv` setempat

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

macOS dan Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Jalankan pelayan

```bash
flask --app flask_day_54.presentation.hello run
python -m flask_day_54.presentation.hello
```

Buka `http://127.0.0.1:5000/` dan hentikan pelayan dengan `Ctrl+C`.

## Jalankan ujian

```bash
python -m pytest
```

## Apa yang kita peroleh

- Satu cara yang boleh diulang untuk bermula daripada salinan kerja yang bersih: `.venv` setempat, pip yang dikemas kini dan pemasangan boleh suntingan (editable).
- Dua cara untuk memulakan pelayan Flask, dan satu set ujian yang berjalan tanpa pelayar.
