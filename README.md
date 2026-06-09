## Key Highlights

- End-to-end containerized application deployment
- Hands-on with Podman (Docker alternative)
- Practical cloud deployment using AWS Free Tier
- Demonstrates platform engineering fundamentals

# flask-postgres-containerized-app

Flask PostgreSQL App (Containerized with Podman)  This project demonstrates a production-like setup of a Flask application  connected to PostgreSQL, containerized using Podman and deployed on AWS EC2.

## Problem Statement

Modern applications require consistent deployment environments and scalable 
database integration. This project demonstrates how to:

- Containerize an application using Podman
- Enable communication between application and database containers
- Deploy the setup on a cloud environment (AWS EC2)

## Architecture

GitHub Repo
     ↓
Local Machine (Podman)
     ↓
-------------------------
|  Flask Container      |
|  PostgreSQL Container |
-------------------------
     ↓
AWS EC2 Deployment

## Tech Stack

- Backend: Flask (Python)
- Database: PostgreSQL
- Containerization: Podman
- Cloud: AWS EC2

## Features

- Create user records
- Retrieve user data
- Environment-based configuration
- Containerized deployment
- Cloud deployment on AWS

## Project Structure

.
├── app/
│   ├── app.py
│   └── db.py
├── Containerfile
├── requirements.txt
└── README.md

## How to Run

### 1. Clone the repository
git clone <repo-url>
cd repo

### 2. Build container image
podman build -t flask-app .

### 3. Create network
podman network create mynet

### 4. Run PostgreSQL container
podman run -d --name postgres-db --network mynet \
-e POSTGRES_USER=admin \
-e POSTGRES_PASSWORD=admin \
-e POSTGRES_DB=mydb postgres

### 5. Run Flask app
podman run -d --name flask-app --network mynet -p 5000:5000 \
-e DB_HOST=postgres-db \
-e DB_USER=admin \
-e DB_PASS=admin \
-e DB_NAME=mydb flask-app

## API Endpoints

POST /users → Add user  
GET /users → Fetch all users

## AWS Deployment

1. Launch EC2 instance (Ubuntu)
2. Install Podman
3. Pull image from DockerHub
4. Run containers (same commands as local)
5. Access via: http://<ec2-ip>:5000

## Challenges

- Container networking: applications cannot use localhost
- Managing environment variables securely
- Ensuring database container is ready before app starts

## Learnings

- Understood container networking using Podman
- Learned how services communicate via container names
- Hands-on experience in deploying apps to AWS EC2
- Improved debugging skills in container-based setups

## Future Improvements

- Add CI/CD pipeline using GitHub Actions
- Deploy using Kubernetes
- Add monitoring with Prometheus & Grafana