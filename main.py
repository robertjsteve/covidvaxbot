# -*- coding: utf-8 -*-
  
##
##         @author: Robert Steve
##         @date created: January 16th, 2021
##         @date last modified: January 18th, 2021
##      
##              Vaccine appointment notification twitter bot.
##
##


import random
import datetime
import tweepy 
import requests
import time
from bs4 import BeautifulSoup
import pytz
from datetime import datetime

global headers

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

consumer_key = '' 
consumer_secret = '' 
access_token = '' 
access_token_secret = '' 


auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def init(shoprite, middlesex, morris, burlington):
    
    #Hunterdon Health Dept
    hunterdon_url = "https://www.signupgenius.com/go/10c0d44a4af23a3f5c25-covid"
    hunterdon_response = requests.get(hunterdon_url, headers=headers)
    hunterdon_soup = BeautifulSoup(hunterdon_response.text, "lxml")
    hunterdon_initcount = str(hunterdon_soup).count("Already filled")
    
    check(shoprite, middlesex, morris, burlington, hunterdon_initcount)
    return 0


def tweet(option):
    tz_NY = pytz.timezone('America/New_York') 
    datetime_NY = datetime.now(tz_NY)
    time = datetime_NY.strftime("%H:%M:%S")


    if option == "hunterdon":
        tweet = "({} EST) ALERT 🚨: Possible availability at the Hunterdon Health Department:\nhttps://www.signupgenius.com/go/10c0d44a4af23a3f5c25-covid".format(time)
        api.update_status(tweet)
        init(True, True, True, True)
        return 0
    elif option == "sr":
        tweet = "({} EST) ALERT 🚨: Possible availability at Shoprite:\nhttps://vaccines.shoprite.com/".format(time)
        api.update_status(tweet)
        init(False, True, True, True)
        return 0

    elif option == "middlesex":
        tweet = "({} EST) ALERT 🚨: Possible availability in Middlesex County:\nhttps://app.acuityscheduling.com/schedule.php?owner=19830283".format(time)
        api.update_status(tweet)
        init(True, False, True, True)
        return 0

    elif option == "morris":
        tweet = "({} EST) ALERT 🚨: Possible availability in Morris County:\nhttps://www.atlantichealth.org/conditions-treatments/coronavirus-covid-19/covid-vaccine/schedule-vaccine-appointment.html".format(time)
        api.update_status(tweet)
        init(True, True, False, True)
        return 0

    elif option == "burlington":
        tweet = "({} EST) ALERT 🚨: Possible availability in Burlington County:\nhttps://boydsrxs.com/".format(time)
        api.update_status(tweet)
        init(True, True, True, False)
        return 0

    elif


def check(shoprite, middlesex, morris, burlington, hunterdon_initcount):
    while True:

        #Hunterdon Health Dept
        hunterdon_url = "https://www.signupgenius.com/go/10c0d44a4af23a3f5c25-covid"
        hunterdon_response = requests.get(hunterdon_url, headers=headers)
        hunterdon_soup = BeautifulSoup(hunterdon_response.text, "lxml")
        hunterdon_newcount = str(hunterdon_soup).count("Already filled")

        #Shoprite Locations
        sr_url = "https://vaccines.shoprite.com/"
        sr_response = requests.get(sr_url, headers=headers)
        sr_soup = BeautifulSoup(sr_response.text, "lxml")

        #Middlesex County
        middlesex_url = "https://app.acuityscheduling.com/schedule.php?owner=19830283"
        middlesex_response = requests.get(middlesex_url, headers=headers)
        middlesex_soup = BeautifulSoup(middlesex_response.text, "lxml")

        #Morris County
        morris_url = "https://www.atlantichealth.org/conditions-treatments/coronavirus-covid-19/covid-vaccine/schedule-vaccine-appointment.html"
        morris_response = requests.get(morris_url, headers=headers)
        morris_soup = BeautifulSoup(morris_response.text, "lxml")

        #Burlington County
        burlington_url = "https://boydsrxs.com/"
        burlington_response = requests.get(burlington_url, headers=headers)
        burlington_soup = BeautifulSoup(burlington_response.text, "lxml")
        
        if hunterdon_newcount > hunterdon_initcount:
            hunterdon_initcount = hunterdon_newcount

        if hunterdon_newcount < hunterdon_initcount:
            tweet("hunterdon")

        if str(sr_soup).count("there are currently no new appointments available") == 0 and shoprite == True:
            tweet("sr")

        if str(middlesex_soup).count("Online registration is at capacity") == 0 and middlesex == True:
            tweet("middlesex")

        if str(morris_soup).count("AT THIS TIME, THERE ARE NO APPOINTMENTS AVAILABLE.") == 0 and morris == True:
            tweet("morris")

        if str(burlington_soup).count("We have no available appointments for the COVID-19 vaccine") == 0 and burlington == True:
            tweet("burlington")
            
        else:
            testtime = random.randint(0, 9) + 30
            time.sleep(testtime)
            print("Checking...")
            continue
    return 0

init(True, True, True, True)
    
