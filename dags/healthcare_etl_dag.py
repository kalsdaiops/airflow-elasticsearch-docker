from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from elasticsearch import Elasticsearch
import random

# Function to connect to Elasticsearch and index documents
def connect_to_elasticsearch(**kwargs):
    # Connect to Elasticsearch (assuming it runs on localhost)
    es = Elasticsearch(
        ['http://localhost:9200'],
        http_auth=('elastic', 'MVy7UGw7')  # Replace with your credentials
    )

    # Check if the connection is established
    if es.ping():
        print("Successfully connected to Elasticsearch")
    else:
        print("Failed to connect to Elasticsearch")
        return

    # Sample data (name, age, diagnosis, procedure, address, patient_id)
    sample_data = [
        {
            "name": "John Doe",
            "age": 34,
            "diagnosis": "Hypertension",
            "procedure": "Blood Pressure Check",
            "address": "123 Main St",
            "patient_id": "001"
        },
        {
            "name": "Jane Smith",
            "age": 28,
            "diagnosis": "Diabetes",
            "procedure": "Insulin Therapy",
            "address": "456 Oak St",
            "patient_id": "002"
        }
    ]

    # Index the data into Elasticsearch under the "healthcare_data" index
    # Create the index if it doesn't exist
    if not es.indices.exists(index=index_name):
        es.indices.create(index=index_name)

    # Index each record in sample data
    for record in sample_data:
        try:
            es.index(index=index_name, document=record)
            print(f"Successfully indexed document: {record}")
        except Exception as e:
            print(f"Error indexing document: {record}. Error: {str(e)}")


# Define the DAG
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2025, 2, 6),
}

dag = DAG(
    'elasticsearch_example_dag',
    default_args=default_args,
    description='A simple DAG to connect to Elasticsearch and index documents',
    schedule_interval='@once',  # This will run once
)

# Define the task
elasticsearch_task = PythonOperator(
    task_id='connect_and_index',
    python_callable=connect_to_elasticsearch,
    provide_context=True,
    dag=dag,
)

# No dependencies, as it's a simple one-task DAG
elasticsearch_task
