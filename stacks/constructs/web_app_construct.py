from pathlib import Path
from aws_cdk import (
    aws_lambda as lambda_,
    aws_apigatewayv2 as apigw,
    aws_apigatewayv2_integrations as integrations,
)
from constructs import Construct

# Mapeia o caminho absoluto para a pasta 'src'
SRC_DIR = str(Path(__file__).parent.parent / "src")

class WebAppConstruct(Construct):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.web_app_lambda = lambda_.Function(
            self, "CreditWebAppLambda",
            runtime=lambda_.Runtime.PYTHON_3_11,
            handler="web_app.handler",
            code=lambda_.Code.from_asset(SRC_DIR),
        )

        self.http_api = apigw.HttpApi(
            self, "CreditWebAppApi",
            api_name="CreditWebAppApi"
        )

        self.http_api.add_routes(
            path="/",
            methods=[apigw.HttpMethod.GET],
            integration=integrations.HttpLambdaIntegration("LambdaIntegration", self.web_app_lambda)
        )
