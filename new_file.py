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


for i in range(2):
    html_text=extract_source(f"https://sofifa.com/players?r=220069&offset={i*60}")
    soup = BeautifulSoup(html_text, 'html.parser')
    player_list=[]
    player_data={}
    players=soup.find_all('tr')

    www=players[0]

    for player in players:  
        if player!=www:
            player_name=player.find('div',class_='ellipsis')
            player_name=controle(player_name)

            player_age=player.find('td',class_='col-ae')
            player_age=controle(player_age)


            player_team=player.find('figure',class_="avatar avatar-sm transparent")
            if player_team is not None:
                player_team=player_team.next_sibling.next_sibling
            player_team=controle(player_team)

            player_country=player.find('img',class_="flag").get('title')
            print(player_country)
            #if player_country is not None:
             #   player_country=player_country.values()['title']
            #player_country=controle(player_country)
            

            player_rating=player.find('td',class_='col-oa')
            if player_rating is not None:
                player_rating=player_rating.span
            player_rating=controle(player_rating)

            player_value=player.find('td',class_='col-vl')
            player_value=controle(player_value)

            player_wage=player.find('td',class_='col-wg')
            player_wage=controle(player_wage)

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
                "country":player_country,
                "team":player_team,
                "rating":player_rating,
                "value":player_value,
                "wage":player_wage,
                "contract":player_contract,
                "Posts":player_post,
            }
            player_list.append(player_data)
    

    df=pd.concat([df,pd.DataFrame(player_list)])
    df.to_csv('test.csv',index=False)


#print(player_list)
