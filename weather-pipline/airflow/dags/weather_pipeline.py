from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG("weather_pipeline", start_date=datetime(2023, 1, 1), schedule_interval="*/5 * * * *", catchup=False) as dag:
    run_spark = BashOperator(
        task_id="run_spark",
        bash_command="spark-submit /opt/spark/consumer.py"
    )