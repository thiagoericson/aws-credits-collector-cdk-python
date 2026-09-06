#!/usr/bin/env python3
import os
import aws_cdk as cdk
from stacks.credits_stack import AWS100CreditsStack

app = cdk.App()

# Instancia a Stack passando a conta e região do ambiente
AWS100CreditsStack(
    app, 
    "AWS100CreditsStack",
    env=cdk.Environment(
        account=os.getenv("CDK_DEFAULT_ACCOUNT"),
        region=os.getenv("CDK_DEFAULT_REGION")
    )
)

app.synth()