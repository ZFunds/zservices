from zsftp.queries import SFTPQueries
from zsftp.config import Config
# variables for testing
connection_params = {
    'hostname': Config.SFTP['hostname'],
    'username': Config.SFTP['username'],
    'password': Config.SFTP['password']
}
local_path = "/home/manish/Desktop/Project/zfunds/zservices/test/AAKPU5949A.pdf"
sftp_path = "abcd/AAKPU5949A2.pdf"

sftp = SFTPQueries(connection_params)


# testing return values
try:
    # t1 = sftp.make_directory("abcd")
    # t1 = sftp.upload_file(local_path, sftp_path)
    t1 = sftp.list_directory()
    print(f"success: {t1}")
except Exception as e:
    print(e)
except OSError as e:
    print(e)