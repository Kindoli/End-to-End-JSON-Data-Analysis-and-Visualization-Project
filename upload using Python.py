
import os
import boto3

# 🛠️ CONFIGURATION: Update these values
LOCAL_FOLDER = "D:/10.Work/Data Engineer/Data Engineering Projects/Yelp Dataset"  # Folder path
S3_BUCKET = "yelpanalysisdata"        #S3 bucket name
S3_PREFIX = "yelpreviews/"         # Prefix inside S3 bucket
AWS_REGION = "eu-north-1"                 # AWS region

# Initializing S3 client
s3_client = boto3.client("s3", region_name=AWS_REGION)

def upload_files_to_s3(local_folder, bucket, prefix=""):
    """Uploads all files in a local folder to an S3 bucket."""
    for root, _, files in os.walk(local_folder):
        for file in files:
            local_path = os.path.join(root, file)
            s3_key = os.path.join(prefix, file).replace("\\", "/")  # Normalize path for S3

            try:
                s3_client.upload_file(local_path, bucket, s3_key)
                print(f"✅ Uploaded: {file} → s3://{bucket}/{s3_key}")
            except Exception as e:
                print(f"❌ Failed to upload {file}: {e}")

# Run the upload function
upload_files_to_s3(LOCAL_FOLDER, S3_BUCKET, S3_PREFIX)
