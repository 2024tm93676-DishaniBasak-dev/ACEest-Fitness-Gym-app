# ACEest Fitness & Gym – DevOps CI/CD Pipeline

## Project Overview

This project demonstrates an end-to-end DevOps implementation for a fitness application, covering the complete software delivery lifecycle from development to cloud deployment.

The project integrates modern DevOps tools and practices including:

* Flask-based application development
* Version control using Git & GitHub
* Automated testing using Pytest
* Continuous Integration using GitHub Actions
* Build validation using Jenkins
* Code quality analysis using SonarQube
* Containerization using Docker
* Container orchestration using Kubernetes
* Cloud deployment using AWS Elastic Kubernetes Service (EKS)
* Advanced deployment strategies (Rolling, Blue-Green, Canary, Shadow, A/B)

The objective is to simulate real-world software evolution and demonstrate automated CI/CD pipelines with scalable cloud deployment.

---

## System Architecture

The DevOps pipeline implemented in this project follows the workflow below:

Developer → GitHub Repository → GitHub Actions CI → Jenkins Pipeline → SonarQube Analysis → Docker Hub → AWS EKS → Kubernetes Deployment → LoadBalancer → End User

### Pipeline Flow

1. Developer pushes code to GitHub
2. GitHub Actions triggers CI pipeline
3. Dependencies are installed and tests are executed
4. Docker image is built
5. Jenkins pipeline validates build and runs tests
6. SonarQube performs static code analysis
7. Docker image is pushed to Docker Hub
8. Kubernetes (EKS) pulls image and deploys application
9. Application is exposed via AWS LoadBalancer

---

## Project Structure

```
ACEest-Fitness-Gym-app
│
├── app/                     # Flask application
├── test/                    # Unit tests
├── versions/                # Application evolution versions
│
├── k8s/                     # Kubernetes manifests
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── blue-deployment.yaml
│   ├── green-deployment.yaml
│   ├── canary-deployment.yaml
│   ├── shadow-deployment.yaml
│   ├── ab-deployment.yaml
│
├── .github/workflows/       # GitHub Actions CI pipeline
├── Dockerfile               # Container build file
├── Jenkinsfile              # Jenkins pipeline
├── sonar-project.properties # SonarQube config
├── requirements.txt         # Dependencies
├── README.md
└── .gitignore
```

---

## Technologies Used

| Technology     | Purpose                 |
| -------------- | ----------------------- |
| Python         | Application development |
| Flask          | Backend API             |
| Git & GitHub   | Version control         |
| Pytest         | Testing framework       |
| GitHub Actions | Continuous Integration  |
| Jenkins        | Build validation        |
| SonarQube      | Code quality analysis   |
| Docker         | Containerization        |
| Kubernetes     | Container orchestration |
| AWS EKS        | Cloud deployment        |

---

## Running the Application Locally

### Install Dependencies

```
pip install -r requirements.txt
```

### Run Application

```
python -m app.app
```

Application runs on:

```
http://localhost:5001
```

---

## Running Tests

```
pytest
```

---

## Docker Setup

### Build Image

```
docker build -t dishaniwilp/aceest-app:v1 .
```

### Push to Docker Hub

```
docker push dishaniwilp/aceest-app:v1
```

### Run Container

```
docker run -p 5001:5001 dishaniwilp/aceest-app:v1
```

---

## GitHub Actions (CI Pipeline)

Location:

```
.github/workflows/main.yml
```

Pipeline Steps:

* Checkout code
* Install dependencies
* Run tests
* Build Docker image

Ensures every commit is automatically validated.

---

## Jenkins Pipeline

Defined in:

```
Jenkinsfile
```

Pipeline Stages:

* Install Dependencies
* Run Tests
* SonarQube Analysis

Jenkins ensures build stability and quality checks.

---

## SonarQube Integration

SonarQube performs static code analysis to detect:

* Bugs
* Code smells
* Vulnerabilities
* Maintainability issues

Improves overall code quality before deployment.

---

## Kubernetes Deployment

### Apply Deployment

```
kubectl apply -f k8s/deployment.yaml
```

### Apply Service

```
kubectl apply -f k8s/service.yaml
```

Application is exposed using a LoadBalancer service.

---

## AWS EKS Deployment

The application is deployed on AWS Elastic Kubernetes Service (EKS).

Key steps:

* Cluster creation
* Node group configuration
* Application deployment
* LoadBalancer exposure

Access the application using:

```
http://<EXTERNAL-IP>:5000
```

---

## Deployment Strategies

### Rolling Deployment

Default Kubernetes update strategy ensuring zero downtime.

---

### Blue-Green Deployment

Two environments (blue & green) allow switching traffic between versions safely.

---

### Canary Deployment

New version is released to a small subset of users before full rollout.

---

### Shadow Deployment

New version runs in parallel without affecting production traffic.

---

### A/B Testing

Multiple versions run simultaneously for comparison and evaluation.

---

## Software Evolution

The project simulates real-world software evolution using multiple versions:

* v1.x – Initial implementation
* v2.x – Feature enhancements
* v3.x – Advanced optimizations

Each version demonstrates incremental development and CI validation.

---

## DevOps Outcomes

This project successfully demonstrates:

* End-to-end CI/CD pipeline
* Automated testing and validation
* Code quality integration
* Containerized deployments
* Kubernetes orchestration
* Cloud deployment using AWS EKS
* Implementation of multiple deployment strategies

---

## Rollback Capability

Rollback functionality was implemented using Kubernetes deployment revision control. The deployment history shows multiple revisions, allowing the system to revert to a previous stable version when required.

Commands used:

kubectl rollout history deployment aceest-app
kubectl rollout undo deployment aceest-app

This ensures zero downtime and reliability in case of deployment failures.

---

## Author

Dishani Basak

DevOps Assignment – Implementing Automated CI/CD Pipelines for ACEest Fitness & Gym
