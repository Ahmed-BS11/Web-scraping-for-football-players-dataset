from pickle import NONE
import time
import pandas as pd
from bs4 import BeautifulSoup
import requests

def extract_source(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    source=requests.get(url, headers=headers).text
    return source

html_text=extract_source("https://sofifa.com/players?r=220069&set=true")
soup = BeautifulSoup(html_text, 'html.parser')
player_list=[]
player_data={}
players=soup.find_all('tr')
def controle(x):
    if x is not None:
        x=x.text
    return x

www=players[0]

for player in players:  
    if player!=www:
        player_name=player.find('div',class_='ellipsis')
        player_name=controle(player_name)

        player_age=player.find('td',class_='col-ae')
        player_age=controle(player_age)


        player_team=player.find('figure',class_="avatar avatar-sm transparent").next_sibling.next_sibling
        player_team=controle(player_team)

        player_value=player.find('td',class_='col-vl')
        player_value=controle(player_value)

        player_contract=player.find('div',class_='sub')
        player_contract=controle(player_contract)
        player_contract=player_contract[1:]

        player_post=[]
        player_posts=player.find_all('span',class_='pos')
        for i in player_posts:
            i=i.text
            player_post.append(i)

        player_data = {
            "name" : player_name,
            "age" :player_age,
            "team":player_team,
            "value":player_value,
            "contract":player_contract,
            "Posts":player_post,
        }
        player_list.append(player_data)

df = pd.DataFrame(player_list)
print(df.head())
df.to_csv('datadata.csv',index=False)

#print(player_list)
