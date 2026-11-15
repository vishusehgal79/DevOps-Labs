# DevOps Labs 

A practical collection of three DevOps labs demonstrating the implementation of version control, CI/CD pipelines, containerization, orchestration, infrastructure automation, monitoring, and DevSecOps practices.

This repository contains source code, configuration files, execution screenshots, and section-wise reports documenting the work completed in each lab.

## Project Overview

| Lab | Description | Technologies |
|---|---|---|
| **Lab 1 – Git & CI/CD** | Version control, Python application, automated testing, Jenkins pipelines | Git, GitHub, Python, Jenkins |
| **Lab 2 – Containerization & Kubernetes** | Docker images, containers, Compose, Kubernetes deployment, scaling, rollback and CI/CD | Docker, Docker Compose, Kubernetes, Minikube, GitHub Actions |
| **Lab 3 – Advanced DevOps** | Configuration management, infrastructure provisioning, logging, security, monitoring and testing | Ansible, Terraform, ELK, Jenkins, Prometheus, Grafana, Selenium |

## Repository Structure

```text
DevOps-Labs/
│
├── Lab-1/
│   ├── DevOps_Lab1_Reports/
│   ├── Jenkinsfile
│   ├── app.py
│   ├── test_app.py
│   └── requirements.txt
│
├── Lab-2/
│   ├── Configuration_Files/
│   │   ├── CI_CD/
│   │   ├── Docker/
│   │   └── Kubernetes/
│   ├── Reports/
│   └── Screenshots/
│
├── Lab-3/
│   ├── Section_1_Ansible/
│   ├── Section_2_Terraform/
│   ├── Section_3_ELK/
│   ├── Section_4_DevSecOps/
│   ├── Section_5_Prometheus_Grafana/
│   ├── Section_6_FeatureFlags_Testing/
│   ├── Section_7_Final_Report/
│   ├── Reports/
│   └── screenshots/
│
└── .gitignore
```

## Lab Implementations

### Lab 1 – Git, Python & Jenkins CI/CD

- Initialized and managed Git repositories.
- Practiced commits, branching, merging and GitHub integration.
- Developed a Python application with automated test cases.
- Installed and configured Jenkins.
- Created a Jenkins pipeline using a Jenkinsfile.
- Executed pipeline stages and verified builds through console output.

### Lab 2 – Containerization & Kubernetes Orchestration

- Built Docker images and managed container lifecycles.
- Worked with Docker Hub and image layers.
- Used Docker Compose to manage multiple services.
- Implemented persistent storage using volumes and bind mounts.
- Configured Docker networking and container communication.
- Deployed an NGINX application using Kubernetes and Minikube.
- Practiced rolling updates, rollbacks and deployment scaling.
- Configured a CI/CD workflow using GitHub Actions and a self-hosted runner.

### Lab 3 – Advanced DevOps & DevSecOps

- **Ansible:** Created playbooks and inventory configuration for automation.
- **Terraform:** Provisioned local resources using Infrastructure as Code.
- **ELK Stack:** Configured Elasticsearch, Logstash and Kibana for centralized logging.
- **DevSecOps:** Integrated security scanning into a Jenkins pipeline.
- **Monitoring:** Configured Prometheus and Grafana for monitoring and visualization.
- **Feature Flags & Testing:** Implemented feature flag functionality and explored load testing and Selenium-based testing.

## Getting Started

### Prerequisites

Install the tools required for the respective lab:

- Git and GitHub
- Python 3 and pip
- Java and Jenkins
- Docker Desktop and Docker Compose
- kubectl and Minikube
- Ansible
- Terraform

Some tools are required only for specific sections. Ansible commands may require a compatible Linux or WSL environment.

### Clone the Repository

```bash
git clone https://github.com/vishusehgal79/DevOps-Labs.git
cd DevOps-Labs
```

## How to Run

The following commands demonstrate the main execution steps for each lab.

### 1. Lab 1 – Python Application

```powershell
cd Lab-1

python -m venv venv
.\venv\Scripts\Activate.ps1

pip install -r requirements.txt
pytest
python app.py
```

To execute the CI/CD workflow, configure Jenkins with the repository and use the `Lab-1/Jenkinsfile` as the pipeline definition.

### 2. Lab 2 – Docker & Kubernetes

**Docker**

```powershell
cd Lab-2/Configuration_Files/Docker

docker build -t lab2-nginx:v1 .
docker run -d --name lab2-nginx-container -p 8081:80 lab2-nginx:v1
```

Access the application at `http://localhost:8081`.

**Docker Compose**

```powershell
docker compose up -d
docker compose ps
docker compose down
```

Run these commands from the Docker configuration directory.

**Kubernetes with Minikube**

```powershell
minikube start --driver=docker

cd ../Kubernetes

kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

kubectl get deployments
kubectl get pods
kubectl get services

minikube service nginx-service
```

**Deployment Management**

```powershell
kubectl rollout status deployment/nginx-deployment

kubectl rollout undo deployment/nginx-deployment

kubectl scale deployment/nginx-deployment --replicas=3
```

### 3. Lab 3 – Automation & Monitoring

**Ansible**

From `Lab-3/Section_1_Ansible`:

```bash
ansible-playbook -i inventory.ini site.yml
```

**Terraform**

From `Lab-3/Section_2_Terraform`:

```bash
terraform init
terraform plan
terraform apply
```

To remove the resources created by Terraform:

```bash
terraform destroy
```

**ELK Stack**

From `Lab-3/Section_3_ELK`:

```bash
docker compose up -d
docker compose ps
```

**Prometheus & Grafana**

From `Lab-3/Section_5_Prometheus_Grafana`:

```bash
docker compose up -d
docker compose ps
```

**Feature Flags & Testing**

From `Lab-3/Section_6_FeatureFlags_Testing`:

```bash
pip install -r requirements.txt
python app.py
pytest
```

For the DevSecOps section, configure the Jenkins pipeline using the `Jenkinsfile` provided in its section folder.

> **Note:** Run commands from the specified directories. Some services may require additional configuration before execution. Review the configuration files and section-wise reports before starting services or provisioning resources.

## Documentation & Evidence

Each lab includes supporting documentation and implementation evidence:

- Section-wise PDF and DOCX reports.
- Screenshots of configurations, commands and successful executions.
- Source code and configuration files.
- Deployment, testing and verification evidence.

Refer to the respective lab folders for detailed implementation steps.

## Key Learning Outcomes

- Version control and Git-based workflows.
- CI/CD pipeline creation and automation.
- Docker containerization and Kubernetes orchestration.
- Infrastructure as Code and configuration management.
- Centralized logging and application monitoring.
- DevSecOps integration and automated testing.
- Practical implementation and documentation of DevOps workflows.

---

**Repository:** [DevOps-Labs – GitHub](https://github.com/vishusehgal79/DevOps-Labs)

*Built as a hands-on implementation of DevOps tools, workflows and automation practices.*
