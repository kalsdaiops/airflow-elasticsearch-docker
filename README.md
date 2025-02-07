# Airflow Elasticsearch Docker Setup

This repository contains a Dockerized setup for Apache Airflow that connects to an Elasticsearch instance. It provides an easy-to-use environment for running Airflow tasks with Elasticsearch integration.

## Project Overview

- **Airflow**: A platform to programmatically author, schedule, and monitor workflows.
- **Elasticsearch**: A distributed, RESTful search and analytics engine.
- **Docker**: Used to containerize both Apache Airflow and Elasticsearch to ensure easy deployment and scalability.

## Features

- Dockerized environment for both Airflow and Elasticsearch.
- Pre-configured connections for integrating Airflow with Elasticsearch.
- Example DAG to interact with Elasticsearch.
  
## Prerequisites

- Docker: [Install Docker](https://www.docker.com/get-started)
- Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/)

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/kalsdaiops/airflow-elasticsearch-docker.git
cd airflow-elasticsearch-docker

## Step 2: Set up the Docker Environment
To build and start the services defined in docker-compose.yml, run:

bash
Copy
docker-compose up -d
This will:

Start Airflow web server on http://localhost:8080
Start Elasticsearch on http://localhost:9200

## Step 3: Access the Airflow UI
Once the containers are up, navigate to the Airflow web UI:

URL: http://localhost:8080
Username: airflow
Password: airflow
Step 4: Verify Elasticsearch Connection
Once the Airflow UI is running, you can check if the example DAG is connecting to Elasticsearch by checking the logs in the Airflow UI or by verifying data indexing in Elasticsearch.

Usage
Running the Example DAG
The example DAG in this setup demonstrates how to connect to Elasticsearch and index sample data. You can run the DAG through the Airflow UI.

Stopping the Docker Containers
To stop the running containers:

bash
Copy
docker-compose down
