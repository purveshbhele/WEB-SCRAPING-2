from bs4 import BeautifulSoup as bs
import requests
import pandas as pd 
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page=requests.get(START_URL)

soup=bs(page.text,'html.parser')
star_table= soup.find('table')
temp_list=[]
table_rows=star_table.find_all('tr')
for tr in table_rows:
    td=tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

star_names=[]
distance=[]
mass=[]
radius=[]
constellation=[]
discovery_year=[]
for i in range(1,len(temp_list)):
    distance.append(temp_list[i][5])
    mass.append(temp_list[i][8])
    radius.append(temp_list[i][9])
    constellation.append(temp_list[i][1])
    discovery_year.append(temp_list[i][13])

df=pd.DataFrame(list(zip(distance,mass,radius,constellation,discovery_year)),columns=['Distance','Mass','Radius','constellation','discovery_year'])
df.to_csv('brown_dwarfs.csv')
