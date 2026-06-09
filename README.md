# Task Management API Platform

A production-ready Task Management API built with FastAPI and PostgreSQL, designed to demonstrate modern DevOps and SRE practices including containerization, Kubernetes deployment, Infrastructure as Code, CI/CD automation, monitoring, and observability.

## Features

* Create, update, delete, and manage tasks
* RESTful API design using FastAPI
* PostgreSQL database integration
* Input validation and error handling
* Environment-based configuration management
* Health check endpoints
* Production-ready deployment architecture

## Technology Stack

### Application

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy

### DevOps & Infrastructure

* Docker
* Kubernetes (AKS)
* Terraform
* GitHub Actions
* Linux

### Monitoring & Observability

* Prometheus
* Grafana

## Architecture

Client → FastAPI Application → PostgreSQL Database

Application → Prometheus Metrics → Grafana Dashboards

GitHub Actions → Docker Build → Kubernetes Deployment

Terraform → Infrastructure Provisioning

## Project Structure

task-management-api/
├── app/
├── tests/
├── terraform/
├── kubernetes/
├── monitoring/
├── .github/workflows/
├── Dockerfile
├── requirements.txt
└── README.md

## Key Implementations

* Containerized application using Docker
* Kubernetes deployment with health probes
* Infrastructure provisioning using Terraform
* Automated CI/CD pipeline using GitHub Actions
* Prometheus metrics collection
* Grafana dashboards for monitoring and visualization
* Alerting for application and infrastructure health

## API Endpoints

| Method | Endpoint    | Description    |
| ------ | ----------- | -------------- |
| GET    | /tasks      | Get all tasks  |
| GET    | /tasks/{id} | Get task by ID |
| POST   | /tasks      | Create task    |
| PUT    | /tasks/{id} | Update task    |
| DELETE | /tasks/{id} | Delete task    |
| GET    | /health     | Health check   |

## Monitoring

The project includes:

* Application metrics
* Request latency monitoring
* Error rate tracking
* Resource utilization monitoring
* Kubernetes workload monitoring
* Dashboard visualization using Grafana

## Future Enhancements

* Authentication and Authorization (JWT)
* Redis Caching
* Horizontal Pod Autoscaling (HPA)
* Centralized Logging
* Multi-environment Deployment Strategy

## Learning Outcomes

This project demonstrates practical experience with:

* FastAPI Development
* Docker Containerization
* Kubernetes Deployment
* Infrastructure as Code (Terraform)
* CI/CD Automation
* Monitoring and Observability
* DevOps Best Practices
* Site Reliability Engineering (SRE) Concepts
