
from flask import Flask

from app import app


def test_app():
    assert app is not None
    assert isinstance(app, Flask)


def test_index_route():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert "ECM" in response.data.decode("utf-8")


def test_user_template():
    client = app.test_client()
    response = client.get("/user/adrien")
    template = app.jinja_env.get_template('user.html')
    assert template.render(name="adrien") == response.get_data(as_text=True)