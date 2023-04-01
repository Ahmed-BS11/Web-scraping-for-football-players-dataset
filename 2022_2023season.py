import requests
from bs4 import BeautifulSoup
from csv import writer


with open('DebutFin2011_2012.csv', 'a', newline='', encoding='utf8') as file:
        thewriter = writer(file)
        header = ['name', 'age', 'position', 'Country', 'MarketValue', 'PreviousTeam', 'LeagueOfPreviousTeam', 'CountryOfPreviousTeam', 'Fee', 'YearOfTranfert', 'NewTeam', 'LeagueOfNewTeam', 'CountryOfNewTeam',
                  'Height', 'Agent', 'JoinedCurrentTeam', 'ContratExpires', 'Squad', 'Appearances', 'PPG', 'Goals', 'Assists', 'OwnGoals', 'SubsON', 'SubsOFF', 'YellowCards', 'SecondYellowCards', 'RedCards', 'PenaltyGoals', 'MinutesPerGoal', 'MinutesPlayed', 'PlaceOfBirth', 'DateOfBirth']  # les noms des colonnes du fichier
        #thewriter.writerow(header)  # first row contains the header values

        for num_page in range(74, 81):
                URL = f"https://www.transfermarkt.com/transfers/saisontransfers/statistik/top/plus/1/galerie/0?saison_id=2011&page=" + \
                    str(num_page)
                # solution to 403 forbidden
                HEADERS = {
                    'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}

                response = requests.get(URL, headers=HEADERS)
                print(response)

                # the whole page content
                soup = BeautifulSoup(response.content, 'html.parser')
                # print(soup.prettify()) #Ou bien tt simplement print(response.text)

                # Debut jiben URLS
                keysS = soup.find('div', class_='keys').find_all('span')
                # print(keysS[7].text)
                keys = [keys.text for keys in
                        keysS]  # liste contient les numeros des joueurs qui apparaissent dans la page.
                # print(keys)

                rows = soup.find('table', class_='items').find('tbody')
                namesS = [row.find('a') for row in rows if row.find('a') != -1]
                names = [names.text for names in
                         namesS]  # liste contient les noms des joueurs qui apparaissent dans la page.
                # print(names)
                D = {" ": "", "ä": "a", "ç": "c", "è": "e", "º": "", "Ã": "A", "Í": "I", "í": "i", "Ü": "U", "â": "a",
                     "ò": "o", "¿": "", "ó": "o", "á": "a", "à": "a", "õ": "o", "¡": "", "Ó": "O", "ù": "u", "Ú": "U",
                     "´": "", "Ñ": "N", "Ò": "O", "ï": "i", "Ï": "I", "Ç": "C", "À": "A", "É": "E", "ë": "e", "Á": "A",
                     "ã": "a", "Ö": "O", "ú": "u", "ñ": "n", "é": "e", "ê": "e", "·": "-", "ª": "a", "°": "", "ü": "u",
                     "ô": "o", "ć": "c", "'": ""}
                listURL = []
                for name, key in zip(range(len(names)), range(len(keys))):
                    url = "https://www.transfermarkt.com/" + str(names[name]).replace('.', '-') + "/leistungsdatendetails/spieler/" + str(
                        keys[key]) + "/saison/2011/verein/0/liga/0/wettbewerb//pos/0/trainer_id/0/plus/1"
                    for ghalet, shyh in D.items():
                        url = url.replace(ghalet, shyh)
                    listURL.append(url)
                # print(listURL)
                # Fin jiben URLS

                table = soup.find('table', class_='items')
                if table is not None:
                        rows = table.find('tbody')
                # print(rows)

                # names = [row.find('a') for row in rows if row.find('a')!= -1]
                td = [row.find_all('td')
                                   for row in rows if row != '\n']  # find all td
                 # print(td[0])
                a = [row.find_all('a') for row in rows if row != '\n']
                # print(a[0])
                img = [row.find_all('img') for row in rows if row != '\n']
                 # print(img[1][-3])
                 # names1 = [row.find('img').get('title') for row in rows if row.find('a')!= -1]

                for i, j, k in zip(range(len(td)), range(len(a)), range(len(img))):
                        name = td[i][3].text.replace('\n', "")
                        age = td[i][5].text.replace('\n', "")
                        position = td[i][4].text.replace('\n', "")
                        MarketValue = td[i][6].text.replace('\n', "")
                        Fee = td[i][-1].text.replace('\n', "")
                        PreviousTeam = a[j][1].get('title').replace('\n', "")
                        LeagueOfPreviousTeam = a[j][3].get(
                            'title').replace('\n', "")
                        NewTeam = a[j][4].get('title').replace('\n', "")
                        LeagueOfNewTeam = a[j][-1].text.replace('\n', "")
                        Country = img[k][1].get('alt').replace('\n', "")
                        CountryOfPreviousTeam = img[k][-3].get(
                            'alt').replace('\n', "")
                        CountryOfNewTeam = img[k][-1].get(
                            'alt').replace('\n', "")
                        YearOfTransfert = "2011"
                        autreURL = listURL[i]
                        print(autreURL)
                        response = requests.get(autreURL, headers=HEADERS)
                        # print(response)
                        soupp = BeautifulSoup(response.content, 'html.parser')

                        dataheadercontent = soupp.find_all(
                            'span', class_='data-header__content')
                        height = soupp.find('span', itemprop='height')
                        if height != None:
                                Height = height.text.replace('\n', "")
                        else:
                                Height = "NONE"

                        agent = soupp.find(
                            'span', class_='data-header__content data-header__content--vertical-aligned')
                        if agent != None:
                                Agent = agent.text.replace('\n', "")
                        else:
                                Agent = "NONE"

                        #JoinedCurrentTeam = dataheadercontent[1].text.replace('\n', "")
                        try:
                            JoinedCurrentTeam = dataheadercontent[1].text.replace('\n',"")
                            ContratExpires = dataheadercontent[2].text.replace('\n',"")
                            PlaceOfBirth = dataheadercontent[4].text.replace('\n',"")
                            DateOfBirth = dataheadercontent[3].text.replace('\n',"")
                        except IndexError:
                            # Handle the situation when the index is out of range
                            #print("Error: The dataheadercontent list does not contain at least two elements")
                            JoinedCurrentTeam = ""
                            ContratExpires = ""
                            PlaceOfBirth= ""
                            DateOfBirth= ""

                        
                        TD = soupp.find_all('td', class_="zentriert")

                        if TD != []:

                                Squad = TD[0].text.replace("-","0").replace('\n', "")
                                Appearances = TD[1].text.replace("-","0").replace('\n', "")
                                PPG = TD[2].text.replace("-","0").replace('\n', "")
                                Goals = TD[3].text.replace("-","0").replace('\n', "")
                                Assists = TD[4].text.replace("-","0").replace('\n', "")
                                OwnGoals = TD[5].text.replace("-","0").replace('\n', "")
                                SubsON = TD[6].text.replace("-","0").replace('\n', "")
                                SubsOFF = TD[7].text.replace("-","0").replace('\n', "")
                                YellowCards = TD[8].text.replace("-","0").replace('\n', "")
                                SecondYellowCards = TD[9].text.replace("-","0").replace('\n', "")
                                RedCards = TD[10].text.replace("-","0").replace('\n', "")
                                PenaltyGoals = TD[11].text.replace("-","0").replace('\n', "")

                        else:
                                Squad = "NONE"
                                Appearances = "NONE"
                                PPG = "NONE"
                                Goals = "NONE"
                                Assists = "NONE"
                                OwnGoals = "NONE"
                                SubsON = "NONE"
                                SubsOFF = "NONE"
                                YellowCards = "NONE"
                                SecondYellowCards = "NONE"
                                RedCards = "NONE"
                                PenaltyGoals = "NONE"


                        TDD =soupp.find_all('td',class_="rechts")
                        try:
                                MinutesPerGoal = TDD[1].text.replace("-","0").replace('\n', "")
                                MinutesPlayed = TDD[2].text.replace("-","0").replace('\n', "")

                        except IndexError:
                                MinutesPerGoal = "NONE"
                                MinutesPlayed = "NONE"
                        if(Goals==0):
                               MinutesPerGoal="-"
                        dataset = [name, age, position, Country, MarketValue,PreviousTeam, LeagueOfPreviousTeam,CountryOfPreviousTeam, Fee, YearOfTransfert, NewTeam, LeagueOfNewTeam, CountryOfNewTeam,
                                   Height,Agent,JoinedCurrentTeam,ContratExpires,Squad,Appearances,PPG,Goals,Assists,OwnGoals,SubsON,SubsOFF,YellowCards,SecondYellowCards,RedCards,PenaltyGoals,MinutesPerGoal,MinutesPlayed,PlaceOfBirth,DateOfBirth]
                        thewriter.writerow(dataset) #ajouter chaque ligne au fichier csv

