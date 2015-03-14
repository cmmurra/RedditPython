#!/bin/usr/python2.7

import time
import praw
r = praw.Reddit('GameDeals List Checker v0.1 by /u/Chubclub')

r.login()
already_done = []
prawWords = ['Counter-Strike', 'counter-strike', 'hotline miami',
'Hotline Miami']

while True:
	subreddit = r.get_subreddit('gamedeals')
	for submission in subreddit.get_hot(limit=10):
	# test if it contains a game I want
		op_text = submission.title.lower()
		has_praw = any(string in op_text for string in prawWords)
		if submission.id not in already_done and has_praw:
			msg = '[Games I want](%s)' % submission.short_link
			r.send_message('chubclub','Games I want', msg)
			already_done.append(submission.id)
time.sleep(18000)
