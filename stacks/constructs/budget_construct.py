from aws_cdk import aws_budgets as budgets
from constructs import Construct

class BudgetConstruct(Construct):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.cost_budget = budgets.CfnBudget(
            self, "CreditCostBudget",
            budget={
                "budgetType": "COST",
                "timeUnit": "MONTHLY",
                "budgetLimit": {"amount": 10, "unit": "USD"},
                "budgetName": "CreditTrackerBudget"
            }
        )
