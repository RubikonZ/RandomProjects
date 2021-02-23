# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import lxml
from lxml import etree
import requests

url = requests.get('https://playoverwatch.com/en-us/career/pc/Rubikon-2275/')  # Hardcoded link

# soup = BeautifulSoup(html_doc, 'html.parser')
parsed_page = etree.HTML(url.text)
x = parsed_page.xpath("""//*[@id="competitive"]/section[3]/div/div""")
heroes_to_parse = len(x) - 1
print(type(x))

for heroes in range(heroes_to_parse):
    y = parsed_page.xpath("""//*[@id="competitive"]/section[3]/div/div[{}]/div""".format(str(heroes + 2))) #adding 2 because range starts at 0 and first hero starts at 2
    categories_to_parse = len(y)
    hero_num = parsed_page.xpath("""//*[@id="competitive"]/section[3]/div/div[{}]""".format(str(heroes + 2)))[0].attrib.get('data-category-id')
    hero = hero_id[hero_num]
    stats[hero] = {}

def get_rating():
    for div in soup.find_all('div'):
        # print(type(div.get('class')))
        if isinstance(div.get('class'), list):
            if div.get('class')[0] == "competitive-rank-level":
                rating = div.get_text()
                print(div.get_text())
                break


def get_top_heroes():
    hero_hours = []
    # print(soup.find(id='competitive').div.prettify())
    for div in soup.find_all('div'):
        if div.get('class') == 'competitive':
            # if isinstance(div.get('class'), list):
            print(div)
            if div.get('class')[0] == "ProgressBar-title" or div.get('class')[0] == "ProgressBar-description":
                print(div)
                print(type(div.get('class')))
                hero_hours.append(div.get_text())
    print(hero_hours)

def get_top_heroes2():
    kik = soup.find('div', id='competitive')
    kek = soup.find_all('div', 'ProgressBar-textWrapper')
    for k in kek:
        print(k)

    print(kik)
    print(type(soup), type(kek), type(k))



def write_to_json():
    with open('player_database.json', 'w+') as file:
        get_rating()
        get_top_heroes()

def input_battle_tag():
    pass

# print(soup.find(id='competitive').prettify())
# get_top_heroes2()
# get_rating()