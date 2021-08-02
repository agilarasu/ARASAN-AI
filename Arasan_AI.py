import speech_recognition as sr
from lxml import html
import requests
import webbrowser
import os
from pynput.keyboard import Key, Controller
import mouse
#to play Sound
from gtts import gTTS
from playsound import playsound
#to clear screen
from subprocess import call
from time import sleep
#cuatom defs
from defs import *
import csv
#import over
#start defs
def clear():
	_ = call('clear')

#welcome msg

mlist = []
loopme = 1
r = sr.Recognizer()
keyboard = Controller()

#say hi
settings_line = 1
with open('csv/userdetails.csv', 'r') as f:
	mycsv = csv.reader(f)
	mycsv = list(mycsv)
	name_userdetials = mycsv[settings_line][0]
	print(name_userdetials)
	appusername=name_userdetials
welcome(appusername)
print("Hello ",appusername,"! \nWelcome To ARASAN AI")
#start recognition
loopme=1
while(loopme == 1):
	
    with sr.Microphone() as source:

        
        r.adjust_for_ambient_noise(source)
        print("Say Something....")
        audio = r.listen(source)
        print("Trying to recognize Your Voice...")
        t = r.recognize_google(audio).lower()
        print("You just said "+t)

    try:
        print("a")
        #open any thing
        if(t.find("open") != -1):
        	le = t.find("open")+len("open")+1
        	t = t[le:]
        	nrow=0
        	print(nrow)
        	if (t=="youtube" or t=="Youtube"):
        		nrow=1
        	elif (t=="twitter" or t=="Twitter"):
        		nrow=2
        	elif (t=="instagram" or t=="insta"):
        		nrow=3
        	print(nrow)
        	try:
        		with open('csv/webapps.csv', 'r') as f:
        			mycsv = csv.reader(f)
        			mycsv = list(mycsv)
        			text = mycsv[nrow][1]
        			print(text)
        			app_name=mycsv[nrow][0]
        			print("Opening ",text)
        			exec(open(text).read())
        	except:
        			print("Cannot open \n"+t+"Check if it is installed")
    except:
    	print("Cannot Open")