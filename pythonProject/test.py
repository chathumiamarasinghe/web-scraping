import requests

# URL of the webpage
url = 'https://science.kln.ac.lk/depts/im/index.php/staff/academic-staff'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the HTML content of the webpage
    print(response.text)
else:
    print("Failed to retrieve the webpage")
