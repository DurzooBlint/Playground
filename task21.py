import requests
from bs4 import BeautifulSoup

#get the page
req = requests.get('http://www.nytimes.com')
req_html = req.text


soup = BeautifulSoup(req_html, "html.parser")

root = soup.find_all('h2', class_='story-heading', recursive=True)

with open('file_to_save.txt', 'w') as open_file:
    for item in root:
     open_file.write(str(root.index(item) + 1) + ' ' + item.get_text().strip())