#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tweepy
import time, sys, random
import auth
print "OK GOOD START TEAM!"

argfile = str(sys.argv[1])

CONSUMER_KEY = 'Mg2JY9DS9qSQcEjAIBrR97gFh' 
CONSUMER_SECRET = auth.CONSUMER_SECRET
ACCESS_TOKEN = '752964356187357184-WrLmQXh7Vy2ucUNXmH7sZwatOvLhRGa'
ACCESS_SECRET =  auth.ACCESS_SECRET
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

filename = open(argfile, 'r')
f = filename.readlines()
filename.close()
random.shuffle(f)

for line in f:
    api.update_status(line)
    print line
    time.sleep(900)
