#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tweepy
import time, sys
print "OK GOOD START TEAM!"

argfile = str(sys.argv[1])

CONSUMER_KEY = 
CONSUMER_SECRET = 
ACCESS_KEY =
ACCESS_SECRET = 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename - open(argfile, 'r')
f = filename.readlines()
filename.close()

for line in f:
    api.update_status(line)
    time.sleep(900)
