from aws_cdk import aws_ec2 as ec2
from constructs import Construct

class ComputeConstruct(Construct):
    def __init__(self, scope: Construct, id: str, vpc: ec2.IVpc, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.instance = ec2.Instance(
            self, "CreditEC2Instance",
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.T2, ec2.InstanceSize.MICRO
            ),
            machine_image=ec2.MachineImage.latest_amazon_linux2023(),
            vpc=vpc,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC)
        )
