# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 18:29:40 2020

@author: micro
"""

# importing speech recognition package from google api 
import speech_recognition as sr 
import playsound # to play saved mp3 file 
from gtts import gTTS # google text to speech 
import os # to save/open files 
import wolframalpha # to calculate strings into formula 
from selenium import webdriver # to control browser operations 
import time


def process_text(input): 
	try: 
		if 'search' in input or 'play' in input: 
			# a basic web crawler using selenium 
			search_web(input) 
			return

		elif "who are you" in input or "define yourself" in input: 
			speak = '''Hello, I am Remind me . Your personal Assistant. 
			I am here to make your life easier. You can command me to perform 
			various tasks such as Reminding you daily essential duties or calculating sums or opening applications etcetra'''
			assistant_speaks(speak) 
			return

		elif "who made you" in input or "created you" in input: 
			speak = "I have been created by Augmented Human lab."
			assistant_speaks(speak) 
			return

		elif "augmented human Lab" in input:# just 
			speak = """Augmented Human Lab is the Best Research Lab."""
			assistant_speaks(speak) 
			return

		elif "calculate" in input.lower(): 
			
			# write your wolframalpha app_id here 
			app_id = "WOLFRAMALPHA_APP_ID"
			client = wolframalpha.Client(app_id) 

			indx = input.lower().split().index('calculate') 
			query = input.split()[indx + 1:] 
			res = client.query(' '.join(query)) 
			answer = next(res.results).text 
			assistant_speaks("The answer is " + answer) 
			return

		elif 'open' in input: 
			
			# another function to open 
			# different application availaible 
			open_application(input.lower()) 
			return
        
		elif 'remind me' in input: 
			
			# another function to open 
			# different application availaible 
			remindme(input.lower()) 
			return

		else: 

			assistant_speaks("I can search the web for you, Do you want to continue?") 
			ans = get_audio() 
			if 'yes' in str(ans) or 'yeah' in str(ans): 
				search_web(input) 
			else: 
				return
	except : 

		assistant_speaks("I don't understand, I can search the web for you, Do you want to continue?") 
		ans = get_audio() 
		if 'yes' in str(ans) or 'yeah' in str(ans): 
			search_web(input) 
            
def remindme(input):
    
    
    assistant_speaks("In how many minutes?")
    str = get_audio().lower() 
    tim = [int(s) for s in str.split() if s.isdigit()] 
    
    local_time = tim[0]
    local_time = local_time * 60
    time.sleep(local_time)
    print(input)
    assistant_speaks(input)
            
def search_web(input): 

	driver = webdriver.Firefox() 
	driver.implicitly_wait(1) 
	driver.maximize_window() 

	if 'youtube' in input.lower(): 

		assistant_speaks("Opening in youtube") 
		indx = input.lower().split().index('youtube') 
		query = input.split()[indx + 1:] 
		driver.get("http://www.youtube.com/results?search_query =" + '+'.join(query)) 
		return

	elif 'wikipedia' in input.lower(): 

		assistant_speaks("Opening Wikipedia") 
		indx = input.lower().split().index('wikipedia') 
		query = input.split()[indx + 1:] 
		driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query)) 
		return

	else: 

		if 'google' in input: 

			indx = input.lower().split().index('google') 
			query = input.split()[indx + 1:] 
			driver.get("https://www.google.com/search?q =" + '+'.join(query)) 

		elif 'search' in input: 

			indx = input.lower().split().index('google') 
			query = input.split()[indx + 1:] 
			driver.get("https://www.google.com/search?q =" + '+'.join(query)) 

		else: 

			driver.get("https://www.google.com/search?q =" + '+'.join(input.split())) 

		return


# function used to open application 
# present inside the system. 
def open_application(input): 

	if "chrome" in input: 
		assistant_speaks("Google Chrome") 
		os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe') 
		return

	elif "firefox" in input or "mozilla" in input: 
		assistant_speaks("Opening Mozilla Firefox") 
		os.startfile('C:\Program Files\Mozilla Firefox\\firefox.exe') 
		return

	elif "word" in input: 
		assistant_speaks("Opening Microsoft Word") 
		os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Word 2013.lnk') 
		return

	elif "excel" in input: 
		assistant_speaks("Opening Microsoft Excel") 
		os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Excel 2013.lnk') 
		return

	else: 

		assistant_speaks("Application not available") 
		return

num = 1
def assistant_speaks(output): 
	global num 

	# num to rename every audio file 
	# with different name to remove ambiguity 
	num += 1
	print("RemindMe: ", output) 

	toSpeak = gTTS(text = output, lang ='en', slow = False) 
	# saving the audio file given by google text to speech 
	file = str(num)+".mp3 "
	toSpeak.save(file) 
	
	# playsound package is used to play the same file. 
	playsound.playsound(file, True) 
	os.remove(file) 



def get_audio(): 

	rObject = sr.Recognizer() 
	audio = '' 

	with sr.Microphone() as source: 
		print("Speak...") 
		
		# recording the audio using speech recognition 
		audio = rObject.listen(source, phrase_time_limit = 5) 
	print("Stop.") # limit 5 secs 

	try: 

		text = rObject.recognize_google(audio, language ='en-US') 
		print("You : ", text) 
		return text 

	except: 

		assistant_speaks("Could not understand your audio, PLease try again !") 
		return 0


# Driver Code 
if __name__ == "__main__": 
	assistant_speaks("What's your name,Homo Sapien?") 
	name ='Homo Sapien'
	name = get_audio() 
	assistant_speaks("Hello, " + name + '.') 
	
	while(1): 

		assistant_speaks("What can i do for you?") 
		text = get_audio().lower() 

		if text == 0: 
			continue

		if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text): 
			assistant_speaks("Ok bye, "+ name+'.') 
			break

		# calling process text to process the query 
		process_text(text) 
        
        
