import requests

# URL of the API endpoint
url = "https://uoftctf-no-code.chals.io/execute"  # Replace with your actual endpoint URL

# Python code to be sent in the POST request
code = '2 + \x01'

# Data to be sent in the POST request
data = {'code': code}

# Send the POST request
response = requests.post(url, data=data)

# Print the response
print(response.status_code)
print(response.json())
