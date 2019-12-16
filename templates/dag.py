{% include 'common.py' %}

dag = DAG('{{platform.env}}_{{project.name}}',max_active_runs=1, catchup=False, default_args=default_args, schedule_interval='{{cron.value}}')


job = BashOperator(
    task_id='job',
    bash_command= " ",
    env={
	},
    dag=dag)

