
"""
To download a file from a website in Python,
you can use the requests library to make an HTTP GET request to the file's URL and then save the content to a local file.
Here's an example of how to download a file from a website:

In this code:

We import the requests library to make an HTTP GET request to the file's URL.

We specify the URL of the file you want to download.

We send an HTTP GET request to the file URL using requests.
get(file_url) and check if the request was successful (status code 200).

If the request is successful, we extract the filename from the URL or provide a custom filename.

We specify the local path where you want to save the file. You can customize the path as needed.

We save the content of the file to the local path using a binary write ('wb') mode to ensure proper handling of binary files.

Finally, we print a message indicating whether the file was downloaded successfully.

Remember to adjust the file_url and local_path variables according to your specific use case.
Additionally, make sure to handle any potential exceptions that may occur during the file download process,
such as network errors or invalid URLs.


"""


import requests

# URL of the file you want to download
file_url = 'https://example.com/path-to-your-file/file.pdf'

# Send an HTTP GET request to the file URL
response = requests.get(file_url)

# Check if the request was successful
if response.status_code == 200:
    # Extract the filename from the URL or provide a custom filename
    filename = file_url.split('/')[-1]  # Extract the filename from the URL

    # Specify the local path where you want to save the file
    local_path = f'./downloads/{filename}'  # You can specify your desired directory

    # Save the file to the local path
    with open(local_path, 'wb') as file:
        file.write(response.content)

    print(f"File '{filename}' downloaded successfully to '{local_path}'")
else:
    print(f"Failed to download the file. Status code: {response.status_code}")


"""
To copy a file from a network path to a local path using Python, you can use the shutil module. 
Here's an example of how to do this:

In this code:

We import the shutil module, which provides high-level file operations.

We specify the source network path (UNC path) of the file you want to copy, such as \\server\share\file.txt.

We specify the destination local path where you want to copy the file. 
Make sure to specify the correct local path where you want to save the file.

We use a try-except block to handle potential exceptions that may occur during the copy process. 
We catch FileNotFoundError if the source file doesn't exist, PermissionError if there are permission issues, 
and a generic Exception for other potential errors.

If the copy operation is successful, a success message is printed.

Make sure to replace the source_network_path and destination_local_path variables with the actual network and local file paths you want to use. 
Also, ensure that your Python script has appropriate permissions to access the network path and write to the local path.

"""

import shutil

# Specify the source network path (UNC path) of the file
source_network_path = r'\\server\share\file.txt'

# Specify the destination local path where you want to copy the file
destination_local_path = 'C:/local_folder/file.txt'

try:
    # Use shutil.copy to copy the file from the source to the destination
    shutil.copy(source_network_path, destination_local_path)
    print(f"File copied successfully from {source_network_path} to {destination_local_path}")
except FileNotFoundError:
    print("Source file not found.")
except PermissionError:
    print("Permission error: Unable to copy the file.")
except Exception as e:
    print(f"An error occurred: {str(e)}")


"""
To download a file from an FTP server using Python, you can use the built-in ftplib module. 
Here's an example of how to download a file from an FTP server:

We import the FTP class from the ftplib module.

We specify the FTP server details, including the hostname (ftp_host), your FTP username (ftp_user), 
and your FTP password (ftp_pass).

We define the path to the file you want to download on the FTP server (remote_file_path) and the local path where you want to save the downloaded file (local_file_path).

Inside the try block, we create an FTP connection to the specified host and log in using the provided credentials.

If the file is in a specific directory on the FTP server, you can use the ftp.cwd("/remote_directory") method to change the current working directory.

We use the ftp.retrbinary method to download the file from the FTP server and save it to the local file. 
The "RETR " command retrieves the file, and local_file.write is used to write the data to the local file.

Finally, we print a success message if the download is successful. If an error occurs, an exception message is printed.

Make sure to replace the placeholders for FTP server details, remote and local file paths, 
and credentials with your specific information. Additionally, you may need to handle various FTP-specific errors based on your use case.


"""


from ftplib import FTP

# FTP server details
ftp_host = "ftp.example.com"
ftp_user = "your_username"
ftp_pass = "your_password"

# File to download on the FTP server
remote_file_path = "/path/to/remote/file.txt"

# Local path to save the downloaded file
local_file_path = "/path/to/local/downloaded_file.txt"

try:
    # Create an FTP connection and log in
    with FTP(ftp_host) as ftp:
        ftp.login(user=ftp_user, passwd=ftp_pass)

        # Change to the appropriate directory on the FTP server (if needed)
        # ftp.cwd("/remote_directory")

        # Download the file
        with open(local_file_path, "wb") as local_file:
            ftp.retrbinary("RETR " + remote_file_path, local_file.write)

        print(f"File downloaded successfully to {local_file_path}")
except Exception as e:
    print(f"An error occurred: {str(e)}")


"""

To download a file from an API using Python, you can use the requests library to send an HTTP GET request to the API endpoint, 
receive the file as a response, 
and save it to a local file. Here's an example of how to do this:

In this code:

We import the requests library to make an HTTP GET request to the API.

We specify the API endpoint URL (api_url) where the file is available.

We specify the local path (local_file_path) where you want to save the downloaded file.

Inside the try block, we send an HTTP GET request to the API endpoint using requests.get(api_url) 
and check if the request was successful (status code 200).

If the request is successful, we save the content of the file to the local path using binary write ('wb') 
mode to ensure proper handling of binary files.

We print a success message if the download is successful. If an error occurs, an exception message is printed.

Make sure to replace the api_url and local_file_path variables with the actual API endpoint URL and the local file path where you want to save the downloaded file. 
Additionally, handle any potential exceptions that may occur during the download process, such as network errors or invalid URLs.
"""

import requests

# API endpoint for file download
api_url = 'https://api.example.com/download/file'

# Local path to save the downloaded file
local_file_path = '/path/to/local/downloaded_file.zip'

try:
    # Send an HTTP GET request to the API endpoint
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Save the file to the local path
        with open(local_file_path, 'wb') as local_file:
            local_file.write(response.content)
        print(f"File downloaded successfully to {local_file_path}")
    else:
        print(f"Failed to download the file. Status code: {response.status_code}")
except Exception as e:
    print(f"An error occurred: {str(e)}")
