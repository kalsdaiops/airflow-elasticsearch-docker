# Use official Airflow image
FROM apache/airflow:2.4.3-python3.8

# Set environment variables for Airflow user and group
ENV AIRFLOW_HOME=/opt/airflow

# Install Spark and Elasticsearch dependencies
RUN pip install --no-cache-dir \
    pyspark==3.1.2 \
    elasticsearch==7.10.0 \
    pandas

# Create a directory for the DAGs and copy them
COPY dags /opt/airflow/dags

# Set up entrypoint for Airflow
ENTRYPOINT ["bash", "-c", "airflow webserver & airflow scheduler"]
