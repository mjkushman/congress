#!	congress.py
#	this program gets all the members of congress by name, 
#	state, district, party, years served, and years in congress

dbn = 'THIS IS PRINTED FOR DEBUGGING'
import requests, os,time, shelve
from bs4 import BeautifulSoup

urlBase = 'https://www.congress.gov/members?pageSize=250&page=' #starting url
urlPage = 1														#url page num
url = urlBase + str(urlPage)
namesFilename = 'congress-names.txt'
os.makedirs('pictures', exist_ok=True) 							#creates dir for pics at /pictures
pagesToCrawl = (int(input('How many pages to crawl? '))+1)												#Define how many pages to crawl


names = []														#creates an empty list of names
conShelf = shelve.open('conShelf', 'c')							#creates or opens a shelf file
if 'names' in conShelf:
	names = list(conShelf['names'])								#assigns names shelved in 'names' to names variable



while urlPage < pagesToCrawl:
	#Open or create a file to store the result


	#TODO: Download page
	url = urlBase + str(urlPage)								#complete url
	print('downloading %s...' % url)							#curret url to download
	res = requests.get(url, headers = {'User-agent': 'friend'})	#returns current url as a response obj
	res.raise_for_status()										#ends program if error downloading page

	print('parsing %s...' % url)								#prints parsing current url
	conSoup = BeautifulSoup(res.text, 'html.parser')			#puts response in bs4 format (parsable)
	namesSelect = conSoup.select('.result-heading')
	print('Appending list of names found on %s...' % url)
	
	print(names, dbn)
	print(type(names),dbn)
	#Add names to list of names
	for n in range(0,len(namesSelect),2):
		if namesSelect[n].string not in names:
			names.append(namesSelect[n].string)

	#TODO: Get names of all congress members
	#main > ol > li:nth-child(1) > span > a
	#main > ol > li:nth-child(3) > span > a



	#TODO: Get party of all congress members



	#TODO Get district of all congress members




	#TODO Get terms served for all congress members




	#TODO: Get number of years served
	print('sleeping for 5')
	time.sleep(5)
	urlPage += 1


conFile = open(namesFilename, 'w')									#opens a file for writing			
print('writing names to ' + str(os.getcwd()) + namesFilename)
for n in range(0,len(names)):
	print(names[n])
	conFile.write(names[n]+ '\n')									#writes the namaes to a txt file
conFile.close()														#closes file

#print(names)

#for n in range(0,len(names)):
#	conShelf['names'].append(names[n])

conShelf['names'] = []										#shelves the names variable as 'names'
upNames = list(conShelf['names'])
upNames.append(names)
conShelf['names'] = str(upNames)
#FUCKEDFUECEDFUCKED!!!!!

print('heres whats in conShelf[names]:')
print(conShelf['names'])
conShelf.close()


print('DONE.')
print('Combed %s pages.' % (urlPage-1))
print('Returned %d names' %len(names))