from pathlib import Path
import glob
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
import os


def upload_to_blob():
    dotenv_path = Path(__file__).resolve().parents[1] / ".env"
    load_dotenv(dotenv_path)

    file_directory = os.getenv("DATA_PATH")    
    azure_conn = os.getenv("AZURE_CONNECTION_STRING")
    container_name = os.getenv("AZURE_CONTAINER_NAME")
    
    blob_service_client = BlobServiceClient.from_connection_string(azure_conn)
    container_client = blob_service_client.get_container_client(container_name)

    csv_files = glob.glob(str(Path(__file__).resolve().parents[1] / file_directory / "*.csv"))
    json_files = glob.glob(str(Path(__file__).resolve().parents[1] / file_directory / "*.json"))

    files = csv_files + json_files


    print(f"File directory: {file_directory}")
    print(f"Matched files: {files}")
        
    for file_path in files:
        file_name = Path(file_path).name
        
        with open(file_path, "rb") as data:
            blob_name = f"bronze/{file_name}"  
            container_client.upload_blob(name=blob_name, data=data, overwrite=True)
            print(f"Uploaded: {blob_name}")
    
    return 

def main():
    upload_to_blob()

if __name__ == "__main__":
    main()
