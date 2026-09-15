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



----

## Quick Start
```bash
# 0. After clone:
cd aws-cdk-bedrock-guardrail-enabler
```

### Virtual Env (.venv)

**- in macOS / Linux terminal:**
```bash
# 1. Create the virtual environment in the project directory, and activate the virtual environment
python3 -m venv .venv
source .venv/bin/activate
```

**- in Windows PowerShell:**
```powershell
# 1. Create the virtual environment in the project directory, and activate the virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Validation:** Upon successfully activating the environment, you will see the `(.venv)` prefix before the prompt in your terminal.

**- Then, in (.venv) in any terminal:**
```bash
# 2. Install project dependencies (AWS CDK, constructs, etc.)
python -m pip install --upgrade pip
pip install -r requirements.txt
```

**Deactivate the virtual environment:** When you finish development, simply type and run `deactivate` in any terminal.


### AWS CDK

```bash
# 3. Prepare the Account/Region (required only the first time)
cdk bootstrap aws://YOUR_AWS_ACCOUNT/YOUR_REGION

# 4. Synthesizes the infrastructure (checking the conversion from Python to CloudFormation)
cdk synth

# 5. Deploys the infrastructure
cdk deploy

# 6. Destroy resources (when necessary)
cdk destroy
```

**Prerequisites:** Needs `aws configure` already set up. If not, please, check the official AWS Docs: [Configuration and credential file settings in the AWS CLI](https://docs.aws.amazon.com/cli/v1/userguide/cli-configure-files.html)

## Author

**Thiago Ericson Cabral**
- [LinkedIn](https://www.linkedin.com/in/thiagoericson/)
- [Medium](https://medium.com/@thiagoericson)
- [AWS Builder Center](https://builder.aws.com/community/@thiagocabral)
- [Github](https://github.com/thiagoericson/)
- [DEV Community](https://dev.to/thiagocabral)

Let's connect!