# Forelæsning 5: Funktioner som førsteklasses objekter

[English](Lecture-5-First-Class-Functions) · **Dansk** · [Bahasa Malaysia](Lecture-5-First-Class-Functions-ms)

![Forelæsning 5: Funktioner som førsteklasses objekter](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/054-flask/raw/branch/main/docs/images/lecture-05.png)

## Hvad forelæsningen handler om

I Python er en funktion et objekt ligesom et heltal eller en streng: den kan sendes som argument, defineres inde i en anden funktion og returneres fra den. Funktionen `calculate` tager to tal og en anden funktion (`add` eller `subtract`) og anvender den. En indlejret funktion kan kaldes af sin overordnede funktion, men ikke udefra. En funktion kan returnere en indlejret funktion, og den, der kalder, gemmer den i en variabel og kalder den senere. Værktøjet Python Tutor viser trinnene visuelt.

## Hvad vi fik ud af det

- Ideen bag dekoratører: en funktion, der modtager en funktion og returnerer en funktion.
- Reglen for scope ved indlejrede funktioner, bekræftet af en test af, at det indlejrede navn ikke kan nås udefra.
- Opgavens navne (`add`, `subtract`, `calculate`) i kode, som andre kursister kan læse og køre.

## I dette repository

Kode: `src/flask_day_54/domain/first_class_functions.py`. Tests: `tests/unit/test_first_class_functions.py`.
