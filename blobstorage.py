import os
from azure.storage.blob import BlobServiceClient, BlobClient


class BlobStorageConnection:
    def __init__(self, connection_string):
        self._client = BlobServiceClient.from_connection_string(connection_string)

    def create_container(self, containername):
        try:
            self._client.create_container(containername)
        except Exception:
            pass

    def put(self, container_name, blob_name, local_file_path):
        """Stores a blob file in a local or remote storage account"""
        file_name = os.path.basename(local_file_path)
        full_blob_name = str(os.path.join(blob_name, file_name))
        blob_client: BlobClient = self._client.get_blob_client(
            container=container_name, blob=full_blob_name
        )
        success_delete = self._delete(container_name, blob_name)
        with open(local_file_path, "rb+") as data:
            blob_client.upload_blob(data)

    def _delete(self, container_name, blob_name):
        """Removes a blob file from a local or remote storage account"""
        try:
            blob_client = self._client.get_blob_client(
                container=container_name, blob=blob_name
            )
            blob_client.delete_blob()
            return True
        except:
            return False

    def get(self, container_name, blob_name, local_path="./"):
        """Downloads a blob file from a local or remote storage account and returns a file path to the downloaded file"""
        blob_client = self._client.get_blob_client(
            container=container_name, blob=blob_name
        )

        file_name = os.path.basename(blob_name)
        save_file_path = os.path.join(local_path, file_name)

        with open(save_file_path, "wb+") as f:
            downloaded_file = blob_client.download_blob()
            downloaded_file.readinto(f)
            return os.path.abspath(save_file_path)
