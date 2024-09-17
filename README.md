# Academic Staff Scraper

This Python script scrapes academic staff information from the Faculty of Science, University of Kelaniya's website, specifically the staff details page. The script retrieves each staff member's name, position, room number, phone, fax, email, and specialization (if available) and exports the information into a CSV file.

## Prerequisites

Make sure you have the following Python packages installed before running the script:

- `requests`: For sending HTTP requests to fetch the webpage.
- `beautifulsoup4`: For parsing the HTML content of the webpage.
- `csv`: For writing the extracted data to a CSV file.

You can install the required packages using `pip`:
## How It Works

- **Extract Data from URL**: The script sends a request to the webpage containing the academic staff details.
- **Parse HTML**: It uses BeautifulSoup to parse the HTML and identify the relevant sections for staff data.
- **Retrieve Staff Information**: For each academic staff member, the script extracts:
  - Name
  - Position
  - Room number
  - Phone number
  - Fax
  - Email
  - Specialization (scraped from a link if available)
- **CSV Output**: The data is written to a CSV file named `academic_staff.csv`.

## Example Output

-<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Position</th>
      <th>Room</th>
      <th>Phone</th>
      <th>Fax</th>
      <th>Email</th>
      <th>Specialization</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Prof.Janaka Wijanayake</td>
      <td>Professorr</td>
      <td>Room 201</td>
      <td>011-2233445</td>
      <td>011-2233446</td>
      <td>janaka@stu.kln.ac.lk</td>
      <td>Computer Science</td>
    </tr>
    <tr>
      <td>Dr. Thilini Mahanama</td>
      <td>Senior Lecture</td>
      <td>Room 202</td>
      <td>011-1234567</td>
      <td>Not available</td>
      <td>thilinie@uni.lk</td>
      <td>Physics</td>
    </tr>
  </tbody>
</table>


## Usage

1. Clone or download the repository containing this script.
2. Make sure you have Python installed on your system.
3. Install the required Python libraries using the following command:
   ```bash
   pip install requests beautifulsoup4
