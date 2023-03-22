import requests
from bs4 import BeautifulSoup
from csv import writer
from pickle import NONE
import time
import pandas as pd



#header = ['name', 'age', 'position', 'Country', 'MarketValue', 'PreviousTeam', 'LeagueOfPreviousTeam','CountryOfPreviousTeam', 'Fee', 'YearOfTranfert', 'NewTeam', 'LeagueOfNewTeam', 'CountryOfNewTeam', 'Height', 'Agent'] #les noms des colonnes du fichier
#thewriter.writerow(header) #first row contains the header values
df = pd.DataFrame()

for num_page in range(1, 2):
        URL = f"https://www.transfermarkt.com/transfers/saisontransfers/statistik/top/plus/1/galerie/0?saison_id=2022&page="+ str(num_page)
        HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}  # solution to 403 forbidden

        response = requests.get(URL, headers=HEADERS)
        print(response)

        soup = BeautifulSoup(response.content, 'html.parser')  #the whole page content
        # print(soup.prettify()) #Ou bien tt simplement print(response.text)




        #Debut jiben URLS
        keysS = soup.find('div', class_='keys').find_all('span')
        # print(keysS[7].text)
        keys = [keys.text for keys in
                keysS]  # liste contient les numeros des joueurs qui apparaissent dans la page.
        #print(keys)

        rows = soup.find('table', class_='items').find('tbody')
        namesS = [row.find('a') for row in rows if row.find('a') != -1]
        names = [names.text for names in
                    namesS]  # liste contient les noms des joueurs qui apparaissent dans la page.
        #print(names)
        D = {" ": "", "ä": "a", "ç": "c", "è": "e", "º": "", "Ã": "A", "Í": "I", "í": "i", "Ü": "U", "â": "a",
                "ò": "o", "¿": "", "ó": "o", "á": "a", "à": "a", "õ": "o", "¡": "", "Ó": "O", "ù": "u", "Ú": "U",
                "´": "", "Ñ": "N", "Ò": "O", "ï": "i", "Ï": "I", "Ç": "C", "À": "A", "É": "E", "ë": "e", "Á": "A",
                "ã": "a", "Ö": "O", "ú": "u", "ñ": "n", "é": "e", "ê": "e", "·": "-", "ª": "a", "°": "", "ü": "u",
                "ô": "o"}
        listURL = []
        for name, key in zip(range(len(names)), range(len(keys))):
            url = "https://www.transfermarkt.com/" + str(names[name]) + "/leistungsdatendetails/spieler/" + str(
                keys[key]) + "/saison/2021/verein/0/liga/0/wettbewerb//pos/0/trainer_id/0/plus/1"
            for ghalet, shyh in D.items():
                url = url.replace(ghalet, shyh)
            listURL.append(url)
        #print(listURL)
        #Fin jiben URLS


        table = soup.find('table', class_='items')
        if table is not None:
                rows = table.find('tbody')
        # print(rows)

        #names = [row.find('a') for row in rows if row.find('a')!= -1]
        td = [row.find_all('td') for row in rows if row != '\n']#find all td
            #print(td[0])
        a = [row.find_all('a') for row in rows if row != '\n']
        #print(a[0])
        img = [row.find_all('img') for row in rows if row != '\n']
            #print(img[1][-3])
            #names1 = [row.find('img').get('title') for row in rows if row.find('a')!= -1]

        for i, j, k in zip(range(len(td)), range(len(a)), range(len(img))):
            name = td[i][3].text.replace('\n', "")
            age = td[i][5].text.replace('\n', "")
            position = td[i][4].text.replace('\n', "")
            MarketValue = td[i][6].text.replace('\n', "")
            Fee = td[i][-1].text.replace('\n', "")
            PreviousTeam = a[j][1].get('title').replace('\n', "")
            LeagueOfPreviousTeam = a[j][3].get('title').replace('\n', "")
            NewTeam = a[j][4].get('title').replace('\n', "")
            LeagueOfNewTeam = a[j][-1].text.replace('\n', "")
            Country = img[k][1].get('alt').replace('\n', "")
            CountryOfPreviousTeam = img[k][-3].get('alt').replace('\n', "")
            CountryOfNewTeam = img[k][-1].get('alt').replace('\n', "")
            YearOfTransfert = "2022"
            autreURL = listURL[i]
            #print(autreURL)
            response = requests.get(autreURL, headers=HEADERS)
            #print(response)
            soupp = BeautifulSoup(response.content, 'html.parser')
            height = soupp.find_all('span', class_='data-header__content')
            #print(height[6].text)
            Height = height[6].text.replace('\n',"")
            agent = soupp.find('span', class_='data-header__content data-header__content--vertical-aligned')
            if agent != None :
                Agent = agent.text.replace('\n',"")
            else:
                Agent = "NONE"

            player_data = {
            "name": name,
            "age": age,
            "position":position,
            "country": Country,
            "MarketValue":MarketValue,
            "previous_team": PreviousTeam,
            "LeagueOfPreviousTeam":LeagueOfPreviousTeam,
            "CountryOfPreviousTeam":CountryOfPreviousTeam,
            "transfer_fee": Fee,
            "YearOfTransfert":YearOfTransfert,
            "NewTeam": NewTeam,
            "LeagueOfNewTeam":LeagueOfNewTeam,
            "CountryOfNewTeam": CountryOfNewTeam,
            "Height": Height,
            "Agent":Agent,
            }
            #dataset = [name, age, position, Country, MarketValue,PreviousTeam, LeagueOfPreviousTeam,CountryOfPreviousTeam, Fee, YearOfTransfert,  NewTeam, LeagueOfNewTeam, CountryOfNewTeam,Height,Agent]
            #thewriter.writerow(dataset)  #ajouter chaque ligne au fichier csv
            df = pd.concat([df, pd.DataFrame(player_data, index=[0])])

df.to_csv('2022season.csv', index=False)

