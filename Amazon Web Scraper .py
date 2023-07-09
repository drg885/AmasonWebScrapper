# Code Author: Norokh Nikita
# 09 07 2023

#!/usr/bin/env python
# coding: utf-8



#import libraries
from bs4 import BeautifulSoup
import requests
import time
import datetime

import smtplib


# connect to the amazon website
url = "https://www.amazon.com/Data-Analyst-T-Shirt-Women-Female/dp/B09RT4MZRD/ref=sr_1_6?crid=1V43ILABMBACV&keywords=data%2Banalyst%2Btshirt&qid=1688892480&sprefix=data%2Banalyst%2Btshir%2Caps%2C321&sr=8-6"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(url, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")
soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find(id='productTitle').get_text().strip()[1:]
price = soup2.select('.a-offscreen')[0].get_text().strip()

import datetime
today = datetime.date.today()

import csv
header = ['Title', 'Price', 'Date']
data = [title, price, today]

with open("AmazonWebScrapperDataset.csv", "w", newline='', encoding='UTF-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)



def track_price():
    url = "https://www.amazon.com/Data-Analyst-T-Shirt-Women-Female/dp/B09RT4MZRD/ref=sr_1_6?crid=1V43ILABMBACV&keywords=data%2Banalyst%2Btshirt&qid=1688892480&sprefix=data%2Banalyst%2Btshir%2Caps%2C321&sr=8-6"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id='productTitle').get_text()
    price = soup2.select('.a-offscreen')[0].get_text()
    
    price = price.strip()[1:]
    title = title.strip()
    
    import datetime
    today = datetime.date.today()
    
    import csv

    header = ['Title', 'Price', 'Date']
    data = [title, price, today]
    # Appending data to created csv - to track price changing

    with open("AmazonWebScrapperDataset.csv", "a+", newline='', encoding='UTF-8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
#         To notificate about price changing using email
    if(price < 25):
        send_mail()

def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    server.login('overcicado885@gmail.com','xxxxxxxxxxx')
    
    subject = "The Shirt you want is below $25! Now is your chance to buy!"
    body = "Nikita, This is the moment we have been waiting for. Now is your chance to pick up the shirt of your dreams. Don't mess it up! Link here: https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data+analyst+tshirt&qid=1626655184&sr=8-3"
   
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'overcicado885@gmail.com',
        msg
     )

# To run it background and track price through time (every 24 hours)
while(True):
    track_price()
    time.sleep(86400)




