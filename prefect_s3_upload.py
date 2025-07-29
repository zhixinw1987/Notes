from concurrent.futures import ThreadPoolExecutor
import os
from prefect_aws.s3 import S3Bucket

s3 = S3Bucket.load("my-s3-bucket-block")

def upload_file(file_path, base_dir, prefix):
    rel_path = os.path.relpath(file_path, base_dir)
    s3_path = f"{prefix}/{rel_path}"
    s3.put_file(from_path=file_path, to_path=s3_path)

base_dir = "/data/myfolder"
prefix = "mybackup"

with ThreadPoolExecutor(max_workers=8) as executor:
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            full_path = os.path.join(root, file)
            executor.submit(upload_file, full_path, base_dir, prefix)
