import time

from bs4 import BeautifulSoup
import requests
import pandas as pd


html_text = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
content=BeautifulSoup(html_text,"lxml")
jobs = content.find_all("li", class_='clearfix job-bx wht-shd-bx')
data=[]
for row in jobs:
    data.append([cell.text for cell in row.find_all('h3',class_='joblist-comp-name')])
    #data.append([cell.text for cell in row.find("span", class_='srp-skills')])

df = pd.DataFrame(data)
print(df.head())

"""for index,job in enumerate(jobs):
        company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
        skill = job.find("span", class_='srp-skills').text.replace(' ', '')"""

