# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 14:13:04 2022

@author: Mo-t
"""
from bs4 import BeautifulSoup as BS
import requests
import pandas as pd
import os
from gtts import gTTS
os.chdir(r'Z:\Projects\Py to yourtube')




Title = 'Need Extra Income? Take Your Pick'

text_intro = open("text_intro.txt", "r")
Intro = text_intro.read()
text_intro.close()


#%% Web Scraper
url = "http://thepennyhoarder.com"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
page = requests.get(url, headers=headers)
soup = BS(page.content, 'html.parser')

pagelink='https://www.thepennyhoarder.com/make-money/side-gigs/best-side-hustles/?=undefined'
# input('Paste Page Link: \n')

page = requests.get(pagelink, headers=headers)

soup = BS(page.content, 'html.parser')
alltext=soup.find("div", {"class":"col-xs-12 single-post-content-inner hub-page"})
alltext=alltext.find_all("p")

alldata=[]
for i in alltext:
    temp=i.get_text()
    alldata.append(temp) 
    
data = pd.DataFrame(alldata, columns=['Title'])

#%% Text - To - Speach
os.chdir(r'Z:\Projects\Py to yourtube')



tts = gTTS(Intro, lang='en', tld='co.uk')
tts.save('hello.mp3')

data.to_csv('scrape.csv')


print(os.getcwd())