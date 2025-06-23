"""
raw_to_gold.py

Move data from a "raw" state in GCS to report-ready dataset.
"""

from airflow import DAG
from airflow.sdk import Asset

from cosmos import ProfileConfig, ProjectConfig, ExecutionConfig, DbtTaskGroup
from cosmos.profiles import GoogleCloudOauthProfileMapping

from datetime import datetime

import os

# Create the BigQuery
carmichael_industries_profile_config: ProfileConfig = ProfileConfig(
    profile_name="carmichael_industries_profile_config",
    target_name="default",  # No specific target
    profile_mapping=GoogleCloudOauthProfileMapping(
        conn_id="gcp_conn_id",
        profile_args={
            "project": "fe-demo-workloads",
            "dataset": "carmichael_industries",
        }
    ),
)

# Create other dbt-level config
DBT_PROJECT_PATH: str = f"{os.environ['AIRFLOW_HOME']}/dags/dbt/sales_reporting"  # Pointing to mounted path
DBT_EXECUTABLE_PATH = f"{os.environ['AIRFLOW_HOME']}/dbt_venv/bin/dbt"


with DAG(
    dag_id="sales_reporting",
    start_date=datetime(2020, 1, 1),
    schedule=[
        Asset("sale_items"),
        Asset("transactions"),
        Asset("transactions__sale_items")
    ],
    catchup=False,
) as dag:

    sales_reporting = DbtTaskGroup(
        group_id="transform_data",
        project_config=ProjectConfig(DBT_PROJECT_PATH),
        profile_config=carmichael_industries_profile_config,
        execution_config=ExecutionConfig(dbt_executable_path=DBT_EXECUTABLE_PATH)
    )

    sales_reporting
