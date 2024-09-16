import requests

# Specify the URL of the webpage you want to get the HTML from
url = "https://science.kln.ac.lk/depts/im/index.php/staff/academic-staff"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Get the HTML content from the response
html_content = response.text

# Print or process the HTML content as needed
print(html_content)
