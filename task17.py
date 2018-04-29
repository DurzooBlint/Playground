import requests
from bs4 import BeautifulSoup

#get the page
req = requests.get('http://www.nytimes.com')
req_html = req.text


soup = BeautifulSoup(req_html, "html.parser")

root = soup.find_all('h2', class_='story-heading', recursive=True)

for item in root:
    print(str(root.index(item) + 1) + ' ' + item.get_text().strip())
