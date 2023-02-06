from pickle import NONE
import time
import pandas as pd
from bs4 import BeautifulSoup
import requests


def extract_source(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    source = requests.get(url, headers=headers).text
    return source


def controle(x):
    if x is not None:
        x = x.text
    return x


Years = [2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014,
         2013, 2012, 2011, 2010, 2009, 2008, 2007, 2006, 2005]
df = pd.DataFrame()
for year in range(len(Years)):

    for pagenum in range(1, 81):
            
        html_text = extract_source(
            f"https://www.transfermarkt.com/transfers/saisontransfers/statistik/top/plus/1/galerie/0?saison_id={Years[year]}&transferfenster=alle&land_id=&ausrichtung=&spielerposition_id=&altersklasse=&leihe=&page="+str(pagenum))
        soup = BeautifulSoup(html_text, 'html.parser')

        blocks_odd = soup.find_all('tr', class_='odd')
        blocks_even = soup.find_all('tr', class_='even')
        players_data = []

        for block_odd in blocks_odd:
            player_name = block_odd.find(
                'img', {'class': 'bilderrahmen-fixed lazy lazy'}).get('title')
            player_value = block_odd.find('td', class_='rechts')
            player_age = player_value.find_previous_sibling('td').text
            player_value = player_value.text
            previous_club = block_odd.findAll('td', class_='hauptlink')[1]
            previous_club = previous_club.a.text
            new_club = block_odd.findAll('td', class_='hauptlink')[2]
            new_club = new_club.a.text
            transfer_fee = block_odd.findAll('td', class_='rechts')[1]
            transfer_fee = transfer_fee.text
            ptab = block_odd.find('table', class_="inline-table")
            player_position = ptab.findAll('td')[2].text
            player_nationality = block_odd.findAll(
                'img', {'class': 'flaggenrahmen'})
            player_countries = []
            for i in player_nationality[:1]:
                player_countries.append(i.get('title'))
            player_countries = ''.join(player_countries)
            player_data = {
                "name": player_name,
                "age": player_age,
                "country": player_countries,
                "previous_team": previous_club,
                "new_team": new_club,
                "value": player_value,
                "transfer_fee": transfer_fee,
                "Posts": player_position,
            }
            players_data.append(player_data)

        for block_even in blocks_even:
            player_name = block_even.find(
                'img', {'class': 'bilderrahmen-fixed lazy lazy'}).get('title')
            player_value = block_even.find('td', class_='rechts')
            player_age = player_value.find_previous_sibling('td').text
            player_value = player_value.text
            previous_club = block_even.findAll('td', class_='hauptlink')[1]
            previous_club = previous_club.a.text
            new_club = block_even.findAll('td', class_='hauptlink')[2]
            new_club = new_club.a.text
            transfer_fee = block_even.findAll('td', class_='rechts')[1]
            transfer_fee = transfer_fee.text
            ptab = block_even.find('table', class_="inline-table")
            player_position = ptab.findAll('td')[2].text
            player_nationality = block_even.findAll(
                'img', {'class': 'flaggenrahmen'})
            player_countries = []
            for i in player_nationality[:1]:
                player_countries.append(i.get('title'))
            player_countries = ''.join(player_countries)
            player_data = {
                "name": player_name,
                "age": player_age,
                "country": player_countries,
                "previous_team": previous_club,
                "new_team": new_club,
                "value": player_value,
                "transfer_fee": transfer_fee,
                "Posts": player_position,
            }
            players_data.append(player_data)
        #print(Years[year], pagenum)
        #print(players_data)

    df = pd.concat([df, pd.DataFrame(players_data)])

df.to_csv('Final_DataSet.csv', index=False)
