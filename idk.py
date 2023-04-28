import csv
from kora.selenium import wd
from bs4 import BeautifulSoup
import time
import requests

start_url='https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
wd.get(start_url)
time.sleep(20)

def scrap():
    headers=['Name', 'Distance', 'Mass', 'Radius']
    star_data=[]
    for i in range(0,198):
        soup=BeautifulSoup(wd.page_source, 'html.parser')
        for ul_tag in soup.find_all('ul', attrs={'class', 'wikipedia'}):
            li_tag=ul_tag.find_all('li')
            temp_list=[]
            for index, li_tag in enumerate(li_tag):
                if index==0:
                    temp_list.append(li_tag.find_all('a')[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append('')
                star_data.append(temp_list)
            wd.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/table')
        with open('idk1.csv','w') as a:
            csv_writer=csv.writer(a)
            csv_writer.writerow(headers)
            csv_writer.writerow(star_data)