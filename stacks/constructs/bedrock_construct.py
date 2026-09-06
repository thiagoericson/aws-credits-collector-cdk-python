from aws_cdk import (
    custom_resources as cr,
    aws_iam as iam,
)
from constructs import Construct

class BedrockConstruct(Construct):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Chamada direta da API Converse do Bedrock no evento de 'onCreate'
        self.bedrock_trigger = cr.AwsCustomResource(
            self, "BedrockOnCreateTrigger",
            on_create=cr.AwsSdkCall(
                service="BedrockRuntime",
                action="converse",
                parameters={
                    "modelId": "us.amazon.nova-lite-v1:0",
                    "messages": [
                        {
                            "role": "user",
                            "content": [{"text": "Hello Bedrock on Stack Creation"}]
                        }
                    ]
                },
                physical_resource_id=cr.PhysicalResourceId.of("BedrockStackCreationTrigger")
            ),
            policy=cr.AwsCustomResourcePolicy.from_statements([
                iam.PolicyStatement(
                    actions=["bedrock:InvokeModel"],
                    resources=["*"]
                )
            ])
        )
