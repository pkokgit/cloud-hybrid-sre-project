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


## Endpoints
- / -> main app
- /health -> health check
- /version -> version