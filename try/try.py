from google.cloud import storage
import os

def upload_file(bucket_name, local_file_path, destination_directory):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)

    file_name = os.path.basename(local_file_path)
    storage_path = os.path.join(destination_directory, file_name)

    blob = bucket.blob(storage_path)
    blob.upload_from_filename(local_file_path)

    print(f"Uploaded {local_file_path} to gs://{bucket_name}/{storage_path}")

# Example usage:
upload_file('axona-hs1', "text_files/jtjp.txt", "jd")
