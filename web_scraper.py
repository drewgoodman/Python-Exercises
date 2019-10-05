# © 2019, Drew Goodman, all rights reserved

import requests
from inflection import titleize
from bs4 import BeautifulSoup

url = requests.get("https://www.dailysmarty.com/topics/python")
html_text = BeautifulSoup(url.text, 'html.parser')
# print(html_text.prettify())
print(f"\n <<< {html_text.title.string.lstrip('DailySmarty | ').upper()}:  >>> \n")

for link in html_text.find_all('a'):
    link_clean = link.get('href')
    if "posts/" in link_clean:
        link_clean = titleize(link_clean.lstrip("/posts/"))
        print(f'   - "{link_clean}"')