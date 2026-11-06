# Lecture 5: Functions as first-class objects

**English** · [Dansk](Lecture-5-First-Class-Functions-da) · [Bahasa Malaysia](Lecture-5-First-Class-Functions-ms)

![Lecture 5: Functions as first-class objects](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/054-flask/raw/branch/main/docs/images/lecture-05.png)

## What the lecture covers

In Python a function is an object like an integer or a string: it can be passed as an argument, defined inside another function and returned from it. The `calculate` function takes two numbers and another function (`add` or `subtract`) and applies it. A nested function can be called by its parent but not from outside. A function can return a nested function, and the caller stores it in a variable and calls it later. The tool Python Tutor shows the steps visually.

## What we gained

- The idea behind decorators: a function that receives a function and returns a function.
- The scope rule for nested functions, confirmed by a test that the nested name is not reachable from outside.
- The assignment's names (`add`, `subtract`, `calculate`) in code that other course participants can read and run.

## In this repository

Code: `src/flask_day_54/domain/first_class_functions.py`. Tests: `tests/unit/test_first_class_functions.py`.
