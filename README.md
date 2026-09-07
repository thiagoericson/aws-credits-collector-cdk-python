# The 100 USD AWS CDK Stack - Python

This project provisions, using AWS CDK (Python), the infrastructure required to meet the 5 requirements of the **Explore AWS / Earn AWS Credits** dashboard and unlock up to **$100 USD in AWS credits**.

Of course, you can do it using console. But, don't be boring, enjoy the learning.

## Prerequisites

- Python 3.9+ with an active virtual environment (`.venv`) and installed dependencies (`pip install -r requirements.txt`)
- AWS CLI installed and authenticated (`aws configure`)
- AWS CDK CLI installed (`npm install -g aws-cdk`)

## Quick Start (Deploy)

```bash
# 1. CDK bootstrapping (Only on the first run per account/region)
cdk bootstrap aws://<your-account-id>/<region>

# 2. Synthesize and validate the infrastructure
cdk synth

# 3. Deploy all resources
cdk deploy

# 4. Cleaning the environment
cdk destroy
```

## Milestones coverage

| Task | Provisoned Resource | Award |
| --- | --- | --- |
| **Launch an instance using EC2** | EC2 instance (`t2.micro`) in the default VPC | $20 USD |
| **Set up a cost budget using AWS Budgets** | Monthly cost budget in AWS Budgets | $20 USD |
| **Create an Aurora or RDS database** | RDS PostgreSQL instance (`t3.micro`) | $20 USD |
| **Create a web app using AWS Lambda** | AWS Lambda + HTTP API Gateway | $20 USD |
| **Use a foundation model in Amazon Bedrock** | Custom Resource (Lambda + `boto3`) invoking a Bedrock model | $20 USD |

> Note: Could take up to 24 hours to get update the status of milestones.

### Amazon Bedrock's milestone
AWS is not recognizing Bedrock API call to check the milestone related to it yet, I keep the code for learning purpose only. 

For that: Console > Amazon Bedrock -> Test -> Playground -> Select model -> Write any prompt -> Run -> Done (got yours 20USD)

## Disclaimer

⚠️ Be aware that AWS usage could be charge.