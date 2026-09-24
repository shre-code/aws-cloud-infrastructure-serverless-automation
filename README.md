# AWS Cloud Infrastructure & Serverless Automation Platform

An end-to-end AWS DevOps project that provisions cloud infrastructure with Terraform and deploys a serverless REST API using AWS Lambda, API Gateway, DynamoDB, S3, CloudWatch, and IAM.

## Architecture

Developer
  |
  v
GitHub
  |
  v
GitHub Actions
  |-----------------------------|
  | Terraform                    | Application
  v                              v
AWS Infrastructure          Lambda Package
  |                              |
  +--> VPC / IAM                 v
  +--> Lambda             API Gateway
  +--> API Gateway              |
  +--> DynamoDB                 v
  +--> S3                 AWS Lambda
  +--> CloudWatch               |
                              DynamoDB
                                |
                              CloudWatch

## Technology Stack

- AWS Lambda
- Amazon API Gateway
- Amazon DynamoDB
- Amazon S3
- Amazon CloudWatch
- AWS IAM
- Terraform
- Python
- GitHub Actions
- pytest
- AWS CloudWatch alarms

## What this project demonstrates

1. Infrastructure as Code with Terraform
2. Serverless application deployment
3. REST API with API Gateway and Lambda
4. DynamoDB persistence
5. S3 artifact storage
6. Least-privilege IAM policies
7. Automated Terraform validation and deployment
8. Automated Python unit tests
9. CloudWatch logging and alarms
10. Separate dev/prod environment structure

## Repository Structure

```text
aws-cloud-infrastructure-serverless-automation/
├── lambda/
│   ├── handler.py
│   └── requirements.txt
├── tests/
│   └── test_handler.py
├── terraform/
│   ├── modules/
│   │   ├── api/
│   │   ├── dynamodb/
│   │   ├── lambda/
│   │   ├── s3/
│   │   └── monitoring/
│   └── environments/
│       └── dev/
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── terraform.yml
├── scripts/
│   └── package_lambda.ps1
├── .gitignore
└── README.md
```

## Local validation

Install dependencies:

```bash
pip install pytest boto3
```

Run tests:

```bash
pytest
```

Validate Terraform:

```bash
cd terraform/environments/dev
terraform init
terraform fmt -recursive
terraform validate
terraform plan
```

## Deployment

Configure AWS authentication securely. For GitHub Actions, use GitHub OIDC with an AWS IAM role rather than storing long-lived AWS access keys.

Then:

```bash
terraform init
terraform plan
terraform apply
```

The Terraform configuration creates the Lambda function, API Gateway HTTP API, DynamoDB table, S3 bucket, IAM role/policies, and CloudWatch alarms.

## Security

Do not commit:

- AWS access keys
- secret keys
- `.env` files
- Terraform state
- Terraform variable files containing secrets
- Lambda ZIP artifacts
- private keys

Use IAM least privilege and GitHub OIDC for CI/CD.

## Production improvements

For a production implementation, add:

- Remote Terraform state in S3 with state locking
- Separate dev/staging/prod accounts
- Terraform modules with version pinning
- Manual approval for production
- API authentication with Cognito/JWT
- AWS WAF
- KMS encryption
- CloudTrail
- centralized logging
- dead-letter queues / destinations
- Lambda provisioned concurrency where required
- CloudWatch dashboards
