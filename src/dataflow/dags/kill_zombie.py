from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

from dataflow.etl.kill_zom import (
    # 建立並回傳一個 DockerOperator 任務
    clear_stuck_dag_runs,
)


with DAG(
    dag_id="maintenance_clear_stuck_runs",
    start_date=days_ago(1),
    schedule_interval="*/20 * * * *",  # 每 20 分鐘掃一次
    catchup=False,
    max_active_runs=1,
) as dag:   
    clear_stuck = PythonOperator(
    task_id="clear_stuck_dag_runs",
    python_callable=clear_stuck_dag_runs,
)