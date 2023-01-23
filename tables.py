import csv
import time

from bs4 import BeautifulSoup
import requests
import pandas as pd

company_names=[]
skills=[]
html_text = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
content=BeautifulSoup(html_text,"lxml")
for i in content.find_all("li", class_='clearfix job-bx wht-shd-bx'):
        string=i.find('h3', class_='joblist-comp-name').text.replace(' ', '')
        company_names.append(string.strip())
        string2=i.find("span", class_='srp-skills').text.replace(' ', '')
        skills.append(string2.strip())
file_name='datata.csv'
with open(file_name,'w',encoding="utf-8")as f:
        f.write=csv.writer(f)
        f.write.writerow(['No.,Company Name,Skills'])
        for i in range(len(skills)):
                f.write.writerow([i+1,company_names[i],skills[i]])

