FROM astrocrpublic.azurecr.io/runtime:3.0-4

# Creation of a virtual environment to run dbt in
RUN python -m venv dbt_venv && source dbt_venv/bin/activate && \
    pip3 install --no-cache-dir dbt-bigquery && deactivate
