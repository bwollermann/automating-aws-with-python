# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation')
ec2 = session.resource('ec2')
key_name = 'python_automation_key'
key_path = key_name + '.pem'
img = ec2.Image('ami-0d8f6eb4f641ef691')
ami_name = 'amzn2-ami-hvm-2.0.20190618-x86_64-gp2'
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key_name)
inst = instances[0]
inst.public_dns_name
inst.wait_until_running()
inst.reload()
inst.public_dns_name
session2 = boto3.Session(profile_name='pythonAutomation')
client = session2.resource('ec2')
client.execute_policy(AutoScalingGroupName='Notifon Example Group', PolicyName='Scale Up')
client = session2.resource('autoscaling')
client = session2.client('autoscaling')
client.execute_policy(AutoScalingGroupName='Notifon Example Group', PolicyName='Scale Up')
client.execute_policy(AutoScalingGroupName='Notifon Example Group', PolicyName='Scale Up')
import boto3
session = boto3.Session(profile_name='pythonAutomation')
as_client = session.client('autoscaling')
as_client.describe_auto_scaling_groups
as_client.describe_auto_scaling_groups()
as_client.describe_policies()
as_client.execute_policy(AutoScalingGroupName='Notifon Example Group', PolicyName='Scale Up')
