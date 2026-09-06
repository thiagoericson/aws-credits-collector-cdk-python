from aws_cdk import (
    RemovalPolicy,
    aws_ec2 as ec2,
    aws_rds as rds
)
from constructs import Construct

class DatabaseConstruct(Construct):
    def __init__(self, scope: Construct, id: str, vpc: ec2.IVpc, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.db_instance = rds.DatabaseInstance(
            self, "CreditRDSInstance",
            engine=rds.DatabaseInstanceEngine.postgres(
                version=rds.PostgresEngineVersion.VER_15
            ),
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.T3, ec2.InstanceSize.MICRO
            ),
            vpc=vpc,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
            publicly_accessible=True,
            allocated_storage=20,
            removal_policy=RemovalPolicy.DESTROY,
            delete_automated_backups=True,
        )
