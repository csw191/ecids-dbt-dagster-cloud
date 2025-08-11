from dagster import Definitions
from dagster_dbt import DbtCliResource
from .assets import ecids_test_dbt_assets
from .project import ecids_test_project
from .schedules import schedules

defs = Definitions(
    assets=[ecids_test_dbt_assets],
    schedules=schedules,
    resources={
        "dbt": DbtCliResource(project_dir=ecids_test_project),
    },
)

