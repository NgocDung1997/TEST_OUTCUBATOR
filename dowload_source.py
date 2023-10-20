import requests
import os
import zipfile

def dowload_from_url():
    # URL dowload file
    download_uris = [
        "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
        "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip"
    ]

    # Path audit file
    output_directory = "D:\\test\\TEST_OUTCUBATOR\\audit"

    # Check if path audit not exist -> create
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)


    for download_uri in download_uris:
        file_name = os.path.basename(download_uri)
        
        download_path = os.path.join(output_directory, file_name)
        print("Dowload path : "+download_path)
        response = requests.get(download_uri, stream=True)
        with open(download_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        with zipfile.ZipFile(download_path, 'r') as zip_ref:
            zip_ref.extractall(output_directory)

        os.remove(download_path)
    