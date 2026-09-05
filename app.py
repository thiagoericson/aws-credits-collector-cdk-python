#!/usr/bin/env python3
import os
import aws_cdk as cdk
from app_stack import AWS100CreditsStack

app = cdk.App()

AWS100CreditsStack(
    app, 
    "AWS100CreditsStack",
    # Passar o 'env' é essencial para que o 'ec2.Vpc.from_lookup' 
    # consiga buscar a VPC padrão da sua conta AWS durante o cdk synth/deploy.
    env=cdk.Environment(
        account=os.getenv("CDK_DEFAULT_ACCOUNT"),
        region=os.getenv("CDK_DEFAULT_REGION")
    )
)

app.synth()