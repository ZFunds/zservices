from zs3 import s3
from zs3.config import Config

# variables for testing
connection_params = {
    'region': Config.AWS['region'],
    's3_key_id': Config.AWS['s3_key_id'],
    's3_key_secret': Config.AWS['s3_key_secret']
}
bucket_name = "zfund-data-storage-pre"
upload_from_url = "url"
upload_from_file = "file path"
with open("test3.txt", 'w') as file_obj:
    upload_from_file_obj = file_obj
s3_conn = s3.S3(connection_params)


# testing return values
try:
    t1 = s3_conn.url_upload_to_s3(upload_from_url, object_id="test1")
    print(f"success: {t1}")
except Exception as e:
    print(e)

try:
    t2 = s3_conn.file_upload_to_s3(upload_from_file, object_id="test2")
except Exception as e:
    print(e)

try:
    with open("test3.txt", 'rb') as file_obj:
        upload_from_file_obj = file_obj
        t3 = s3_conn.bytes_upload_to_s3(upload_from_file_obj, object_id="test3", bucket=bucket_name)
except Exception as e:
    print(e)
