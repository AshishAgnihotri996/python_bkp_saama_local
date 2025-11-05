from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.email_operator import EmailOperator
from airflow.operators.empty import EmptyOperator
from airflow.operators.python_operator import PythonOperator, BranchPythonOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from airflow.sensors.time_delta import TimeDeltaSensor
from airflow.providers.amazon.aws.operators.glue import GlueJobOperator
from airflow.sensors.external_task_sensor import ExternalTaskSensor
from airflow.utils.state import State
from airflow.models import Variable
from datetime import datetime, timedelta
from airflow.models import TaskInstance
from airflow.models import DagRun
import sys
from csv import reader
import pendulum
import pandas as pd
import pytz
import boto3

runs_id = datetime.today().strftime('%Y%m%d%H%M%S')
print("run ID is generated for the DAG" + str(runs_id))
entity = "c3ae_mdi_daily_master_dag"
marker_name = "c3ae_mdi_daily_master_dag"
env_val = Variable.get("environment")
local_tz = pendulum.timezone("America/Los_Angeles")
pst_timezone = pytz.timezone('US/Pacific')

email_recipient = ['gcoi_mdi_ops-d@gene.com']
region_name = "us-west-2"

glue_iam_role = 'DMSCDC_Execution_Role'
num_dpu_medium = 10

seven_days_ago = datetime.combine(datetime.today() - timedelta(7), datetime.min.time())
department = ("USIX" if env_val == "dev" else "USIX-OPS")
environment = ''
if env_val == "qa":
    environment = "QA"
elif env_val == "dev":
    environment = "DEV"
else:
    environment = "PROD"

env_val = Variable.get("environment")
environment = ("DEV" if env_val == "dev" else "PROD")
dag_id = 'c3ae_mdi_daily_master_dag'

S3_BUCKET = f'cmg-oasis-{env_val}-c3ae-internal-datasources'
S3_PREFIX = 'common/inbound/mdi'


def check_s3_file(**kwargs):
    s3_client = boto3.client("s3")
    # List objects in the S3 folder
    try:
        response = s3_client.list_objects_v2(Bucket=S3_BUCKET, Prefix=S3_PREFIX)
        print(response)
        # Initialize file_exists flag
        file_exists = False
        if 'Contents' in response:
            # Iterate through the files and check if any ends with '_bad_records.csv'
            for content in response['Contents']:
                if content['Key'].split('/')[-1] != '~.xlsx':
                    print("went inside the first if statment")
                    if content['Key'].endswith('.csv') or content['Key'].endswith('.xlsx'):
                        print(f"Found matching file: {content['Key']}")
                        file_exists = True
                        break  # Stop once we find the first matching file
    except Exception as e:
        file_exists = False

    task_to_run = "c3ae_file_archive_mdi_dag" if file_exists else "Qlik_Publication_1"
    return task_to_run


default_args = {
    'owner': 'c3ae',
    'start_date': datetime(2024, 8, 6, tzinfo=local_tz),
    'email': email_recipient,
    'email_on_failure': True,
    'wait_for_downstream': True,
    'depends_on_past': True
}

# Task creation

with DAG(
        'c3ae_mdi_daily_master_dag',
        max_active_runs=1,
        default_args=default_args,
        # schedule_interval=None,
        schedule_interval="55 4-19/3 * * 1-5",
        catchup=False
) as dag:
    start = EmptyOperator(
        task_id='start',
        dag=dag
    )


    def execution_date_to_check(current_execution_date: datetime, context) -> datetime:
        dag_runs = DagRun.find(dag_id=dag_id)
        dag_runs.sort(key=lambda x: x.execution_date, reverse=True)
        print(dag_runs)
        # print(DagRun.get_previous_dagrun('privious_run_time_check_dag'))
        print(dag_runs[1].execution_date)
        privious_execution_date = dag_runs[1].execution_date
        return privious_execution_date


    wait_for_task_in_previous_run = ExternalTaskSensor(
        task_id='wait_for_task_in_previous_run',
        external_dag_id='c3ae_mdi_daily_master_dag',
        external_task_id='Build_Schedule_3',
        allowed_states=['success', 'skipped'],
        poke_interval=60,
        mode='poke',
        timeout=180,
        execution_date_fn=execution_date_to_check,
        dag=dag)

    check_s3_file = BranchPythonOperator(
        task_id="check_s3_file",
        python_callable=check_s3_file,
        dag=dag
    )

    c3ae_file_archive_mdi_dag = TriggerDagRunOperator(
        task_id="c3ae_file_archive_mdi_dag",
        trigger_dag_id="c3ae_file_archive_mdi_dag",
        wait_for_completion=True
    )

    Build_Schedule_1 = TriggerDagRunOperator(
        task_id="Build_Schedule_1",
        trigger_dag_id="foundry_build_call_dag",
        conf={"build_name": "MDI Build Schedule 1 | Prod Daily"},
        wait_for_completion=True
    )

    '''Build_Schedule_1 = EmptyOperator(
        task_id='Build_Schedule_1',
        dag=dag
    )'''

    c3ae_mdi_man_preprocess_master_dag = TriggerDagRunOperator(
        task_id="c3ae_mdi_man_preprocess_master_dag",
        trigger_dag_id="c3ae_mdi_man_preprocess_master_dag",
        wait_for_completion=True
    )

    c3ae_mdi_adj_master_dag = TriggerDagRunOperator(
        task_id="c3ae_mdi_adj_master_dag",
        trigger_dag_id="c3ae_mdi_adj_master_dag",
        wait_for_completion=True
    )

    c3ae_mdi_disputes_master_dag = TriggerDagRunOperator(
        task_id="c3ae_mdi_disputes_master_dag",
        trigger_dag_id="c3ae_mdi_disputes_master_dag",
        wait_for_completion=True
    )

    Build_Schedule_2 = TriggerDagRunOperator(
        task_id="Build_Schedule_2",
        trigger_dag_id="foundry_build_call_dag",
        conf={"build_name": "MDI Build Schedule 2 | Prod Daily"},
        wait_for_completion=True
    )

    c3ae_file_copy_and_athena_creation_mdi_dag = TriggerDagRunOperator(
        task_id="c3ae_file_copy_and_athena_creation_mdi_dag",
        trigger_dag_id="c3ae_file_copy_and_athena_creation_mdi_dag",
        wait_for_completion=True
    )

    c3ae_file_archive_mdi_stg_dag = TriggerDagRunOperator(
        task_id="c3ae_file_archive_mdi_stg_dag",
        trigger_dag_id="c3ae_file_archive_mdi_stg_dag",
        wait_for_completion=True
    )

    Build_Schedule_3 = TriggerDagRunOperator(
        task_id="Build_Schedule_3",
        trigger_dag_id="foundry_build_call_dag",
        conf={"build_name": "MDI Build Schedule 3 | Prod Daily"},
        wait_for_completion=True
    )

    MDI_Email_dag = TriggerDagRunOperator(
        task_id="MDI_Email_dag",
        trigger_dag_id="MDI_Email_dag",
        wait_for_completion=True
    )

    Qlik_Publication = GlueJobOperator(
        job_name='Qlik_Publication',
        region_name=region_name,
        iam_role_name=glue_iam_role,
        # script_args={
        #   '--s3globalConfigDQMPath': 's3://' + code_bucket + '/dags/mdm-inbound/common/mcmdm_inbound_dq_trigger.json'},
        num_of_dpus=num_dpu_medium,
        script_args={
            '--dag_name': dag_id
        },
        task_id='Qlik_Publication',
        dag=dag
    )

    Qlik_Publication_1 = GlueJobOperator(
        job_name='Qlik_Publication',
        region_name=region_name,
        iam_role_name=glue_iam_role,
        # script_args={
        #   '--s3globalConfigDQMPath': 's3://' + code_bucket + '/dags/mdm-inbound/common/mcmdm_inbound_dq_trigger.json'},
        num_of_dpus=num_dpu_medium,
        script_args={
            '--dag_name': dag_id
        },
        task_id='Qlik_Publication_1',
        dag=dag
    )

    send_success_email = EmailOperator(
        task_id='send_success_email',
        to=email_recipient,
        subject=f'{dag_id} Completed',
        html_content=f'No CLD,DISP AND ADJ file avaialble to process,The DAG {dag_id} has completed successfully  at {datetime.now(pst_timezone).strftime("%Y-%m-%d %H:%M:%S")}.',
        dag=dag
    )

    end = EmptyOperator(
        task_id='end',
        dag=dag
    )

# Dependencies create

check_s3_file >> [c3ae_file_archive_mdi_dag, Qlik_Publication_1]

start.set_downstream(wait_for_task_in_previous_run)

wait_for_task_in_previous_run.set_downstream(check_s3_file)

c3ae_file_archive_mdi_dag.set_downstream(Build_Schedule_1)
c3ae_file_archive_mdi_dag.set_downstream(c3ae_mdi_man_preprocess_master_dag)
c3ae_file_archive_mdi_dag.set_downstream(c3ae_mdi_adj_master_dag)
c3ae_file_archive_mdi_dag.set_downstream(c3ae_mdi_disputes_master_dag)

Build_Schedule_1.set_downstream(Build_Schedule_2)
c3ae_mdi_man_preprocess_master_dag.set_downstream(Build_Schedule_2)
c3ae_mdi_adj_master_dag.set_downstream(Build_Schedule_2)
c3ae_mdi_disputes_master_dag.set_downstream(Build_Schedule_2)

Build_Schedule_2.set_downstream(c3ae_file_copy_and_athena_creation_mdi_dag)
Build_Schedule_2.set_downstream(MDI_Email_dag)

c3ae_file_copy_and_athena_creation_mdi_dag.set_downstream(Qlik_Publication)
c3ae_file_copy_and_athena_creation_mdi_dag.set_downstream(c3ae_file_archive_mdi_stg_dag)

c3ae_file_archive_mdi_stg_dag.set_downstream(Build_Schedule_3)

Build_Schedule_3.set_downstream(end)
MDI_Email_dag.set_downstream(end)
Qlik_Publication.set_downstream(end)
Qlik_Publication_1.set_downstream(send_success_email)