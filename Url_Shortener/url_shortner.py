import requests
import json

# Get the long URL from the user input
UI = input("Enter the long link: ")

# Bitly API Key (Note: For production, consider using environment variables for security)
api_key = '2e234fb0fc05db179a4b3d753436ce3425fd0aa3'

# Set up headers for authentication and content type
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json',
}

# Prepare the payload with the URL to shorten
data = {"long_url": UI}

# Retry logic: Attempt to shorten the URL up to 3 times
for i in range(3): 
    result = requests.post("https://api-ssl.bitly.com/v4/shorten", headers=headers, data=json.dumps(data))
    # If the request is successful (HTTP 200), exit the retry loop
    if result.status_code == 200:
        break

# Check if the final request was successful
if result.status_code == 200:
    # Parse the JSON response to extract the shortened link
    link = json.loads(result.content)['link']
    print(f"\nYour shortened link: {link}")
else:
    print("error occurred")
