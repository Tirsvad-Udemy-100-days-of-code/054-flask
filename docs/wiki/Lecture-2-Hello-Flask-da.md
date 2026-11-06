# Forelæsning 2: Den første Flask-server

[English](Lecture-2-Hello-Flask) · **Dansk** · [Bahasa Malaysia](Lecture-2-Hello-Flask-ms)

![Forelæsning 2: Den første Flask-server](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/054-flask/raw/branch/main/docs/images/lecture-02.png)

## Hvad forelæsningen handler om

Et bibliotek bliver kaldt af din kode, men et framework kalder din kode og bestemmer strukturen. Forelæsningen opretter den mindste mulige Flask-applikation i en fil med navnet `hello.py` (aldrig `flask.py`, som ville skjule biblioteket), installerer Flask med `pip`, peger `FLASK_APP` på filen og starter serveren med `flask run`. Browseren viser derefter "Hello, World!" fra den lokale adresse. `Ctrl+C` stopper serveren, så to applikationer ikke kæmper om den samme port.

## Hvad vi fik ud af det

- Forskellen mellem et bibliotek og et framework.
- En fungerende webserver på seks linjer: `app = Flask(__name__)`, en rute til `/` og en funktion, der returnerer tekst.
- Hvordan `FLASK_APP` fortæller Flask, hvilken fil der skal køres.
- En vane med at teste ruten med Flasks testklient i stedet for en browser.

## I dette repository

Kode: `src/flask_day_54/presentation/hello.py` (ruten `hello_world`), use casen `application/get_greeting.py` og konstanten `GREETING`. Tests: `tests/e2e/test_hello_app.py`.
