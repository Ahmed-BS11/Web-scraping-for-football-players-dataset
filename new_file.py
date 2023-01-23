import time
import pandas as pd
from bs4 import BeautifulSoup
import requests

html_text=requests.get("https://sofifa.com/players?r=220069&set=true").text
soup = BeautifulSoup(html_text, 'lxml')
player_list=[]
alll=soup.find('table',class_='table table-hover persist-area')
print(soup.prettify())
players=soup.find('tr')
for player in players:
    player_name=player.find('div',class_='ellipsis')
    print(player_name)
    player_age=player.find('td',class_='col-ae')
    player_team=player.find("a")
    player_value=player.find('td',class_='col-vl')
    player_contract=player.find('div',class_='sub')
    player_list.append([player_name,player_age,player_team,player_value,player_contract])

#print(player_stats())
