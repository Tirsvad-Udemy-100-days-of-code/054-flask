## @file constants.py
#  @brief Constants of the domain layer.
"""Constants of the domain layer."""

from typing import Final

## @brief The greeting shown by the first Flask route.
GREETING: Final[str] = "Hello, World!"

## @brief Value of `__name__` when a file is executed directly.
MAIN_MODULE_NAME: Final[str] = "__main__"

## @brief Sentence shown when the file runs as the main program.
MAIN_PROGRAM_SENTENCE: Final[str] = (
    "Running as the main program: the file was executed directly"
)

## @brief Sentence template shown when the file is imported; `{name}` is the module.
IMPORTED_MODULE_SENTENCE: Final[str] = "Running as an imported module named {name}"

## @brief Warning shown for commands that remove data without asking.
NO_CONFIRMATION_WARNING: Final[str] = "No confirmation is asked - double-check the path"

## @brief Command line cheat sheet rows.
#  Each row is (name, purpose, Windows equivalent, is destructive, warning).
CLI_COMMANDS: Final[tuple[tuple[str, str, str, bool, str], ...]] = (
    ("pwd", "Print the current working directory", "cd", False, ""),
    ("ls", "List the files in a directory", "dir", False, ""),
    ("cd", "Change the current directory", "cd", False, ""),
    ("mkdir", "Create a new directory", "mkdir", False, ""),
    ("touch", "Create an empty file", "type nul > file", False, ""),
    ("rm", "Remove a file", "del file", True, NO_CONFIRMATION_WARNING),
    (
        "rm -rf",
        "Remove a directory and everything in it",
        "rmdir /s /q",
        True,
        NO_CONFIRMATION_WARNING,
    ),
)
