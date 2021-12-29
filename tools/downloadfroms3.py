import boto3, os

# assumes credentials & configuration are handled outside python in .aws directory or environment variables
s3 = boto3.resource('s3') 

bucket_name = "mybuckets3s3s3s3s3s3"
s3_folder = "jenkins"
local_dir = "/tmp/jenkins"


def download_s3_folder(bucket_name, s3_folder, local_dir=None):
    """
    Download the contents of a folder directory
    Args:
        bucket_name: the name of the s3 bucket
        s3_folder: the folder path in the s3 bucket
        local_dir: a relative or absolute directory path in the local file system
    """
    bucket = s3.Bucket(bucket_name)
    for obj in bucket.objects.filter(Prefix=s3_folder):
        target = obj.key if local_dir is None \
            else os.path.join(local_dir, os.path.relpath(obj.key, s3_folder))
        if not os.path.exists(os.path.dirname(target)):
            os.makedirs(os.path.dirname(target))
        if obj.key[-1] == '/':
            continue
        print("Downloading {} into {}".format(obj.key, target))
        bucket.download_file(obj.key, target)

download_s3_folder(bucket_name, s3_folder, local_dir)