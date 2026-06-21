from azure.storage.blob import BlobServiceClient
import pandas as pd
from io import StringIO

#Azure Blob storage account credintials
account_name = 'depracticegk'
account_key = 'ACCESS_KEY'
container_name = 'raw-data'
blob_name = 'orders_dataset.csv'

# Connecting string (using this instead  of account name and key)
# this is we can fetch from the azure secrate access keys section the whole connection string

connection_string = f"DefaultEndpointsProtocol=https;AccountName={account_name};AccountKey={account_key};EndpointSuffix=core.windows.net"

# Initilize BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# get the container client 
container_client = blob_service_client.get_container_client(container_name)

# get blob client 
blob_client = container_client.get_blob_client(blob_name)

# download blob content as a string

blob_data = blob_client.download_blob().content_as_text()

# read the content into a dataframe

df = pd.read_csv(StringIO(blob_data))

# print the data for the verification 
print(df)