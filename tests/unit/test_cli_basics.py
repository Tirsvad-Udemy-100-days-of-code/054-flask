import pytest

from flask_day_54.domain.cli_basics import (
    describe_command,
    destructive_commands,
    format_cheat_sheet,
)


def test_describe_command_returns_windows_equivalent_when_known() -> None:
    assert describe_command("ls").windows_equivalent == "dir"
    assert describe_command("touch").windows_equivalent == "type nul > file"
    assert describe_command("pwd").windows_equivalent == "cd"


def test_describe_command_raises_value_error_when_unknown() -> None:
    with pytest.raises(ValueError, match="Unknown command: 'foo'"):
        describe_command("foo")


def test_destructive_commands_contains_only_rm_variants() -> None:
    names = {c.name for c in destructive_commands()}

    assert names == {"rm", "rm -rf"}


def test_recursive_remove_has_warning_and_windows_equivalent() -> None:
    command = describe_command("rm -rf")

    assert command.windows_equivalent == "rmdir /s /q"
    assert command.warning == "No confirmation is asked - double-check the path"


def test_format_cheat_sheet_lists_every_command_and_warns_on_rm() -> None:
    text = format_cheat_sheet()

    for name in ("pwd", "ls", "cd", "mkdir", "touch", "rm", "rm -rf"):
        assert name in text
    assert text.count("WARNING") == 2
