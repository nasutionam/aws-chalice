from chalice import Chalice
import os
import boto3

AMI = os.environ['AMI']
INSTANCE_TYPE = os.environ['INSTANCE_TYPE']
KEY_NAME = os.environ['KEY_NAME']
SUBNET_ID = os.environ['SUBNET_ID']

ec2 = boto3.resource('ec2')

app = Chalice(app_name='create-ec2')

@app.lambda_function(name='create-ec2')
def create_ec2(event, context):
    instance = ec2.create_instances(
        BlockDeviceMappings=[
            {
                'DeviceName': '/dev/xvda',
                'Ebs': {
                    'DeleteOnTermination': True,
                    'VolumeSize': 123,
                    'VolumeType': 'gp3',
                    'Encrypted': True
                },
            },
        ],
        ImageId=AMI,
        InstanceType=INSTANCE_TYPE,
        KeyName=KEY_NAME,
        SubnetId=SUBNET_ID,
        MaxCount=1,
        MinCount=1,
    )

    print("New instance created: ", instance[0].id)

# docs terkait
# https://codeflex.co/boto3-create-ec2-with-tags/
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html
