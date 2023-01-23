import time
import pandas as pd
from bs4 import BeautifulSoup
import requests

def player_stats():
    html_text=requests.get("https://sofifa.com/")
    soup = BeautifulSoup(html_text, 'lxml')
    player_list=[]
    players=soup.find_all('tr')
    for player in players:
        player_name=player.find('div',class_='ellipsis')
        player_age=player.find('td',class_='col-ae')
        player_team=player.find("a")
        player_value=player.find('td',class_='col-vl')
        player_contract=player.find('div',class_='sub')
        player_list.append([player_name,player_age,player_team,player_value,player_contract])
    return player_list

player_stats()
