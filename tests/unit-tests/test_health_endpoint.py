import os


from starlette.testclient import TestClient
from schema_reg_viz.main import app
import pytest


@pytest.fixture(scope="session")
def init_test_client(pytestconfig):
    return TestClient(app)


def test_health(init_test_client):
    response = init_test_client.get("/health")
    result = response.json()
    assert response.status_code == 200
    assert result["app_name"] == "schema registry viz"