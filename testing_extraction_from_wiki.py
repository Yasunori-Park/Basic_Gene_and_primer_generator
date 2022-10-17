from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import pandas as pd

url = "https://www.targetscan.org/cgi-bin/targetscan/vert_72/targetscan.cgi?species=Human&mir_sc=miR-145-5p"
data = requests.get(url).text
soup = BeautifulSoup(data, 'html.parser')

list = []

for row in soup.find_all('td'):
    for columns in row.find_all('target'):
        print(columns)
    #if(columns!=[]):
    #    Gene = columns[0].text.strip()
    #    list.append(Gene)

#print(list)
