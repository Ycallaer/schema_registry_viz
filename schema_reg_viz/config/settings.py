from pydantic import BaseModel
from functools import lru_cache
import os
import yaml


class SchemaRegistrySetting(BaseModel):
    url: str
    port: int
    protocol: str

    class Config:
        env_prefix = "POSTGRES_"


class Settings(BaseModel):
    schema_registry: SchemaRegistrySetting


@lru_cache()
def get_settings() -> Settings:
    """
    Loads the configuration settings file for a given environment into a Pydantic model
    :return:
    """
    settings_path = "schema_reg_viz/config/{}.yaml".format(
        os.getenv("SR_VIZ_ENV", "local")
    )

    with open(settings_path) as fp:
        result = yaml.safe_load(fp)
        settings = Settings.parse_obj(result[0])

    return settings
