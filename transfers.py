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

html_text=extract_source("https://www.transfermarkt.com/transfers/saisontransfers/statistik?land_id=0&ausrichtung=&spielerposition_id=&altersklasse=&leihe=&transferfenster=alle&saison-id=0&plus=6/page=5")
soup = BeautifulSoup(html_text, 'html.parser')

Players_data=[]
player_list=[]
ages=[]
countries_list=[]
positions_list=[]
values_list=[]

player_data={}

player_name=soup.find_all('img',{'class':'bilderrahmen-fixed lazy lazy'})
player_age=soup.find_all('td',class_='zentriert')
Age = soup.find_all("td", {"class": "zentriert"})
Positions = soup.find_all("td", {"class": ["zentriert rueckennummer bg_Torwart",
                                            "zentriert rueckennummer bg_Abwehr",
                                            "zentriert rueckennummer bg_Mittelfeld",
                                            "zentriert rueckennummer bg_Sturm"]})
Nationality =soup.find_all("img", {"class": "flaggenrahmen"})
Values= soup.find_all("td", {"class": "rechts hauptlink"})
for i in Nationality:
    countries_list.append(i.get('title'))
    print(i.get('title'))
for i in range(0, len (player_name)):
    player_list.append(str(player_name [i]).split('" class',1) [0].split('<img alt="', 1) [1] )
    
for i in range (1, (len (player_name)*4), 4):
    ages.append(str(player_age[i].text))#.split("(",1) [0].split(")",1)[0])
for i in range(0, len(Positions)):
    positions_list.append(str(Positions[i].text))#.split('title="', 1) [0].split('"><div')[0])
#for i in range (0, (len (Nationality))):
 #   countries_list.append(str (Nationality[i].get('title')))#.split('title="', 1) [0].split('"/',1)[0])
for i in range(0, len (Values)):
    values_list.append (Values [i].text)
"""
for i in range(0,len(player_list)):
    player_data = {
                "name" : player_list[i],
                "age" :ages [i],
                "country":countries_list[i],
                #"team":player_team,
                #"rating":player_rating,
                "value":values_list[i],
                #"wage":player_wage,
                #"contract":player_contract,
                #"Posts":positions_list[i],
            }
    Players_data.append(player_data)
"""

print(len(player_list),'///',len(ages),'///',len(countries_list),'///',len(values_list),'//',len(positions_list))
final_df=pd.DataFrame({
                "name" : player_list,
                "age" :ages ,
                "country":countries_list,
                #"team":player_team,
                #"rating":player_rating,
                #"value":values_list,
                #"wage":player_wage,
                #"contract":player_contract,
               # "Posts":positions_list,
            })
final_df.to_csv('lisss.csv',index=False)
















"""for link in pagination_links:
    page_url = url + link["href"]
    page_response = requests.get(page_url)
    page_soup = BeautifulSoup(page_response.text, "html.parser")
    
    # Extract the required data from the HTML source code of each page
    ...
"""