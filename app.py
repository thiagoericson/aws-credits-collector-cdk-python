#!/usr/bin/env python3
import os
import aws_cdk as cdk
from stacks.aws100usd_stack import AWS100USDStack

app = cdk.App()

AWS100USDStack(
    app, 
    "AWS100USDStack",
    env=cdk.Environment(
        account=os.getenv("CDK_DEFAULT_ACCOUNT"),
        region=os.getenv("CDK_DEFAULT_REGION")
    )
)

app.synth()