from aws_cdk import (
    Stack,
    Duration,
    RemovalPolicy,
    aws_ec2 as ec2,
    aws_rds as rds,
    aws_budgets as budgets,
    aws_lambda as lambda_,
    aws_apigatewayv2 as apigw,
    aws_apigatewayv2_integrations as integrations,
    aws_iam as iam,
    custom_resources as cr,
)
from constructs import Construct

class AWS100CreditsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Usar a VPC default da conta
        vpc = ec2.Vpc.from_lookup(self, "DefaultVPC", is_default=True)

        # -------------------------------------------------------------
        # 1. Launch an instance using EC2 ($20)
        # -------------------------------------------------------------
        ec2_instance = ec2.Instance(
            self, "CreditEC2Instance",
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.T2, ec2.InstanceSize.MICRO
            ),
            machine_image=ec2.MachineImage.latest_amazon_linux2023(),
            vpc=vpc,
        )

        # -------------------------------------------------------------
        # 2. Set up a cost budget using AWS Budgets ($20)
        # -------------------------------------------------------------
        cost_budget = budgets.CfnBudget(
            self, "CreditCostBudget",
            budget=budgets.CfnBudget.BudgetDataProperty(
                budget_type="COST",
                time_unit="MONTHLY",
                budget_limit=budgets.CfnBudget.AmountProperty(
                    amount=10,
                    unit="USD"
                ),
                budget_name="CreditTrackerBudget"
            )
        )

        # -------------------------------------------------------------
        # 3. Create an Aurora or RDS database ($20)
        # -------------------------------------------------------------
        db_instance = rds.DatabaseInstance(
            self, "CreditRDSInstance",
            engine=rds.DatabaseInstanceEngine.postgres(
                version=rds.PostgresEngineVersion.VER_15
            ),
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.T3, ec2.InstanceSize.MICRO
            ),
            vpc=vpc,
            allocated_storage=20,
            removal_policy=RemovalPolicy.DESTROY,
            delete_automated_backups=True,
        )

        # -------------------------------------------------------------
        # 4. Create a web app using AWS Lambda ($20)
        # -------------------------------------------------------------
        web_app_lambda = lambda_.Function(
            self, "CreditWebAppLambda",
            runtime=lambda_.Runtime.PYTHON_3_11,
            handler="index.handler",
            code=lambda_.Code.from_inline(
                "def handler(event, context):\n"
                "    return {'statusCode': 200, 'body': 'Hello World from Lambda Web App!'}"
            ),
        )

        http_api = apigw.HttpApi(
            self, "CreditWebAppApi",
            api_name="CreditWebAppApi"
        )

        http_api.add_routes(
            path="/",
            methods=[apigw.HttpMethod.GET],
            integration=integrations.HttpLambdaIntegration("LambdaIntegration", web_app_lambda)
        )

        # -------------------------------------------------------------
        # 5. Use a foundation model in Amazon Bedrock ($20)
        # -------------------------------------------------------------
        # Lambda que faz a chamada ao Amazon Bedrock durante o deploy
        bedrock_caller = lambda_.Function(
            self, "CreditBedrockCaller",
            runtime=lambda_.Runtime.PYTHON_3_11,
            handler="index.handler",
            timeout=Duration.seconds(30),
            code=lambda_.Code.from_inline(
                "import boto3, json\n"
                "def handler(event, context):\n"
                "    if event.get('RequestType') == 'Delete':\n"
                "        return {'Status': 'SUCCESS'}\n"
                "    client = boto3.client('bedrock-runtime')\n"
                "    body = json.dumps({'prompt': 'Human: Hello\\nAssistant:', 'max_tokens_to_sample': 10})\n"
                "    try:\n"
                "        client.invoke_model(modelId='anthropic.claude-v2', body=body)\n"
                "    except Exception as e:\n"
                "        print(f'Bedrock call attempted: {e}')\n"
                "    return {'Status': 'SUCCESS'}\n"
            ),
        )

        bedrock_caller.add_to_role_policy(
            iam.PolicyStatement(
                actions=["bedrock:InvokeModel"],
                resources=["*"]
            )
        )

        # Provider que executa a Lambda do Bedrock no `cdk deploy`
        cr.Provider(
            self, "BedrockTriggerProvider",
            on_event_handler=bedrock_caller
        )