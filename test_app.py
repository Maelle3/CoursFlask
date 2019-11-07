
from flask import Flask


#
# def test_app():
#     assert app is not None
#     assert isinstance(app, Flask)
#
#
# def test_index_route():
#     client = app.test_client()
#     response = client.get("/")
#     assert response.status_code == 200
#     assert "ECM" in response.data.decode("utf-8")
#
#
# def test_index_user():
#     client = app.test_client()
#     response = client.get("/user/adrien")
#     assert response.status_code == 200
#     result = response.data.decode("utf-8")
#     assert "Hello, adrien" in result
#
#
# def test_user_template():
#     client = app.test_client()
#     response = client.get("/user/adrien")
#     template = app.jinja_env.get_template('user.html')
#     assert template.render(name="adrien") == response.get_data(as_text=True)
from tasks.tests.factories import TaskFactory


def test_app(app):
    assert app is not None
    assert isinstance(app, Flask)


def test_index_route(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "ECM" in response.get_data(as_text=True)

def test_index_user(client, user_name):
    response = client.get(f"/user/{user_name}")
    assert response.status_code == 200
    assert f"Hello, {user_name}" in response.get_data(as_text=True)


def test_user_template(app, client, user_name):
    response = client.get(f"/user/{user_name}")
    template = app.jinja_env.get_template('user.html')
    assert template.render(name=user_name) == response.get_data(as_text=True)


def test_user_view_uses_correct_template(client, captured_templates, user_name):
    response = client.get(f"/user/{user_name}")
    assert len(captured_templates) == 1

    template, context = captured_templates[0]

    assert template.name == "user.html"

    assert "name" in context
    assert context["name"] == user_name


def test_professor_view(app, client):
    response = client.get("/professor")
    assert response.json["name"] == "Adrien"

def test_todoz(app, client, db_session):
    task = TaskFactory()
    db_session.commit()

    response = client.get("/todoz")
    assert len(response.json["results"]) > 0
