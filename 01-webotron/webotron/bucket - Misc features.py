# -*- coding: utf-8 -*-

"""Classes for S3 Buckets."""

from pathlib import Path
import mimetypes
from functools import reduce

import boto3
from botocore.exceptions import ClientError

from hashlib import md5
import util


class BucketManager:
    """Manage an S3 Bucket."""

    CHUNK_SIZE = 8388608
    found_keys = []

    def __init__(self, session):
        """Create a BucketManager object."""
        self.session = session
        self.s3 = self.session.resource('s3')
        self.transfer_config = boto3.s3.transfer.TransferConfig(
            multipart_chunksize=self.CHUNK_SIZE,
            multipart_threshold=self.CHUNK_SIZE
        )
        self.manifest = {}

    def get_region_name(self, bucket):
        """Get the bucket's region name."""
        bucket_location = self.s3.meta.client.get_bucket_location(
            Bucket=bucket.name)

        return bucket_location["LocationConstraint"] or 'us-east-1'

    def get_bucket_url(self, bucket):
        """Get the website URL for this bucket."""
        return "http://{}.{}".format(
            bucket.name,
            util.get_endpoint(self.get_region_name(bucket)).host)

    def all_buckets(self):
        """Get an iterator for all buckets."""
        return self.s3.buckets.all()

    def all_objects(self, bucket_name):
        """Get an iterator for all objects in a bucket."""
        return self.s3.Bucket(bucket_name).objects.all()

    def init_bucket(self, bucket_name):
        """Create new bucket, or retrun existing on by name."""
        s3_bucket = None
        try:
            s3_bucket = self.s3.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={
                    'LocationConstraint': self.session.region_name
                }
            )
        except ClientError as error:
            if error.response['Error']['Code'] == 'BucketAlreadyOwnedByYou':
                s3_bucket = self.s3.Bucket(bucket_name)
            else:
                raise error

        return s3_bucket

    def set_policy(self, bucket):
        """Set bucket policy to be readable by everyone."""
        policy = """
        {
            "Version":"2012-10-17",
            "Statement":[{
            "Sid":"PublicReadGetObject",
            "Effect":"Allow",
            "Principal": "*",
                "Action":["s3:GetObject"],
                "Resource":["arn:aws:s3:::%s/*"
                ]
             }
             ]
        }
        """ % bucket.name
        policy = policy.strip()

        pol = bucket.Policy()
        pol.put(Policy=policy)

    def configure_website(self, bucket):
        """Configure the website."""
        # ws = s3_bucket.Website()
        # ws.put(WebsiteConfiguration={
        bucket.Website().put(WebsiteConfiguration={
            'ErrorDocument': {
                'Key': 'error.html'
            },
            'IndexDocument': {
                'Suffix': 'index.html'
            }
        })

    def load_manifest(self, bucket):
        """Load manifest for caching purposes."""
        # print("Loading manifest")
        paginator = self.s3.meta.client.get_paginator('list_objects_v2')
        for page in paginator.paginate(Bucket=bucket.name):
            for obj in page.get('Contents', []):
                self.manifest[obj['Key']] = obj['ETag']
        print("Manifest=", self.manifest)

    # Use when you don't need to know anything about bucket or BucketManager
    @staticmethod
    def hash_data(data):
        """Generate md5 hash for data."""
        hash = md5()
        hash.update(data)

        return hash

    def gen_etag(self, path):
        """Generate etag for file."""
        hashes = []

        with open(path, 'rb') as f:
            while True:
                data = f.read(self.CHUNK_SIZE)

                if not data:
                    break

                hashes.append(self.hash_data(data))

        if not hashes:
            return '"{}"'.format(self.hash_data(data).hexdigest())
        elif len(hashes) == 1:
            return '"{}"'.format(hashes[0].hexdigest())
        else:
            digests = (h.digest() for h in hashes)
            hash = self.hash_data(reduce(lambda x, y: x + y, digests))
            # hash = self.hash_data(reduce(
            # lambda x,
            # y: x + y,
            # (h.digest() for h in hashes)))
            return '"{}-{}"'.format(hash.hexdigest(), len(hashes))

    def upload_file(self, bucket, path, key):
        """Upload path to s3_bucket at key."""
        content_type = mimetypes.guess_type(key)[0] or 'text/plain'

        etag = self.gen_etag(path)
        # print("Key=", key, "ETag new object=", etag
        #       " Etag manifest=", self.manifest.get(key, ''))

        self.found_keys.append(key)
        # print('Found_keys=', self.found_keys)
        manifest_key = self.manifest.get(key, '')
        if manifest_key == etag:
            print("Skipping {}, etags match".format(key))
            return

        return bucket.upload_file(
            path,
            key,
            ExtraArgs={
                'ContentType': content_type
            },
            Config=self.transfer_config)

    def sync(self, pathname, bucket_name):
        """Sync contents of path to bucket."""
        bucket = self.s3.Bucket(bucket_name)
        self.load_manifest(bucket)

        root = Path(pathname).expanduser().resolve()

        def handle_directory(target):
            for p in target.iterdir():
                if p.is_dir():
                    handle_directory(p)
                if p.is_file():
                    # print("Path: {}\n Key: {}".format(p,
                    #                                   p.relative_to(root)))
                    # upload_file(
                    #   s3_bucket, str(p),
                    #   str(p.relative_to(root)).replace("\\","/"))
                    key = p.relative_to(root).as_posix()
                    # key = (p.relative_to(root).replace("\\", "/"))
                    # print("Bucket=", bucket, "\nPath=", p, "\nKey=", key)
                    self.upload_file(bucket, str(p), str(key))

        handle_directory(root)

        def compare_manifest():
            """Search each manifest file to see if it is in found keys."""
            for manifest_key, manifest_hash in self.manifest.items():
                if manifest_key not in self.found_keys:
                    print(manifest_key, "no longer exists in the website")

        compare_manifest()
