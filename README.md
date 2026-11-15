\# DevOps Labs 



A collection of practical DevOps labs covering version control, CI/CD automation, containerization, orchestration, infrastructure automation, monitoring, and DevSecOps.



This repository documents the implementation of three labs, including configuration files, source code, execution evidence, and section-wise reports.



\## Repository Overview



| Lab | Focus Areas | Key Tools |

|---|---|---|

| \*\*Lab 1\*\* | Git, Python application, Jenkins CI/CD pipelines, automated testing | Git, GitHub, Python, Jenkins |

| \*\*Lab 2\*\* | Kubernetes deployment, rolling updates, rollback, scaling, Docker, storage, networking, CI/CD | Docker, Docker Compose, Kubernetes, Minikube, GitHub Actions |

| \*\*Lab 3\*\* | Configuration management, infrastructure provisioning, centralized logging, security scanning, monitoring, feature flags and testing | Ansible, Terraform, ELK Stack, Jenkins, Prometheus, Grafana, Selenium |



\## Project Structure



```text

DevOps-Labs/

│

├── Lab-1/

│   ├── DevOps\_Lab1\_Reports/

│   ├── Jenkinsfile

│   ├── app.py

│   ├── test\_app.py

│   └── requirements.txt

│

├── Lab-2/

│   ├── Configuration\_Files/

│   │   ├── CI\_CD/

│   │   ├── Docker/

│   │   └── Kubernetes/

│   ├── Reports/

│   └── Screenshots/

│

├── Lab-3/

│   ├── Section\_1\_Ansible/

│   ├── Section\_2\_Terraform/

│   ├── Section\_3\_ELK/

│   ├── Section\_4\_DevSecOps/

│   ├── Section\_5\_Prometheus\_Grafana/

│   ├── Section\_6\_FeatureFlags\_Testing/

│   ├── Section\_7\_Final\_Report/

│   ├── Reports/

│   └── screenshots/

│

└── .gitignore

```



\## Lab Details



\### Lab 1 – Git, Python and Jenkins CI/CD



\- Practiced Git initialization, configuration, commits, branching, merging, and pushing code to GitHub.

\- Developed a Python application with automated tests.

\- Installed and configured Jenkins.

\- Created a Jenkins pipeline using a `Jenkinsfile`.

\- Worked with pipeline stages, build execution, and console output.

\- Explored automated application testing and deployment workflows.



\### Lab 2 – Containerization and Kubernetes Orchestration



\- Built and ran Docker images and containers.

\- Worked with Docker image layers, container lifecycle management, and Docker Hub.

\- Used Docker Compose to manage multiple services.

\- Implemented persistent storage using volumes and bind mounts.

\- Configured Docker networks and tested container communication.

\- Deployed an NGINX application on Kubernetes using Minikube.

\- Practiced rolling updates, rollbacks, and deployment scaling.

\- Configured a CI/CD workflow using GitHub Actions and a self-hosted runner.



\### Lab 3 – Infrastructure Automation, Monitoring and DevSecOps



\- \*\*Ansible:\*\* Created playbooks and configured inventory for automation.

\- \*\*Terraform:\*\* Provisioned local resources using infrastructure-as-code.

\- \*\*ELK Stack:\*\* Set up Elasticsearch, Logstash, and Kibana for centralized logging.

\- \*\*DevSecOps:\*\* Integrated security scanning into a Jenkins pipeline.

\- \*\*Monitoring:\*\* Configured Prometheus and Grafana for monitoring and visualization.

\- \*\*Feature Flags and Testing:\*\* Implemented feature flag functionality and explored load testing and Selenium-based testing.



\## Getting Started



\### Prerequisites



Install the tools required for the lab you want to execute:



\- Git and GitHub

\- Python 3 and pip

\- Java and Jenkins

\- Docker Desktop and Docker Compose

\- kubectl and Minikube

\- Ansible

\- Terraform

\- A web browser



Some tools are only required for their respective sections. Ansible, for example, may require a compatible Linux or WSL environment.



\### Clone the Repository



```bash

git clone https://github.com/vishusehgal79/DevOps-Labs.git

cd DevOps-Labs

```



\## How to Run



The following commands provide the main execution steps. Run them from the specified lab directories.



\### 1. Lab 1 – Python Application and Tests



```bash

cd Lab-1

```



Create and activate a virtual environment (Windows PowerShell):



```powershell

python -m venv venv

.\\venv\\Scripts\\Activate.ps1

```



Install dependencies and run tests:



```bash

pip install -r requirements.txt

pytest

```



Run the application:



```bash

python app.py

```



To execute the CI/CD pipeline, configure Jenkins with the repository and use the `Lab-1/Jenkinsfile` as the pipeline definition.



\### 2. Lab 2 – Docker and Kubernetes



\*\*Docker\*\*



```powershell

cd Lab-2/Configuration\_Files/Docker

docker build -t lab2-nginx:v1 .

docker run -d --name lab2-nginx-container -p 8081:80 lab2-nginx:v1

```



Open `http://localhost:8081` to access the NGINX application.



\*\*Docker Compose\*\*



From the Docker configuration directory:



```bash

docker compose up -d

docker compose ps

docker compose down

```



\*\*Kubernetes with Minikube\*\*



Start the local cluster:



```bash

minikube start --driver=docker

```



Apply the deployment and service manifests:



```bash

cd ../Kubernetes

kubectl apply -f deployment.yaml

kubectl apply -f service.yaml

```



Verify the deployment:



```bash

kubectl get deployments

kubectl get pods

kubectl get services

```



Access the application:



```bash

minikube service nginx-service

```



Additional commands for rolling updates, rollback, and scaling:



```bash

kubectl set image deployment/nginx-deployment nginx=nginx:latest

kubectl rollout status deployment/nginx-deployment

kubectl rollout undo deployment/nginx-deployment

kubectl scale deployment/nginx-deployment --replicas=3

```



\### 3. Lab 3 – Automation, Infrastructure and Monitoring



\*\*Ansible\*\*



From `Lab-3/Section\_1\_Ansible`:



```bash

ansible-playbook -i inventory.ini site.yml

```



\*\*Terraform\*\*



From `Lab-3/Section\_2\_Terraform`:



```bash

terraform init

terraform plan

terraform apply

```



To remove the resources created by Terraform:



```bash

terraform destroy

```



\*\*ELK Stack\*\*



From `Lab-3/Section\_3\_ELK`:



```bash

docker compose up -d

docker compose ps

```



\*\*Prometheus and Grafana\*\*



From `Lab-3/Section\_5\_Prometheus\_Grafana`:



```bash

docker compose up -d

docker compose ps

```



\*\*Feature Flags and Testing\*\*



From `Lab-3/Section\_6\_FeatureFlags\_Testing`:



```bash

pip install -r requirements.txt

python app.py

pytest

```



The Jenkinsfile in the DevSecOps section can be used to configure the corresponding Jenkins pipeline.



> \*\*Note:\*\* Some services require additional configuration, environment variables, or tool-specific setup before execution. Refer to the configuration files and section-wise reports for details. Review resource definitions before running `terraform apply` or `terraform destroy`.



\## Documentation and Evidence



Each lab contains supporting documentation and execution evidence:



\- Section-wise reports describing the implementation.

\- Screenshots showing important configurations and successful executions.

\- YAML, Docker, Terraform, Ansible, Jenkins, and Python configuration files.



Refer to the respective lab folders for detailed steps and results.



\## Learning Outcomes



Through these labs, I gained practical experience with:



\- Git-based version control and collaborative workflows.

\- CI/CD pipeline creation and automation.

\- Docker containerization and Kubernetes orchestration.

\- Infrastructure automation using Ansible and Terraform.

\- Centralized logging and application monitoring.

\- DevSecOps practices and automated testing.

\- Managing and documenting end-to-end DevOps workflows.



\---



\*\*Repository:\*\* \[DevOps-Labs](https://github.com/vishusehgal79/DevOps-Labs)



