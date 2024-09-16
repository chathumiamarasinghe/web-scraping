from bs4 import BeautifulSoup
import requests
import csv

def extract_ul_text(url):
    req = requests.get(url).text
    soup = BeautifulSoup(req, 'html.parser')
    panel_list = soup.find_all('div', class_="sppb-addon-content")

    if len(panel_list) >= 10:    # Check if at least 10 "sppb-addon-content" divs exist
        fourth_panel = panel_list[9]  # Retrieve the tenth "sppb-addon-content" div (index 9)
        uLists = fourth_panel.find_all('ul')  # Find all ul elements inside the fourth panel

        ul_texts = []  # List to store comma-separated ul texts

        for uList in uLists:
            li_texts = [li.text.strip() for li in uList.find_all('li')]
            ul_text = ','.join(li_texts)
            ul_texts.append(ul_text)

        if ul_texts:
            return ','.join(ul_texts)    # Return all elements joined as a comma-separated string
        else:
            return "Not available"
    else:
        return "Not available."

# Make a request to the webpage
url = "https://science.kln.ac.lk/depts/im/index.php/staff/academic-staff"
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the sections containing staff information
staff_sections = soup.find_all('section', class_='sppb-section')

# Initialize a list to store extracted data
data = []

# Iterate through each staff section and extract details
for section in staff_sections:
    # Find name and position
    name_elem = section.find('h3')
    position_elem = section.find('strong')

    # Extract name and position or provide default values if not found
    name = name_elem.text.strip() if name_elem else "Not available"
    position = position_elem.text.strip() if position_elem else "Not available"

    button_element = section.find('div', class_="sppb-text-center")
    url_element = button_element.find('a') if button_element else None
    if url_element:
        link = url_element.get('href')  # Get the value of the 'href' attribute
        specialization = extract_ul_text(link)  # Extract specialization for this lecturer

    # Check if both name and position are "Not available", if so, skip this entry
    if name == "Not available" and position == "Not available":
        continue

    # Find additional details
    additional_info = section.find_all('span', style='font-size: 12pt;')

    # Initialize variables for additional details
    room = phone = fax = email = "Not available"

    # Extract additional details if available
    if additional_info:
        info_texts = [info.text.strip() for info in additional_info]
        for info in info_texts:
            if 'Room' in info:
                room = info.split(':')[1].strip()
            elif 'Phone' in info:
                phone = info.split(':')[1].strip()
            elif 'Fax' in info:
                fax = info.split(':')[1].strip()
            elif 'Email' in info:
                email = info.split(':')[1].strip()

    # Append the extracted information to the data list
    data.append([name, position, room, phone, fax, email,specialization])

# Define the filename for the CSV file
csv_filename = "academic_staff.csv"

# Write the data to a CSV file
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    # Create a CSV writer object
    csv_writer = csv.writer(csvfile)

    # Write the header row
    csv_writer.writerow(['Name', 'Position', 'Room', 'Phone', 'Fax', 'Email','Specialization'])

    # Write the data rows
    csv_writer.writerows(data)

print(f"CSV file '{csv_filename}' has been created successfully.")