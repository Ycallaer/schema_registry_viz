from schema_reg_viz.graph.graph_vizualiser import do_url_request
import pytest
from requests.exceptions import ConnectionError


def test_failing_url_request():
    with pytest.raises(ConnectionError):
        result = do_url_request(request_url='http://localhost:9999', sr_protocol='http')
