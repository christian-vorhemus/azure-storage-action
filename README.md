# Azure Storage Action

This simplistic action allows to upload or download blobs to the local system.

## Inputs

### `direction`

**Required** Specifies if you want to 'upload' or 'download' a blob.

### `connection_string`

**Required** Specifies the connection string of the Azure Storage account to use.

### `container`

**Required** Specifies the container name of your Azure Storage account to use.

### `blob_path`

**Required**  Specifies the path or file of the blob in your Azure Storage account.

### `local_path`

**Optional** Specifies the path or file on the local machine. Default: `./`

## Example usage

Download a file `theblob.txt` from container `mycontainer` to the local directory `./build`

```
- name: Download blob
  uses: christian-vorhemus/azure-storage-action@v3
  with:
    direction: 'download'
    connection_string: ${{ secrets.AZUREBLOBCONNECTIONSTRING }}
    container: 'mycontainer'
    blob_path: 'theblob.txt'
    local_path: './build'
```

Upload a local file `theblob.txt` to the Azure storage container `mycontainer` under folder `blobs/`:

```
- name: Upload blob
  uses: christian-vorhemus/azure-storage-action@v3
  with:
    direction: 'upload'
    connection_string: ${{ secrets.AZUREBLOBCONNECTIONSTRING }}
    container: 'mycontainer'
    blob_path: 'blobs/'
    local_path: './theblob.txt'
```