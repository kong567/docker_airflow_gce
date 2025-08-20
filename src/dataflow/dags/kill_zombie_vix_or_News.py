from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from dataflow.etl.kill_zom import (
    # 建立並回傳一個 DockerOperator 任務
    clear_stuck_dag_runs_NEWS,
)
today = datetime.now().strftime('%Y%m%d')

with DAG(
    dag_id="maintenance_clear_stuck_runs_NEWS",
    start_date=days_ago(1),
    schedule_interval="50 23 * * *",  # 每 20 分鐘掃一次
    catchup=False,
    max_active_runs=1,
) as dag:   
    clear_stuck = PythonOperator(
    task_id=f"clear_stuck_dag_runs_NEWS_{today}",
    python_callable=clear_stuck_dag_runs_NEWS,
    queue = "All_crawler",
)