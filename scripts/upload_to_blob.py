from pathlib import Path
import glob
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
import os


def upload_to_blob():
    # Load environment variables from .env
    dotenv_path = Path(__file__).resolve().parents[1] / ".env"
    load_dotenv(dotenv_path)

    # Load the file path from the environment variable (relative path)
    file_directory = os.getenv("DATA_PATH")
    
    if not file_directory:
        print("File path not found in environment variables.")
        return

    print(f"Looking for files in: {Path(__file__).resolve().parents[1] / file_directory}")
    
    azure_conn = os.getenv("AZURE_CONNECTION_STRING")
    container_name = os.getenv("AZURE_CONTAINER_NAME")
    
    # Connect to Azure Blob Storage
    blob_service_client = BlobServiceClient.from_connection_string(azure_conn)
    container_client = blob_service_client.get_container_client(container_name)
    
    # Use glob to get all CSV files in the folder using relative path
    files = glob.glob(str(Path(__file__).resolve().parents[1] / file_directory))  # Relative path
    
    print(f"Matched files: {files}")
    
    for file_path in files:
        # Get the file name from the path
        file_name = Path(file_path).name
        
        # Upload the file to Azure Blob Storage
        with open(file_path, "rb") as data:
            blob_name = f"bronze/{file_name}"  # Set the desired blob name
            container_client.upload_blob(name=blob_name, data=data, overwrite=True)
    
    print("Files uploaded successfully!")
    return 1

def main():
    upload_to_blob()

if __name__ == "__main__":
    main()