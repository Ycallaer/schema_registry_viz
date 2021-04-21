from schema_reg_viz.schema_registry.schema_reg import SchemaRegistry


def test_sr_endpoints():
    sr = SchemaRegistry(base_url="http://fakeurl:8080")

    assert sr.get_protocol() == "http"
    assert sr.get_schema_by_id_url(schema_id=1) == "http://fakeurl:8080/schemas/ids/1/"
