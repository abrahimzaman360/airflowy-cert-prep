"""
This is a DAG documentation specific to current DAG below!
"""

from airflow.sdk import Asset
from airflow.decorators import dag, task
from pendulum import datetime
from datetime import datetime as dt
import requests


@dag(
    dag_id="first_dag",
    dag_display_name="First DAG",
    start_date=datetime(2024, 1, 1),
    schedule="0/5 * * * *",  # run after every 5 seconds
    catchup=False,
    tags=["first_dag"],
    doc_md=__doc__,
)
def init_dag():
    @task(outlets=[Asset("first_asset_dag")])
    def get_info():
        res = requests.get("https://meowfacts.herokuapp.com", timeout=5)

        if res.status_code == 200:
            return {
                "fact": res.json()["data"][0],
                "timestamp": dt.now(),
            }
        else:
            return {"fact": "No fact found", "timestamp": dt.now()}

    @task()
    def print_info(info):
        print(info)
        print("This is big happiness!")

    # data sharing
    print_info(get_info())


dag = init_dag()
