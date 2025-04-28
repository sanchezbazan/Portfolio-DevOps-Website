📦 Amazon (DevOps Cost Monitoring Dashboard)
📚 Table of Contents
About

High-Level DevOps Architecture

AWS Services Used

DevOps & Cloud Technologies

Deployment & CI/CD Pipeline

Setup Instructions

Environment Variables

Monitoring & Logging

Screenshots

Future Enhancements

Contact

🧠 About
Amazon is a full-stack DevOps-focused project designed to:

Automate retrieval of AWS billing/cost data (Cost Explorer)

Persist historical cost records into a backend (Django/PostgreSQL)

Expose APIs for React-based visualization

Practice AWS integration, containerization, automated deployments, and cost monitoring

Simulate a real-world cloud cost control dashboard

🏛️ High-Level DevOps Architecture
plaintext

React.js (frontend)
    |
Django REST API (backend)
    |
PostgreSQL Database (cost storage)
    |
AWS SDK (boto3) -> AWS Cost Explorer
    |
GitHub Actions CI/CD -> Docker Build -> EC2 Deployment (or ECS/Fargate future)

☁️ AWS Services Used

Service	Purpose
AWS Cost Explorer	Pull service-by-service and environment-tagged cost data
AWS S3	Optional: Resource listing and object storage examples
AWS IAM	Secure API access with scoped permissions
AWS EC2	Host the backend server (plan: move to ECS Fargate)
AWS CloudWatch (future)	Metrics collection and monitoring alerts

🛠️ DevOps & Cloud Technologies

Category	Tools
Infrastructure	AWS EC2, S3, Cost Explorer
Automation	Boto3 (AWS SDK), GitHub Actions
Backend	Django, Django REST Framework
Frontend	React.js
Containerization	Docker
Database	PostgreSQL (local dev), Amazon RDS (future)
Secrets Management	.env files locally, AWS Secrets Manager (future)
Monitoring	Planned integration: AWS CloudWatch Alarms, Logs

🚀 Deployment & CI/CD Pipeline
GitHub Actions Workflow (.github/workflows/deploy.yml)

Trigger: On push to main branch

Steps:

Run Django unit tests

Build Docker images for Django app and React app

Push Docker images to AWS Elastic Container Registry (ECR)

Deploy updated container on AWS EC2 or Fargate

Docker Compose for local development (backend + frontend)

Future enhancement: Terraform scripts for complete AWS infrastructure as code (ECS, ALB, ACM, Route53)

⚙️ Setup Instructions
Clone Repository


git clone https://github.com/sanchezbazan/DevOps-Portfolio.git
cd amazon-devops-dashboard

Setup Python Backend

poetry install
poetry shell
python manage.py migrate
python manage.py runserver

Setup React Frontend
cd frontend
npm install
npm run dev
(Optional) Build Docker locally
docker-compose up --build

🔑 Environment Variables

.env for Django backend:
AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
AWS_REGION=us-east-1
DJANGO_SECRET_KEY=your-django-secret
DATABASE_URL=your-database-url

.env for React frontend:
VITE_API_URL=http://localhost:8000

📈 Monitoring & Logging
Logging:

Django logs AWS API call results

Plan: Centralize logs into AWS CloudWatch Logs

Monitoring:

Plan: Integrate AWS CloudWatch Metrics (EC2 instance CPU, memory)

Plan: Build threshold alerts (e.g., if AWS costs exceed $100/day → trigger notification)

📸 Screenshots


🛠️ Future Enhancements
Add monthly AWS budget warnings and Slack/Email alerts

Build infrastructure with Terraform (ECS cluster, RDS database, Load Balancer)

Implement Kubernetes deployment using EKS

Add RBAC authentication (JWT-based user login) for dashboard access

Move to multi-account AWS support (Organizational Units)

📬 Contact
Brayan Sanchez Bazan



🧠 Summary for Hiring Managers:
✅ Full pipeline: Coding → Infrastructure → Deployment → Monitoring
✅ Hands-on AWS cost tracking and billing optimization
✅ Security-conscious with .env loading and secrets handling
✅ Dockerized architecture ready for cloud scaling
✅ Proactive future plans: CloudWatch monitoring, Terraform infra, Kubernetes containerization