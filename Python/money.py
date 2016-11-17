#!/usr/bin/python
# Checks a give set of users balances
# and texts the answers to the specified phone number

import requests
import os
import sys
import sqlite3
from bs4 import BeautifulSoup
from twilio.rest import TwilioRestClient
from time import sleep

# Read in users
users= []
f = open('creds.txt')
for line in f:
	tmp = line.split()
	users += [(tmp[0], tmp[1])]
f.close()

# Connect to our database
db = sqlite3.connect('balances.db')
c = db.cursor()
c.execute("CREATE TABLE IF NOT EXISTS users (user TEXT, balance INT, UNIQUE(user))")
db.commit()

#Set Headers
headers = {
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Accept-Encoding':'gzip, deflate, sdch, br',
	'Accept-Language':'en-US,en;q=0.8',
	'Cache-Control':'max-age=0',
	'Upgrade-Insecure-Requests':'1'
	}

print("-------------------------")
cookie_jar = {}
updated = []
#Create a Session
s = requests.Session()
s.headers.update(headers)
for user in users:
	print("[--]Checking %s" % user[0])
	#Inital get request to populate cookies
	r = s.get('https://shareeek.com/')

	#Html Parser
	soup = BeautifulSoup(r.content, 'html.parser')

	cookie_jar['_ga'] = "GA1.2.452462395.1472660623"
	cookie_jar['_gat'] = '1'
	_token = soup.input['value']

	#Prepping data to be posted
	# -------------------------------------------------------------------------------------------------------
	data_jar = {'password': user[1],'email': user[0],'_token':_token}
	# -------------------------------------------------------------------------------------------------------

	#Add new headers
	headers['Content-Type'] = 'application/x-www-form-urlencoded'
	headers['Referer'] = 'https://shareeek.com/'
	s.headers.update(headers)

	#Post the login information
	r = s.post('https://shareeek.com/login', cookies=cookie_jar, data=data_jar)

	#Pretend to watch an add before submitting the survey request

	balance_page = s.get("https://shareeek.com/my")
	soup = BeautifulSoup(balance_page.content, 'html.parser')
	balance = soup.find("h1", {"class": "text-center"}).string
	balance = balance.replace("$", "")
	print("[--]Balance %s" % balance)

	c.execute("SELECT balance FROM users WHERE user=?", (user[0],))
	prev_balance = c.fetchone()

	if not prev_balance:
		print("[--]Adding user into database")
		c.execute("INSERT INTO users VALUES (?, ?)", (user[0], balance))
		db.commit()
	else:
		prev_balance = prev_balance[0]
		if int(prev_balance) < int(balance):
			c.execute("UPDATE users SET balance=? WHERE user=?", (balance, user[0]))
			db.commit()
			print("[--]%s won" % user[0])
			updated += [user[0]]

		else:
			print("[--]No change")

# Send SMS messages
if not updated:
	print("[--]Done")
	sys.exit(0)

f = open('tokens.txt')
for line in f:
	tmp = line.split()
	account_sid = tmp[0]
	auth_token = tmp[1]
f.close()
print("[--]Sending updated users")
client = TwilioRestClient(account_sid, auth_token)
winners = ','.join(x for x in updated)
message = client.messages.create(to="+12072813940", from_="+15852964222",
                                     body="%s won today" % winners)
print("[--]Done")
