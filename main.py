from bs4 import BeautifulSoup

with open('home.html','r') as html_file:
    content=html_file.read()
    soup = BeautifulSoup(content,'lxml')
    tags=soup.find_all('section')
    for tag in tags:
        tag_name=tag.h2.text
        tag_price=tag.p.text.split()[-1]

        print(f'{tag_name} costs {tag_price}')
