from zsftp.sftp import SFTP
from zdynamodb import logger


class SFTPQueries:
    def __init__(self, connection_params=None):
        logger.info('[SFTP]: Initiating SFTPQueries Class')
        self.connection_params = connection_params
        self._client = SFTP(self.connection_params).connection

    def upload_file(self, local_path, sftp_path):
        try:
            resp = self._client.put(local_path, sftp_path)
            return resp
        except Exception as e:
            logger.warning(f'[SFTP]: Unable to upload file on sftp server, e= {e}')
            raise e
        finally:
            self._client.close()

    def make_directory(self, dir_name):
        try:
            self._client.mkdir(dir_name)
        except Exception as e:
            logger.warning(f'[SFTP]: Unable to create sftp connection, e= {e}')
            raise e
        finally:
            self._client.close()

    def list_directory(self):
        try:
            dir_list = self._client.listdir()
            return dir_list
        except Exception as e:
            logger.warning(f'[SFTP]: Unable to create sftp connection, e= {e}')
            raise e
        finally:
            self._client.close()
