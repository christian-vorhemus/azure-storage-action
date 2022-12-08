import os
from blobstorage import BlobStorageConnection


def main(action, connection_string, container, blob_path, local_path):
    conn = BlobStorageConnection(connection_string)

    if action == "upload":
        conn.put(container, blob_path, local_path)
    else:
        conn.get(container, blob_path, local_path)


if __name__ == "__main__":
    action = os.environ["INPUT_ACTION"]
    connection_string = os.environ["INPUT_CONNECTION_STRING"]
    container = os.environ["INPUT_CONTAINER"]
    blob_path = os.environ["INPUT_BLOB_PATH"]
    local_path = os.environ["INPUT_LOCAL_PATH"]
    main(action, connection_string, container, blob_path, local_path)
