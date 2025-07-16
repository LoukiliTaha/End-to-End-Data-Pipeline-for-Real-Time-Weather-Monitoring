# 🌦️ End-to-End-Data-Pipeline-for-Real-Time-Weather-Monitoring
An end-to-end data engineering project that collects real-time weather data, processes it with Spark Streaming, stores it in PostgreSQL, automates tasks with Airflow, and visualizes trends using Grafana.


📖 Project Overview :

This project demonstrates a scalable data engineering pipeline for ingesting and processing live weather data from the OpenWeatherMap API.
It automates data collection, transformation, storage, and visualization.

🛠️Tech Stack:

| Layer            | Tools Used                       |
| ---------------- | -------------------------------- |
| Ingestion        | Kafka Producer (OpenWeather API) |
| Processing       | Apache Spark Streaming           |
| Storage          | PostgreSQL                       |
| Orchestration    | Apache Airflow                   |
| Visualization    | Grafana + PostgreSQL             |
| Containerization | Docker, Docker Compose           |



🔁 Pipeline Workflow and Architecture Overview:

- Ingestion: Python Kafka producer pulls real-time weather data from OpenWeatherMap API.

- Streaming Processing: Spark Streaming consumes data, transforms temperature, humidity, wind data.

- Storage: Cleaned data is pushed into PostgreSQL.

- Visualization: Grafana queries PostgreSQL to display weather metrics.

- Automation: Airflow DAGs schedule producer jobs and health checks.



[Python Weather API Producer] ──> [Kafka Topic: weather_data]
                                       │
                                       ▼
                             [Spark Structured Streaming]
                                       │
                              transforms & cleans data
                                       ▼
                                [PostgreSQL Database]
                                       │
                              Grafana reads from here
                                       ▼
                                [Grafana Dashboards]

[Airflow] —> Optionally schedules Spark jobs, monitors pipelines, cleans data

All components are containerized and orchestrated via [Docker Compose]












