#!/usr/bin/python

#importing the requests modules to do basic get commands
import requests

from sys import argv

script, user, pswd, orig, term, msg  = argv

#we are going to ask user for the creds
#user = raw_input('username: ')
#pswd = raw_input('password: ')
#orig = raw_input('orig TN: ')
#term = raw_input('term TN: ')
#msg = raw_input('msg: ')
n = input('no. of mgs: ')

#set the sms-sender url

url = 'http://192.168.102.67:13013/cgi-bin/sendsms?username=%s&password=%s&\
to=%s&text=%s&from=%s' % (user, pswd, orig, msg, term)

while n > 0:
    get = requests.get(url)
    n = n -1
