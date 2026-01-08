Flask REST API with Docker, Kubernetes, and Helm

📌 Overview
This project demonstrates a simple Flask REST API deployed using Docker, Kubernetes, and Helm.
It exposes a single endpoint /champions that returns sample JSON data.
The goal of this project is to showcase containerization, orchestration, and package management for cloud‑native applications.

🚀 Getting Started
1. Build Docker Image
docker build -t rest-api:1.0 .


2. Run Locally with Docker
docker run -p 8080:8080 rest-api:1.0


Test the API:
curl http://localhost:8080/champions


🐳 Deploy to Kubernetes (without Helm)
Apply manifests:
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml


Check resources:
kubectl get pods
kubectl get svc


Access API:
http://localhost:<NodePort>/champions


🎯 Deploy with Helm
Install chart:
helm install rest-api ./rest-api-chart


Check resources:
kubectl get pods
kubectl get svc


Access API:
http://localhost:<NodePort>/champions


📂 Project Structure
Matrix/
├── app.py                # Flask REST API
├── requirements.txt      # Python dependencies
├── Dockerfile            # Docker image definition
├── deployment.yaml       # Kubernetes Deployment manifest
├── service.yaml          # Kubernetes Service manifest
├── rest-api-chart/       # Helm chart
│   ├── Chart.yaml
│   ├── values.yaml
│   └── templates/
│       ├── deployment.yaml
│       └── service.yaml
└── README.md             # Project documentation


✨ Features
- Simple Flask REST API (/champions endpoint)
- Dockerized application
- Kubernetes manifests for Deployment and Service
- Helm chart for easy installation and management

📖 Example Output
Calling the endpoint:
curl http://localhost:8080/champions


Response:
[
  {"name": "Garen", "role": "Top"},
  {"name": "Ahri", "role": "Mid"},
  {"name": "Ezreal", "role": "ADC"}
]


📌 License
This project is for educational and portfolio purposes.
