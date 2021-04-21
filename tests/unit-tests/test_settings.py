from schema_reg_viz.config.settings import get_settings


def test_health():
    result = get_settings()

    assert result.schema_registry.port == 8081
    assert result.schema_registry.protocol == 'http'
    assert result.schema_registry.url == 'localhost'
