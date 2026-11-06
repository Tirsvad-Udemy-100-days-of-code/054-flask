## @file cli_basics.py
#  @brief Lecture 3 command line cheat sheet.
"""Command line cheat sheet with Windows equivalents."""

from dataclasses import dataclass

from flask_day_54.domain.constants import CLI_COMMANDS


## @brief One command of the cheat sheet.
@dataclass(frozen=True, slots=True)
class CommandInfo:
    """A shell command, its purpose, Windows equivalent and risk."""

    name: str
    purpose: str
    windows_equivalent: str
    is_destructive: bool
    warning: str


def _all_commands() -> tuple[CommandInfo, ...]:
    return tuple(CommandInfo(*row) for row in CLI_COMMANDS)


## @brief Look up one command by name.
#  @param name Command name such as "ls" or "rm -rf".
#  @return The command information.
#  @throws ValueError When the command is not in the cheat sheet.
def describe_command(name: str) -> CommandInfo:
    """Return the cheat sheet entry for a command name."""
    for command in _all_commands():
        if command.name == name:
            return command
    raise ValueError(f"Unknown command: {name!r}")


## @brief List the commands that remove data without asking.
def destructive_commands() -> tuple[CommandInfo, ...]:
    """Return the destructive commands."""
    return tuple(c for c in _all_commands() if c.is_destructive)


## @brief Format the cheat sheet as text, one command per line.
def format_cheat_sheet() -> str:
    """Return the cheat sheet as multi-line text."""
    lines: list[str] = []
    for command in _all_commands():
        line = (
            f"{command.name:<8} {command.purpose} "
            f"(Windows: {command.windows_equivalent})"
        )
        if command.is_destructive:
            line += f" WARNING: {command.warning}"
        lines.append(line)
    return "\n".join(lines)


## @brief Print the cheat sheet.
def main() -> None:
    """Print the cheat sheet; the output is the lecture's result."""
    print(format_cheat_sheet())


if __name__ == "__main__":
    main()
