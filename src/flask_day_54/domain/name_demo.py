## @file name_demo.py
#  @brief Lecture 4 demo of the `__name__ == "__main__"` check.
"""Shows whether a file runs as the main program or as an imported module."""

from flask_day_54.domain.constants import (
    IMPORTED_MODULE_SENTENCE,
    MAIN_MODULE_NAME,
    MAIN_PROGRAM_SENTENCE,
)


## @brief Describe how a module is running from its `__name__`.
#  @param name The value of `__name__`.
#  @return A short sentence.
def describe_name(name: str) -> str:
    """Return a sentence telling how the module with this name is running."""
    if name == MAIN_MODULE_NAME:
        return MAIN_PROGRAM_SENTENCE
    return IMPORTED_MODULE_SENTENCE.format(name=name)


## @brief Print the description of this module's own `__name__`.
def main() -> None:
    """Print how this file is running; the output is the demo's result."""
    print(describe_name(__name__))


if __name__ == "__main__":
    main()
