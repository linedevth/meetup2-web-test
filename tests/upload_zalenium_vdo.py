import boto3
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("access_key", help="AWS access key")
parser.add_argument("secret_key", help="AWS secret key")
parser.add_argument("bucket", help="AWS S3 bucket name")
parser.add_argument("files_path", help="Path contains files")
parser.add_argument("key_prefix", help="Key name prefix (folder) in S3")
args = parser.parse_args()

BUCKET_NAME = args.bucket

s3 = boto3.resource(
    's3',
    aws_access_key_id=args.access_key,
    aws_secret_access_key=args.secret_key
)

for root, dirs, files in os.walk(args.files_path):
    for name in files:
        if name.endswith((".mp4")):
            file_path = root + name
            test_name = name.split('.')[0].replace('zalenium_', '')
            key_name = args.key_prefix + '/' + test_name + '.mp4'
            data = open(file_path, 'rb')

            print('Uploading:' + name)
            result = s3.Bucket(BUCKET_NAME).put_object(Key=key_name, Body=data, ACL='public-read', ContentType='video/mp4')
