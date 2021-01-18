from selenium import webdriver
from bs4 import BeautifulSoup
import time,csv

start_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
browser = webdriver.Chrome('/Users/kalravmineshbhatt/Dropbox/My Mac (Jack’s MacBook Air)/Downloads/chromedriver')
browser.get(start_url)

time.sleep(10)

def Scrape():
    headers = ['NAME','Distance','Mass','Radius']
    PlanetData = []
    Soup = BeautifulSoup(browser.page_source, 'html.parser')

    browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()

    for ul_tag in Soup.find_all('tr'):
        temp_list = []
        li_tag = ul_tag.find_all('td')

        for index,li_tag in enumerate(li_tag):

            if index == 0:
                temp_list.append(li_tag.find_all('a')[0].contents[0])

            else:
                try:
                    temp_list.append(li_tag.contents[0])

                except:
                    temp_list.append('')
                    PlanetData.append(temp_list)  

    with open('scraper.csv','w') as f:
        csvWriter = csv.writer(f)
        csvWriter.writerow(headers)
        csvWriter.writerows(PlanetData)                

Scrape()