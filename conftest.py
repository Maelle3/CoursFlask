import pytest



from app import create_app

@pytest.fixture
def user_name():
    return "adrien"


@pytest.fixture
def app():
    app = create_app()
    return app