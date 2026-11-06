import pytest

flask = pytest.importorskip("flask")


def _client() -> "flask.testing.FlaskClient":
    from flask_day_54.presentation.hello import app

    return app.test_client()


def test_root_returns_greeting_when_get() -> None:
    response = _client().get("/")

    assert response.status_code == 200
    assert response.get_data(as_text=True) == "Hello, World!"


def test_unknown_path_returns_404() -> None:
    assert _client().get("/missing").status_code == 404


def test_root_content_type_is_html() -> None:
    response = _client().get("/")

    assert response.content_type.startswith("text/html")
