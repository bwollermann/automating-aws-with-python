# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')
buket = s3.create_bucket(Bucket='brian-videolyzer-videos', CreateBucketConfiguration={'LocationContraint': session.region_name})
buket = s3.create_bucket(Bucket='brian-videolyzer-videos', CreateBucketConfiguration={'LocationConstraint': session.region_name})
bucket = buket
from pathlib import Path
pathname = r'C:\Users\BWollerm\OneDrive - Nelnet, Inc\code\automating-aws-with-python\03-videolyzer\Pexels Videos 2957.mp4'
pathname = r'C:\Users\BWollerm\Downloads\Pexels Videos 2957.mp4'
path = Path(pathname).expanduser().resolve()
path
print(path)
print(path).as_posix()
path.as_posix()
bucket.upload_file(str(path), str(path.name))
rekognition_client = session.client('rekognition')
response = rekognition_client.start_label_detection(Video={'S3Object': {'Bucket': bucket.name, 'Name': path.name}})
response
JobId='7f9adb9ad96093ec1de3d9c85f5e40cd98faf04fa91747657e1423378f0c0397'
JobId = response['JobId']
result = rekognition_client.get_label_detection(JobId=job_id)
jobid = JobId
result = rekognition_client.get_label_detection(JobId=job_id)
job_id = JobId
result = rekognition_client.get_label_detection(JobId=job_id)
result
result.keys()
result['JobStatus']
result['ResponseMetadata']
result['VideoMetadata']
result['Labels']
len(result['Labels'])
