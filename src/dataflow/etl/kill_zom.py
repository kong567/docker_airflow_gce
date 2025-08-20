from airflow.models import DagRun
from airflow.utils.state import State
from datetime import datetime, timedelta
from airflow.utils.session import provide_session

@provide_session
def clear_stuck_dag_runs(session=None, **kwargs):
    stuck_runs = (
        session.query(DagRun)
        .filter(DagRun.state == State.RUNNING)
        .filter(DagRun.execution_date < datetime.utcnow() - timedelta(minutes=30))
        .all()
    )
    for run in stuck_runs:
        print(f"Clearing stuck DAG: {run.dag_id}, run: {run.execution_date}")
        run.set_state(State.FAILED)
    session.commit()

