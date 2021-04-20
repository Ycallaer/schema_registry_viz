try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

__author__ = 'Yves callaert'

setup(
    name="schema_registry_viz",
    description="schema registry visualizer",
    version="0.0.1",
    packages=["schema_reg_viz", "schema_reg_viz.config", "schema_reg_viz.graph", "schema_reg_viz.json_logging", "schema_reg_viz.pydantic_models", "schema_reg_viz.schema_registry"],
    scripts=[],
    setup_requires=[],
    install_requires=[],
    dependency_links=[
    ]
)
