# Forelæsning 4: __name__ og __main__

[English](Lecture-4-Name-and-Main) · **Dansk** · [Bahasa Malaysia](Lecture-4-Name-and-Main-ms)

![Forelæsning 4: __name__ og __main__](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/054-flask/raw/branch/main/docs/images/lecture-04.png)

## Hvad forelæsningen handler om

`__name__` er en indbygget variabel, der indeholder navnet på det aktuelle modul. Når en fil køres direkte, sætter Python den til `"__main__"`; når filen importeres, indeholder den modulets navn. Med `if __name__ == "__main__":` kan en fil bestemme, hvad der kun kører, når den er hovedprogrammet, for eksempel `app.run()`. Det giver en anden måde at starte Flask-serveren på ved siden af `flask run`, og det gør det nemt at starte og stoppe under udvikling.

## Hvad vi fik ud af det

- Reglen om, at kode kører korrekt, uanset om en fil køres eller importeres.
- En `main()`-funktion i `hello.py`, der kun kaldes under `__main__`-tjekket, så import aldrig starter en server.
- Et testet eksempel (`describe_name`), der forklarer de to tilfælde med ord.

## I dette repository

Kode: `src/flask_day_54/presentation/hello.py` (`main`) og `src/flask_day_54/domain/name_demo.py`. Tests: `tests/unit/test_name_demo.py` og `tests/e2e/test_hello_main.py`.
