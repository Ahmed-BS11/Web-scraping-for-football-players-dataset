from pickle import NONE
import time
import pandas as pd
from bs4 import BeautifulSoup
import requests

def extract_source(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    source=requests.get(url, headers=headers).text
    return source

def controle(x):
    if x is not None:
        x=x.text
    return x

df=pd.DataFrame()
player_data={}
html_text=extract_source("https://www.transfermarkt.com/transfers/saisontransfers/statistik?land_id=0&ausrichtung=&spielerposition_id=&altersklasse=&leihe=&transferfenster=alle&saison-id=0&plus=6/page=5")
soup = BeautifulSoup(html_text, 'html.parser')

blocks_odd=soup.find_all('tr',class_='odd')
blocks_even=soup.find_all('tr',class_='even')
players_data=[]

for block_odd in blocks_odd:
    player_name=block_odd.find('img',{'class':'bilderrahmen-fixed lazy lazy'}).get('title')
    player_value=block_odd.find('td',class_='rechts')
    player_age=player_value.find_previous_sibling('td').text

    previous_club=block_odd.findAll('td',class_='hauptlink')[1]
    previous_club=previous_club.a.text
    new_club=block_odd.findAll('td',class_='hauptlink')[2]
    new_club=new_club.a.text
    transfer_fee=block_odd.findAll('td',class_='rechts')[1]
    transfer_fee=transfer_fee.text
    ptab=block_odd.find('table',class_= "inline-table")
    player_position=ptab.findAll('td')[2].text
    player_nationality=block_odd.findAll('img',{'class':'flaggenrahmen'})
    player_countries=[]
    for i in player_nationality[:1]:
        player_countries.append(i.get('title'))
    player_countries=''.join(player_countries)
    player_data = {
            "name" : player_name,
            "age" :player_age ,
            "country":player_countries,
            "previous_team":previous_club,
            "new_team":new_club,
            "value":player_value,
            "transfer_fee":transfer_fee,
            "Posts":player_position,
        }
    players_data.append(players_data)

for block_even in blocks_even:
    player_name=block_even.find('img',{'class':'bilderrahmen-fixed lazy lazy'}).get('title')
    player_value=block_even.find('td',class_='rechts')
    player_age=player_value.find_previous_sibling('td').text

    previous_club=block_even.findAll('td',class_='hauptlink')[1]
    previous_club=previous_club.a.text
    new_club=block_even.findAll('td',class_='hauptlink')[2]
    new_club=new_club.a.text
    transfer_fee=block_even.findAll('td',class_='rechts')[1]
    transfer_fee=transfer_fee.text
    ptab=block_even.find('table',class_= "inline-table")
    player_position=ptab.findAll('td')[2].text
    player_nationality=block_even.findAll('img',{'class':'flaggenrahmen'})
    player_countries=[]
    for i in player_nationality[:1]:
        player_countries.append(i.get('title'))
    player_countries=''.join(player_countries)
    player_data = {
            "name" : player_name,
            "age" :player_age ,
            "country":player_countries,
            "previous_team":previous_club,
            "new_team":new_club,
            "value":player_value,
            "transfer_fee":transfer_fee,
            "Posts":player_position,
        }
    players_data.append(players_data)
print(players_data)

df=pd.concat([df,pd.DataFrame(players_data)])
df.to_csv('final.csv',index=False)
