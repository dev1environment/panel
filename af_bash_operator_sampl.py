from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

with DAG("bash_operator_example", start_date=datetime(2023, 1, 1), schedule_interval="@daily") as dag:
    # Task 1: Run a Bash command
    run_bash_command_task = BashOperator(
        task_id="run_bash_command",
        bash_command="echo 'Hello, World!'"
    )

    # Task 2: Execute a Bash script
    run_bash_script_task = BashOperator(
        task_id="run_bash_script",
        bash_command="bash /path/to/script.sh"
    )

    # Task 3: Run a command with environment variables
    run_with_env_vars_task = BashOperator(
        task_id="run_with_env_vars",
        bash_command="my_command",
        env={'MY_VARIABLE': 'my_value'}
    )

    run_bash_command_task >> run_bash_script_task >> run_with_env_vars_task