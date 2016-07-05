#!/usr/bin/env python
import tweepy, sys, time
from TwitterAPI import TwitterAPI
from random import randint
from keys import keys
# import gethandlesfromhtml
import krowdkrawl
from itertools import cycle
 
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN_KEY = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']
 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
tweepy_api = tweepy.API(auth)
twitter_api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
 
# get_handles(sys.argv[1])
messages_tuple = ("Teaching Juno to chase sling-shotted objects! https://youtu.be/w-hze-8exT8", "Teaching Juno to run in a specific direction https://youtu.be/w-hze-8exT8")

message_cycle = cycle(range(len(messages_tuple)))

with open("h.txt", "r") as f:
	h = f.readlines()
	for i in h:
		m = (i + " " + messages_tuple[message_cycle.next()].replace('\n', ''))
		print m
		# tweepy_api.update_status(m)
		file = open('Juno.jpg', 'rb')
		data = file.read()
		r = twitter_api.request('statuses/update_with_media', {'status':m}, {'media[]':data})
		nap = randint(1, 60*7)
		time.sleep(nap)

# for handle in krowdkrawl.crawl_krowd(1):
# 	m = (handle + " " + messages_tuple[message_cycle.next()].replace('\n', ''))
# 	print m
# 	api.update_status(m)
# 	nap = randint(1, 60*7)
# 	time.sleep(nap)

