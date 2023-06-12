import aws_cdk as cdk
from constructs import Construct
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep


class HelloCdkPipelineStack(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        synth_step = ShellStep("Synth",
                               input=CodePipelineSource.git_hub(repo_string="iapostol-69/hello-cdk",branch="master"))

        pipeline = CodePipeline(self,
                                "Pipeline",
                                pipeline_name="PipelineSameAccReg",
                                commands=["npm install -g aws-cdk", "python -m pip install -r requirements.txt", "cdk synth"])