import aws_cdk as cdk
from constructs import Construct
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep
import aws_cdk.aws_iam as iam


class HelloCdkPipelineStack(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        synth_step = ShellStep("Synth",
                               input=CodePipelineSource.git_hub(repo_string="iapostol-69/hello-cdk", branch="master"),
                               commands=["npm install -g aws-cdk",
                                         "python -m pip install -r requirements.txt",
                                         "cdk synth",
                                         "cdk deploy --require-approval never"])

        pipeline = CodePipeline(self,
                                "Pipeline",
                                pipeline_name="HelloCdkPipeline",
                                synth=synth_step)

        # role = iam.Role(self, "CFRole", assumed_by=iam.ServicePrincipal("codepipeline.amazonaws.com"))
        # role.add_to_policy(iam.PolicyStatement(actions=["cloudformation:*"],
        #                                        effect=iam.Effect.ALLOW,
        #                                        resources=["*"]))


