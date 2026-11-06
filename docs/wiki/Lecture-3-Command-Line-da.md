# Forelæsning 3: Kommandolinjen

[English](Lecture-3-Command-Line) · **Dansk** · [Bahasa Malaysia](Lecture-3-Command-Line-ms)

![Forelæsning 3: Kommandolinjen](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/054-flask/raw/branch/main/docs/images/lecture-03.png)

## Hvad forelæsningen handler om

Terminalen taler med operativsystemets kerne (kernel) gennem skallen (shell) (en pistacienød: kernen er nødden, skallen er den ydre skal). Den giver udviklere kontrol og hastighed. Forelæsningen viser `pwd` (hvor er jeg), `ls` (hvad er her), `cd` (gå derhen), `mkdir` (ny mappe), `touch` (ny fil) og `rm` (slet). `rm -rf` fjerner en mappe og alt i den uden at spørge, så den kræver forsigtighed. Windows har lignende kommandoer: `cd`, `dir`, `type nul > file`, `del`, `rmdir /s /q`.

## Hvad vi fik ud af det

- De seks kommandoer, vi bruger hver dag til at bevæge os rundt og administrere filer.
- En tydelig advarsel om de to destruktive kommandoer, skrevet ind i koden som data.
- Selvtillid til at bruge terminalen i stedet for kun grafiske værktøjer.

## I dette repository

Kode: `src/flask_day_54/domain/cli_basics.py` angiver kommandoerne med deres Windows-former. Skærmbilledet viser rigtige kommandoer kørt i en midlertidig mappe. Tests: `tests/unit/test_cli_basics.py`.
