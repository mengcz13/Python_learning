# -*- coding: utf-8 -*-
import urllib
from bs4 import BeautifulSoup

#get the url
print 'Input the word you want to look up in merriam-webster dictionary online:'
dicurl = raw_input()
dicurl = 'http://www.merriam-webster.com/dictionary/'+dicurl

print '-----------------------------------'
print 'Here are the raw materials:'
print '-----------------------------------'

#fetch the html source code and analyse with BeautifulSoup
#Problem: The form is not clear for some entries. 8/5/2015
dichandle = urllib.urlopen(dicurl)
soup = BeautifulSoup(dichandle.read().decode('utf-8'),'html.parser')
meaning=u''
for tag in soup.find_all('span', class_='ssens'):
	for string in tag.stripped_strings:
		meaning = meaning+string
for submeaning in meaning.split(';'):
	print submeaning