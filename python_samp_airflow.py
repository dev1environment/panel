from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

# Define the default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 5, 21),
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}

# Create the DAG object
dag = DAG(
    'sample_dag',
    default_args=default_args,
    description='A simple DAG example',
    schedule_interval='@daily',
)

# Define a Python function to be executed by the PythonOperator
def print_message():
    print("Hello, Airflow!")

# Define the tasks
task1 = BashOperator(
    task_id='task1',
    bash_command='echo "Task 1"',
    dag=dag,
)

task2 = PythonOperator(
    task_id='task2',
    python_callable=print_message,
    dag=dag,
)

# Define the task dependencies
task1 >> task2
