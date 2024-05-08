import os
import requests
import json
from bs4 import BeautifulSoup


def download_file(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        content_type = response.headers.get('content-type')
        if 'xml' in content_type:
            with open(save_path, 'wb') as file:
                file.write(response.content)
            print('XML file downloaded successfully!')
        else:
            print('The file is not in XML format.')
    else:
        print('Failed to download the file.')
def scrape_website():
    url = 'http://mycelcat.unizulu.ac.za/mindex.html'
    response = requests.get(url)

    if response.status_code == 200:
        document = BeautifulSoup(response.text, 'html.parser')
        select_element = document.select_one('select')

        if select_element is not None:
            option_elements = select_element.select('option:not(:first-child)')

            data = {}  # Dictionary to store scraped data

            for option in option_elements:
                text = option.text
                key = text[:7]
                value_html = option['value']
                value = value_html[:6] + '.xml'
                print(value)

                if key != 'Please':
                    link = f'http://mycelcat.unizulu.ac.za/{value}'
                    response2 = requests.get(link)
                    print(response2.status_code)

                    # Download the source file
                    base_directory = os.path.expanduser('~/Documents')
                    save_directory = os.path.join(base_directory, 'Campus/timetableData')
                    os.makedirs(save_directory, exist_ok=True)
                    save_path = os.path.join(save_directory, value)
                    events = download_file(link, save_path)

                    if events is not None:
                        data[key] = {'text': text, 'value': value, 'events': events}

            # Write data to JSON file
            base_directory = os.path.expanduser('~/Documents')
            save_directory2 = os.path.join(base_directory, 'Campus')
            json_data = json.dumps(data)
            json_path = os.path.join(save_directory2, 'timetable.json')

            with open(json_path, 'w') as json_file:
                json_file.write(json_data) #this one maps module code with file name 

            print('Data saved to timetable.json')
        else:
            print('Select element not found')
    else:
        print('Failed to fetch the webpage')

    print('done boooooooooooooii beVictorious ')
