# Lecture 4: __name__ and __main__

**English** · [Dansk](Lecture-4-Name-and-Main-da) · [Bahasa Malaysia](Lecture-4-Name-and-Main-ms)

![Lecture 4: __name__ and __main__](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/054-flask/raw/branch/main/docs/images/lecture-04.png)

## What the lecture covers

`__name__` is a built-in variable that holds the name of the current module. When a file is run directly Python sets it to `"__main__"`; when the file is imported it holds the module name. Checking `if __name__ == "__main__":` lets a file decide what runs only when it is the main program, for example `app.run()`. That gives a second way to start the Flask server, next to `flask run`, and it makes starting and stopping easy during development.

## What we gained

- The rule that code runs correctly whether a file is run or imported.
- A `main()` function in `hello.py` that is only called under the `__main__` check, so importing it never starts a server.
- A tested example (`describe_name`) that explains the two cases in words.

## In this repository

Code: `src/flask_day_54/presentation/hello.py` (`main`) and `src/flask_day_54/domain/name_demo.py`. Tests: `tests/unit/test_name_demo.py` and `tests/e2e/test_hello_main.py`.
