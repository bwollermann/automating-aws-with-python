import boto3
import click
import re

session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')

@click.group()
def cli():
    "Webotron deploys websites to AWS"
    pass

@cli.command('list-buckets')
def list_buckets():
    "List all s3 buckets"
    regex = re.compile("automating")
    for bucket in s3.buckets.all():
        if regex.search(bucket.name):  # If we find a match do the following:
            print(bucket)

@cli.command('list-bucket-objects')
@click.argument('bucket')
def list_bucket_objects(bucket):
    "List objects in an S3 bucket"
    for obj in s3.Bucket(bucket).objects.all():
        print (obj)

if __name__ == '__main__':
    cli()
