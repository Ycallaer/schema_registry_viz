from starlette.testclient import TestClient
from schema_reg_viz.main import app
import pytest
from fastapi import Depends



@pytest.fixture(scope="session")
def init_test_client(pytestconfig):
    return TestClient(app)


def test_graph_call(init_test_client):
    response = init_test_client.post(
        "/viz_topic",
        data='{"subjectname": "google%2fprotobuf%2fdescriptor.proto"}'
    )

    assert response.status_code == 200