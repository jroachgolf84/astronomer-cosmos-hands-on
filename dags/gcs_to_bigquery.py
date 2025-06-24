"""
gcs_to_bigquery.py

Move data from GCS into BigQuery.
"""

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from airflow.sdk import Asset

from datetime import datetime, timedelta

import random


def _upstream_task():
    if random.randint(1, 10) > 7: raise Exception("Data is not ready!")


with DAG(
    dag_id="gcs_to_bigquery",
    start_date=datetime(2020, 1, 1),
    schedule=timedelta(minutes=75),
    catchup=False,
) as dag:
    # Create a list of Tasks used to move data from GCS to BigQuery
    _table_load_tasks: list[GCSToBigQueryOperator] = []

    upstream_task = PythonOperator(
        task_id="upstream_task",
        python_callable=_upstream_task,
    )

    for table_name in ["sale_items", "transactions", "transactions__sale_items"]:
        _table_load_tasks.append(
            GCSToBigQueryOperator(
                task_id=f"{table_name}_to_bigquery",
                bucket="carmichael_industries",
                source_objects=[f"raw/{table_name}.csv"],
                destination_project_dataset_table=f"carmichael_industries.{table_name}",
                write_disposition="WRITE_TRUNCATE",
                project_id="fe-demo-workloads",
                gcp_conn_id="gcp_conn_id",
                impersonation_chain="carmichael-industries-developm@fe-demo-workloads.iam.gserviceaccount.com",
                outlets=[Asset(f"{table_name}")],
            )
        )

    upstream_task >> _table_load_tasks
