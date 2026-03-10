# ACEest Fitness & Gym – DevOps CI/CD Pipeline

## Project Overview

This project demonstrates the implementation of a complete **DevOps lifecycle** including:

- Application development using **Flask**
- Version control using **Git & GitHub**
- Automated testing using **Pytest**
- Containerization using **Docker**
- Continuous Integration using **GitHub Actions**
- Build validation using **Jenkins**

The objective is to simulate the **software evolution of a real-world application** while automating the build and testing workflow through CI/CD pipelines.

---

# System Architecture

The DevOps workflow implemented in this project follows the pipeline below:

```
Developer pushes code
        ↓
GitHub Repository
        ↓
GitHub Actions CI Pipeline
        ↓
Install dependencies
Run automated tests
Build Docker image
        ↓
Jenkins Build Pipeline
        ↓
Run automated tests again
Validate application build

```

This architecture ensures **continuous integration and automated validation** for every code change.

---

# Project Structure

```
ACEest-Fitness-Gym-app
│
├── app/
│   ├── __init__.py
│   ├── app.py
│   ├── routes.py
│   └── services.py
│
├── test/
│   └── test_app.py
│
├── versions/
│   ├── Aceestver-1.0.py
│   ├── Aceestver-1.1.py
│   ├── Aceestver-1.1.2.py
│   ├── Aceestver-2.0.1.py
│   ├── Aceestver-2.1.2.py
│   ├── Aceestver-2.2.1.py
│   ├── Aceestver-2.2.4.py
│   ├── Aceestver-3.0.1.py
│   ├── Aceestver-3.1.2.py
│   └── Aceestver-3.2.4.py
│
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
├── README.md
└── .github/workflows/main.yml
```

---

# Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core application development |
| Flask | Backend API service |
| Git & GitHub | Version control |
| Pytest | Automated testing |
| Docker | Containerization |
| GitHub Actions | CI pipeline automation |
| Jenkins | Build validation pipeline |

---

# Running the Application Locally

## Install Dependencies

```
pip install -r requirements.txt
```

---

## Run the Flask Application

```
python -m app.app
```

The application will run on:

```
http://localhost:5001
```

---

# Running Unit Tests

Automated tests are implemented using **Pytest**.

Run:

```
pytest
```

Example output:

```
3 passed in 0.11s
```

---

# Running the Application with Docker

## Build Docker Image

```
docker build -t aceest-app .
```

## Run Docker Container

```
docker run -p 5001:5001 aceest-app
```

The application will be available at:

```
http://localhost:5001
```

---

# Continuous Integration (GitHub Actions)

The CI pipeline automatically runs whenever code is pushed to the repository.

Workflow file location:

```
.github/workflows/main.yml
```

Pipeline stages include:

1. Checkout repository
2. Install dependencies
3. Run unit tests
4. Build Docker image

This ensures that every commit is automatically validated.

---

# Jenkins Build Pipeline

A Jenkins pipeline is implemented using the **Jenkinsfile**.

Pipeline stages include:

```
Install Dependencies
Run Tests
```

Jenkins automatically pulls the repository and validates the build process.

---

# Software Evolution Simulation

Multiple versions of the ACEest application were provided to simulate **real software evolution**.

Versions include:

```
v1.0 Initial version
v1.1 Feature enhancements
v1.1.2 Bug fixes
v2.x Database integration and analytics
v3.x Advanced tracking and optimization
```

Each version was committed sequentially to demonstrate **continuous integration behavior**.

---

# DevOps Outcomes

This project demonstrates:

- Continuous Integration
- Automated testing pipelines
- Containerized application deployment
- Build validation with Jenkins
- Realistic software version evolution

The pipeline ensures that every change is **automatically tested and validated**, improving reliability and development efficiency.

---

# Author

**Dishani Basak**

DevOps Assignment – Implementing Automated CI/CD Pipelines for ACEest Fitness & Gym
