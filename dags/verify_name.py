from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'phidelist',
    'depends_on_past': False,
    'start_date': datetime(2023, 7, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'verify_my_name_dag',
    default_args=default_args,
    description='A DAG to verify if my name is phidelist',
    schedule_interval=timedelta(days=1),
)

start = DummyOperator(
    task_id='start',
    dag=dag,
)

def verify_name(name):
    if name == "phidelist":
        print("Name verified: phidelist")
    else:
        raise ValueError("Name verification failed: not phidelist")

verify_name_task = PythonOperator(
    task_id='verify_name_task',
    python_callable=verify_name,
    op_args=['phidelist'], 
    dag=dag,
)

process_data = DummyOperator(
    task_id='process_data',
    dag=dag,
)

save_results = DummyOperator(
    task_id='save_results',
    dag=dag,
)

send_notification = DummyOperator(
    task_id='send_notification',
    dag=dag,
)

end = DummyOperator(
    task_id='end',
    dag=dag,
)


start >> verify_name_task >> process_data >> save_results >> send_notification >> end
