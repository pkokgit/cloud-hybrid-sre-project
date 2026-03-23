# Cloud Hybrid SRE Project

## Overview
Hybrid AWS + Azure project demonstrating DevOps, SRE, and Security (SIEM).

## Phase 1
- Built Flask app
- Dockerized application
- Set up GitHub repo

## Phase 2
- AWS CLI works
- Docker image pushed to ECR
- EKS cluster created
- kubectl shows nodes

## Phase 3
- Docker container app deployed to EKS & running 
- EKS service LoadBalancer works
- Debugged any pod/image errors
- CloudTrail, CloudWatch, Guardrails, Budget working
- Costs under control

## Phase 4
- Azure CLI installed
- Azure Key Vault created
- Azure Secret stored
- Azure App identity created
- Azure Key Vault permissions set
- AWS app pulling Azure Secret successfully
### Achievement
- Hybrid cloud integration
- Cross-cloud secret retrieval
- Identity-based authentication

## Phase 5
- Docker image builds
- Image pushed to ECR
- Kubernetes deployment updated
- App redeployed in EKS
- Secrets remain safe (K8s Secrets)
### Achievement
- CI/CD pipeline (GitHub Actions)
- Automated deployment to EKS
- Secure secret handling
- Production-style DevOps workflow

## Phase 6
- Prometheus + Grafana
- To do:
- CloudTrail + GuardDuty → Sentinel
- SIEM integration
- Set up Prometheus / Grafana in EKS
- Connect logs from Flask app / pods
- Integrate AWS GuardDuty + CloudTrail logs into monitoring dashboard
- Optional: integrate Azure Monitor metrics
- Alerts / dashboards for SRE observability

## Phase 7 
- Remove test secrets from local / GitHub
- Document architecture, CI/CD workflow, secret management
- Prepare for interviews / showcase project

## Endpoints
- / -> main app
- /health -> health check
- /version -> version