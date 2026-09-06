from aws_cdk import Stack, aws_ec2 as ec2
from constructs import Construct

# Importações relativas corrigidas
from .constructs.compute_construct import ComputeConstruct
from .constructs.database_construct import DatabaseConstruct
from .constructs.budget_construct import BudgetConstruct
from .constructs.web_app_construct import WebAppConstruct
from .constructs.bedrock_construct import BedrockConstruct

class AWS100CreditsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc.from_lookup(self, "DefaultVPC", is_default=True)

        ComputeConstruct(self, "ComputeModule", vpc=vpc)
        DatabaseConstruct(self, "DatabaseModule", vpc=vpc)
        BudgetConstruct(self, "BudgetModule")
        WebAppConstruct(self, "WebAppModule")
        BedrockConstruct(self, "BedrockModule")
