from g_ayush_sql_orch_airflow_jobs.utils import *

def Model_1():
    from airflow.operators.python import PythonOperator
    from datetime import timedelta
    import os
    import zipfile
    import tempfile

    return PythonOperator(
        task_id = "Model_1",
        python_callable = invoke_dbt_runner,
        op_kwargs = {
          "is_adhoc_run_from_same_project": False,
          "is_prophecy_managed": False,
          "run_deps": False,
          "run_seeds": True,
          "run_parents": False,
          "run_children": False,
          "run_tests": True,
          "run_mode": "model",
          "entity_kind": "model",
          "entity_name": "m1",
          "project_id": "64582",
          "git_entity": "branch",
          "git_entity_value": "dev2",
          "git_ssh_url": "https://github.com/ayushgupta128/prophecy_projects",
          "git_sub_path": "folder1",
          "select": "",
          "threads": "",
          "exclude": "",
          "run_props": "",
          "envs": {"DBT_DATABRICKS_INVOCATION_ENV" : "prophecy"}
        },
    )
