# Cosmos Hands-on

Welcome! This repo will provide you all in the information that you need to run Cosmos in Airflow 3.0! This example will
be full reproducible, and can be manipulated as each user sees fit.

## Prerequisites

The following prereq's must be met before following the steps below. For teams of multiple users, these pre-reqs are
really only applicable for a single team member.

* `gcloud` CLI
* `astro` CLI
* Access to create GCS buckets, BigQuery datasets and tables
* Access to create GCP service accounts
* Access to Astro


## Getting Up-and-running

### In GCP

1. Create a bucket called `carmichael_industries` in your GCP project.
2. Create a `raw/` folder in the `carmichael_industries` bucket. Add the `.csv` files in `include/dbt_data` into `raw/`.  
3. Create a dataset in BigQuery called `carmichael_industries`.
4. Create three new tables in the `carmichael_industries` dataset; `sale_items`, `transactions`, and 
   `transactions__sale_items` by "importing" from GCS. Auto-discover the schema.
5. Create a service account in GCP called `carmichael_industries`. Add the permissions "BigQuery Data Editor", 
   "BigQuery Job User", and "Storage Object Admin" to that service account. Make sure that your personal user has the
   permissions to impersonate, by providing it "Service Account Token Creator" permissions.


### Locally

1. Log in with the `gcloud` CLI using `gcloud auth login`.
2. Update the `docker-compose.override.yml` to point to your `gcloud` credentials.
3. Update your `GOOGLE_CLOUD_PROJECT` in the `.env` to your project ID.
4. Run `astro dev start`.
5. Once the Airflow UI has spun up, create a connection called `gcp_conn_id` of type `google_cloud_platform`. Don't add
   anything to this connection.
6. Turn on the `gcs_to_bigquery` and `sale_reporting` DAGs.

### In Astro

1. Create a new Astro Deployment called `cosmos-hands-on`.
2. In the "Details" tab of the `cosmos-hands-on` Deployment, copy the Workload Identity. Allow this Workload Identity
   to assume the `carmichael_industries` service account.
3. In the "Environment" tab of the `cosmos-hands-on` Deployment, create a variable called `GOOGLE_CLOUD_PROJECT` with
   your project ID.
4. Create a connection called `gcp_conn_id` of type `google_cloud_platform`. Don't add anything to this connection.
5. Turn on the `gcs_to_bigquery` and `sale_reporting` DAGs.
