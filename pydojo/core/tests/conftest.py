import pytest
from pydojo import create_app
from pydojo.config import TestConfig


@pytest.fixture
def app():
    app = create_app(TestConfig)
    return app
