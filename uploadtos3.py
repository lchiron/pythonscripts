import os
import sys
import boto3
import pathlib

# get an access token, local (from) directory, and S3 (to) directory
# from the command-line
local_directory = "/Users/edward.li/jenkins_home"
bucket = "mybuckets3s3s3s3s3s3"
destination = "jenkins"

client = boto3.client('s3')


# enumerate local files recursively
for root, dirs, files in os.walk(local_directory):

  for filename in files:

    # construct the full local path
    local_path = os.path.join(root, filename)

    # construct the full Dropbox path
    relative_path = os.path.relpath(local_path, local_directory)
    s3_path = os.path.join(destination, relative_path)

    # relative_path = os.path.relpath(os.path.join(root, filename))
    try:
        print('Searching {} in {}'.format(s3_path, bucket))
        localfilesize = os.path.getsize(local_path)
        head = client.head_object(Bucket=bucket, Key=s3_path)
        s3contentlenth = head['ContentLength']
        if localfilesize != s3contentlenth:
            print("Found local file {} content changed, uploading...".format(s3_path))
            client.upload_file(local_path, bucket, s3_path)
        
        # try:
            # client.delete_object(Bucket=bucket, Key=s3_path)
        # except:
            # print "Unable to delete %s..." % s3_path
    except:
        print("S3 not found {} Uploading...".format(s3_path))
        client.upload_file(local_path, bucket, s3_path)