import os  # Import the os module to interact with the operating system
import requests  # Import the requests library to make HTTP requests
from dotenv import load_dotenv  # Import load_dotenv to load environment variables from a .env file

# Load environment variables from the .env file
load_dotenv()

# Define the Pinata API URL for pinning files to IPFS
PINATA_API_URL = "https://api.pinata.cloud/pinning/pinFileToIPFS"


# Retrieve Pinata API keys from environment variables
PINATA_API_KEY = os.getenv("PINATA_API_KEY")
PINATA_SECRET_API_KEY = os.getenv("PINATA_SECRET_API_KEY")

def upload_pdf_to_pinata(file_path):
    """
    Uploads a PDF file to Pinata's IPFS service.

    Args:
        file_path (str): The path to the PDF file to be uploaded.

    Returns:
        str: The IPFS hash of the uploaded file if successful, None otherwise.
    """
    # Prepare headers for the API request with the Pinata API keys
    headers = {
        "pinata_api_key": PINATA_API_KEY,
        "pinata_secret_api_key": PINATA_SECRET_API_KEY
    }

    # Open the file in binary read mode
    with open(file_path, 'rb') as file:
        # Send a POST request to Pinata API to upload the file
        response = requests.post(PINATA_API_URL, files={'file': file}, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            print("File uploaded successfully")  # Print success message
            # Return the IPFS hash from the response JSON
            return response.json()['IpfsHash']
        else:
            # Print an error message if the upload failed
            print(f"Error: {response.text}")
            return None  # Return None to indicate failure
