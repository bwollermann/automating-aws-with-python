# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation')
ec2 = session.resource('ec2')
key_name='python_automation_key'
key_path = key_name + '.pem'
key = ec2.create_key_pair(KeyName=key_name)
key.key_material
with open(key_path, 'w') as key_file:
    key_file.write(key.key_material)
    
get_ipython().run_line_magic('ls', '-l python_automation_key.pem')
import os, stat
os.chmod(key_path, stat.S_IRUSR | stat.S_IWUSR)
get_ipython().run_line_magic('ls', '-l python_automation_key.pem')
ec2.images.filter(Owners=['amazon'])
list(ec2.images.filter(Owners=['amazon']))
len(list(ec2.images.filter(Owners=['amazon'])))
img = ec2.Image('ami-0d8f6eb4f641ef691')
img.name
ec2_apse2 = session.resource('ec2', region_name='ap_southeast-2')
ec2_apse2 = session.resource('ec2', region_name='ap-southeast-2')
img_apse2 = ec2_apse2.Image('ami-0d8f6eb4f641ef691')
img_apse2.name
img.name
ami_name = 'amzn2-ami-hvm-2.0.20190618-x86_64-gp2'
filters = [{'Name': 'name', 'Values': [ami_name]}]
list(ec2.images.filter(Owners=['amazon'], Filters=filters))
list(ec2_apse2.images.filter(Owners=['amazon'], Filters=filters))
img
key
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstancType='t2.micro', KeyName=key.key_name)
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
inst = instances[0]
inst.terminate()
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
inst = instances[0]
inst.public_dns_name
inst.public_dns_name
inst.public_dns_name
inst.public_dns_name
inst.wait_until_running()
inst.public_dns_name
inst.reload()
inst.public_dns_name
inst.security_groups
#Look up the security group
# Authorize incoming connections from our public IP address, on port 22
security_group = ec2.SecurityGroup('sg-4e00bc27')
security_group
security_group.authorize_ingress(
    CidrIp='12.175.4.5/32',
    FromPort=22,
    GroupName='default',
    IpPermissions=[
        {
            'FromPort': 22,
            'IpProtocol': 'TCP',
            'IpRanges': [
                {
                    'CidrIp': '12.175.4.5/32',
                    'Description': 'SSH'
                },
            ],
        },
   ],
   IpProtocol='TCP',
)
security_group.authorize_ingress(
    CidrIp='12.175.4.5/32',
    FromPort=22,
    GroupName='default',
    IpProtocol='TCP'
)
security_group.authorize_ingress(
    CidrIp='12.175.4.5/32',
    FromPort=22,
    GroupName='default',
    IpProtocol='TCP',
    ToPort=22
)
sg = ec2.SecurityGroup(inst.security_groups[0]['GroupId']
)
sg
sg.authorize_ingress(IpPermissions=[{'FromPort':22, 'ToPort':22, 'IpProtocol': 'TCP', 'IPRanges': [{'CidrIp': '10.10.10.10/32'}]}])
sg.authorize_ingress(IpPermissions=[{'FromPort':22, 'ToPort':22, 'IpProtocol': 'TCP', 'IpRanges': [{'CidrIp': '10.10.10.10/32'}]}])
sg.authorize_ingress(IpPermissions=[{'FromPort':22, 'ToPort':22, 'IpProtocol': 'TCP', 'IpRanges': [{'CidrIp': '10.10.10.11/32', 'Description': 'created for notifon'}]}])
get_ipython().run_line_magic('history', '')
sg.authorize_ingress(IpPermissions=[{'FromPort':80, 'ToPort':80, 'IpProtocol': 'TCP', 'IpRanges': [{'CidrIp': '12.175.4.5/32', 'Description': 'created for notifon'}]}])
sg.authorize_ingress(IpPermissions=[{'FromPort':80, 'ToPort':80, 'IpProtocol': 'TCP', 'IpRanges': [{'CidrIp': '0.0.0.0/0', 'Description': 'created for notifon'}]}])
inst.public_dns_name
get_ipython().run_line_magic('history', '')
