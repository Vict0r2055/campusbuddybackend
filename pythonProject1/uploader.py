import requests
import os

url = 'http://127.0.0.1:5000/upload'  # Replace with the actual server URL
folder_path = 'C:\\Users\\luyas\\Documents\\Campus'  # Replace with the actual folder path

def upload_files():
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as f:
                files = {'file': f}
                response = requests.post(url, files=files)
                print(f'Uploaded {file_path}: {response.text}')

#upload_files(url, folder_path)


