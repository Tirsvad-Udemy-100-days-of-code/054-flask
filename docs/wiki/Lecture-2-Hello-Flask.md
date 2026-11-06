# Lecture 2: The first Flask server

**English** · [Dansk](Lecture-2-Hello-Flask-da) · [Bahasa Malaysia](Lecture-2-Hello-Flask-ms)

![Lecture 2: The first Flask server](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/054-flask/raw/branch/main/docs/images/lecture-02.png)

## What the lecture covers

A library is called by your code, but a framework calls your code and decides the structure. The lecture creates the smallest Flask application in a file named `hello.py` (never `flask.py`, which would hide the library), installs Flask with `pip`, points `FLASK_APP` at the file and starts the server with `flask run`. The browser then shows "Hello, World!" from the local address. `Ctrl+C` stops the server so that two applications do not fight over the same port.

## What we gained

- The difference between a library and a framework.
- A working web server in six lines: `app = Flask(__name__)`, a route for `/` and a function that returns text.
- How `FLASK_APP` tells Flask which file to run.
- A habit of testing the route with Flask's test client instead of a browser.

## In this repository

Code: `src/flask_day_54/presentation/hello.py` (route `hello_world`), the use case `application/get_greeting.py` and the constant `GREETING`. Tests: `tests/e2e/test_hello_app.py`.
