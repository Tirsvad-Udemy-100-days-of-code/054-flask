import importlib

import pytest

flask = pytest.importorskip("flask")

from flask_day_54.infrastructure.constants import DEBUG, HOST, PORT  # noqa: E402


def test_main_runs_app_with_configured_host_port_and_debug(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from flask_day_54.presentation import hello

    calls: list[dict[str, object]] = []
    monkeypatch.setattr(hello.app, "run", lambda **kwargs: calls.append(kwargs))

    hello.main()

    assert calls == [{"host": HOST, "port": PORT, "debug": DEBUG}]


def test_importing_module_does_not_start_server(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from flask_day_54.presentation import hello

    calls: list[object] = []
    monkeypatch.setattr(flask.Flask, "run", lambda *args, **kwargs: calls.append(args))

    importlib.reload(hello)

    assert calls == []
