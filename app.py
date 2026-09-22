#!/usr/bin/env python3
import os
import aws_cdk as cdk
from stacks.credits_stack import CreditsStack

app = cdk.App()

CreditsStack(
    app, 
    "CreditsStack",
    env=cdk.Environment(
        account=os.getenv("CDK_DEFAULT_ACCOUNT"),
        region=os.getenv("CDK_DEFAULT_REGION")
    )
)

app.synth()