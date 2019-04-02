#!/usr/bin/env python
import sys
import random
from twython import Twython
from wordnik import *
import configparser
import logging


def getANewWord(fileToUse):
	lineToUse = random.choice(open(fileToUse).readlines())
	lineToUse = lineToUse.split(' ')
	wordToUse = lineToUse[0]
	return wordToUse


def findDefinition(wordToFind):
	# wordnik authentication
	wordnikApiUrl = 'http://api.wordnik.com/v4'
	wordnikApiKey = config['wordnik']['apiKey']

	client = swagger.ApiClient(wordnikApiKey, wordnikApiUrl)

	wordConnection = WordApi.WordApi(client)
	example = wordConnection.getExamples(word=wordToFind,limit=3)
	example = example.examples
	defn = wordConnection.getDefinitions(word=wordToFind,sourceDictionaries='wiktionary')
	#print example.text
	#print defn[0].text
	return (defn,example)
	

def tweetDefn(word,defn):
	arr = ["You must be knowing","Just realized","Did u know","Dictionary says","Pata hai"," "]
	prefix = random.choice(arr)
	tweet = prefix+" #"+word+" means "+abbreviatePoS(defn[0].partOfSpeech)+'  '+defn[0].text
	if len(tweet) > 140:
		tweet1 = tweet[:120]+'(1/2)'
		api.update_status(status=tweet1)
		tweet2 = tweet[120:]+'(2/2) #'+word
		api.update_status(status=tweet2)
	else:
		api.update_status(status=tweet)
	logging.info("Tweeted another word!") 


def abbreviatePoS(partOfSpeech):
	if partOfSpeech == 'noun':
		return '(n.)'
	elif partOfSpeech == 'adjective':
		return '(adj.)'
	elif partOfSpeech == 'verb':
		return '(v.)'


def DMdef(word,defn,example):
	#arr = ["You must be knowing","Just realized","Did you know","Dictionary says","Pata hai"," "]
	#prefix = random.choice(arr)
	message = '#'+word.upper()+": \n--------------------------------\n"
	for definition in defn:
		message = message+abbreviatePoS(definition.partOfSpeech)+'  '+definition.text+"\n\n"
	#tweet = prefix+" "+word+" means "+defn+" \n\n"+"EXAMPLE :- "+example+"\n"
	message=message+"\nEXAMPLES: \n--------------------------\n"
	for eg in example:
		if len(eg.text)<=200:
			message = message+eg.text+"\n\n"
	#message=message+"----------------------"
	api.send_direct_message(screen_name=config['twitter']['receiverTwitterUsername'],text=message)
	logging.info("DMs Sent.")


def tweetANewWord():
	config = configparser.ConfigParser()
	config.read('config_auth.properties')

	# Twython authentication
	# your twitter consumer and access information goes here
	apiKey = config['twitter']['apiKey']
	apiSecret = config['twitter']['apiSecret']
	accessToken =  config['twitter']['accessToken']
	accessTokenSecret = config['twitter']['accessTokenSecret']

	api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)
	print "api for twython done bro"

	# LOGIC!!!!
	filesAvailable = ['words.txt','wordsPrinceton.txt']
	fileToUse = random.choice(filesAvailable)
	print "will be using "+fileToUse+" file."

	wordToUse = getANewWord(fileToUse)
	wordToUse = wordToUse.strip()

	print "wordToUse is "+wordToUse
	definition,example = findDefinition(wordToUse)

	#DMdef(wordToUse,definition,example)
	tweetDefn(wordToUse,definition)
	print "Done."
