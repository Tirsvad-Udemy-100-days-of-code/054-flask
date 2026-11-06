# Forelæsning 6: Dekoratører og @-syntaksen

[English](Lecture-6-Decorators) · **Dansk** · [Bahasa Malaysia](Lecture-6-Decorators-ms)

![Forelæsning 6: Dekoratører og @-syntaksen](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/054-flask/raw/branch/main/docs/images/lecture-06.png)

## Hvad forelæsningen handler om

En dekoratør tilføjer adfærd til en eksisterende funktion uden at redigere den. Forelæsningen opsummerer først førsteklasses funktioner samt indlejring og returnering af funktioner og introducerer derefter `@`-syntaksen: at skrive `@make_bold` over en funktion er det samme som `say_hello = make_bold(say_hello)`. Flask bruger den samme idé til sine ruter: `@app.route("/")`. Med `functools.wraps` beholder den indpakkede funktion sit navn.

## Hvad vi fik ud af det

- `@`-syntaksen som genvej til at sende en funktion til en wrapper.
- Stabling af dekoratører: den nærmest funktionen kører først, så `@make_bold @make_emphasis @make_underlined` giver `<b><em><u>...</u></em></b>`.
- En forståelse af, hvad `@app.route("/")` gør i de næste forelæsninger.

## I dette repository

Kode: `src/flask_day_54/domain/decorators.py`. Tests: `tests/unit/test_decorators.py`.
