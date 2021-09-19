# Write backend
# Convert APIs in this repo to Python Code
# Collect data list of all ufc fighters past/present : https://github.com/valish?tab=repositories
# Get data source

# Create SQL data types in SQL alchemy
# Set up SQL database
# Create table and ingest

# Write frontend to display data


# extract list of ufc fighters

import sys
import time
from bs4 import BeautifulSoup
import requests
import pprint
import pandas as pd
from selenium import webdriver


response = requests.get('https://www.ufc.com/athletes/all')

print(response)

soup = BeautifulSoup(response.content, 'html.parser')

# selenium logic

# options = webdriver.ChromeOptions()
# options.add_argument('headless')

################################################################################### SELENIUM LOGIC ####################################################################################

url = 'https://www.ufc.com/athletes/all'
driver = webdriver.Chrome(
    executable_path=r"C:\\Users\\Nick\\Desktop\\2021 Python\\MMadag\\Dags\\chromedriver.exe")
driver.get(url)
html = driver.page_source.encode('utf-8')
page_num = 0

xpath = '//*[@id="block-mainpagecontent"]/div/div/div[2]/div/div/ul/li/a'

# wait for cookies banner to load

time.sleep(4)

# click accept cookies
driver.find_element_by_id("onetrust-accept-btn-handler").click()

# load all the pages
while driver.find_element_by_xpath(xpath):
    time.sleep(1)
    driver.find_element_by_xpath(xpath).click()
    page_num += 1
    print("getting page num: " + str(page_num))
    time.sleep(1)
    name = soup.find_all('span', class_='c-listing-athlete__name', text=True)

print("finished!")

print(name)


# html = driver.page_source.encode('utf-8')

# soup = BeautifulSoup(response.content, 'html.parser')


################################################################################### PANDAS LOGIC ####################################################################################

# col_list = "column fighter_name	nickname	division	wins	losses	draws	win_by_ko	win_by_sub	win_by_dec	sig_str_acc	sig_str_landed	sig_str_attempt	grap_acc	td_landed	td_attempt	sgt_str_min	sig_str_abs	td_avg_per_15 sub_avg_per_15	sig_str_def	td_def	ko_ratio	avg_fight_time	sig_str_standing	sig_str_clinch	sig_str_ground	sig_str_head	sig_str_body	sig_str_leg	win_by_ko_tko	win_by_dec	win_by_sub"

# col_list = col_list.split()

# df = pd.DataFrame(col_list)


# dynamically add to df https://stackoverflow.com/questions/48030350/dynamically-add-rows-to-dataframe
# find fighter elements
# hover over fighter
# grab name, nickname, division, record
# store in data frame
# find athlete profile button.click
# create dataframe


name = soup.find_all('span', class_='c-listing-athlete__name', text=True)
print(name)
names_list = list(names)

# find a way to load the page as you scrape

# fetch data from one fighter to grab templates before creating csv


# find elements on soup page
