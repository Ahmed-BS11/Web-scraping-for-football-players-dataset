import time

from bs4 import BeautifulSoup
import requests

print('Put some unfamiliar skills')
unfamiliar_skills = input('>')
print(f'filtering out :{unfamiliar_skills}')

def find_jobs():
    html_text = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all("li", class_='clearfix job-bx wht-shd-bx')

    for index ,job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skill = job.find("span", class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']
            if unfamiliar_skills not in skill:
                with open(f'posts/{index}.txt','w') as f:

                    f.write(f'the company:{company_name.strip()}\n')
                    f.write(f"required skills:{skill.strip()}\n")
                    f.write(f"more info:{more_info.strip()}")
                print(f'file saved: {index}')

"""
if __name__=='__main__':
    while True:
        find_jobs()
        time_wait=5
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait*60)
"""
