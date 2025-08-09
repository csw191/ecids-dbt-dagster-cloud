from setuptools import find_packages, setup

setup(
    name="ecids_dbt_dagster_cloud",
    version="0.0.1",
    packages=find_packages(),
    package_data={
        "ecids_dbt_dagster_cloud": [
            "dbt-project/**/*",
        ],
    },
    install_requires=[
        "dagster",
        "dagster-cloud",
        "dagster-dbt",
        "dbt-core<1.11",
        "dbt-snowflake<1.11",
    ],
    extras_require={
        "dev": [
            "dagster-webserver",
        ]
    },
)

