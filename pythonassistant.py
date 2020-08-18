# importing required libraries

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random

# Starting the pyttsx3 engine for speaking
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# printing the available voices in computer
# print(voices)
# Selecting the specific voice
engine.setProperty('voice',voices[2].id)



def speak(audio):
	# creating the speak function for speaking
	engine.say(audio)
	engine.runAndWait()
	
def takecommand():
		#it takes the sound input from the microphone and recognizes it.
		r = sr.Recognizer()
		with sr.Microphone() as source:
			print('listening....')
			r.pause_threshold = 1
			audio = r.listen(source)
		# it will convert to text of the given audio from microphone using google recognizer	
		try :
			print('Recognizing')
			query = r.recognize_google(audio,language = 'en-in')
			print(f'user said : {query}\n')
		# if it doesn't recognize then it will ask again to speak	
		except Exception as e:
			# print(e)
			print("can't recognize say it again please")
			return 'None'
		# Returns the recognized query	
		return query

def wishme():
	# this function initializes the dekstop assistant and wishes Users
	hour = datetime.datetime.now().hour
	if hour > 0 and hour <= 12 :
		speak('Good morning')
	elif hour>= 12 and hour <= 18 :
		speak('Good evening')
	else :
		speak('Good night')
	speak('Sir I am your dekstop assistant .How can i help you')
	
def sendemail(tob,contents):
	# this function is for setting up server for sending emails
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login('myEmail','myPassword')
	server.send(tob,contents)
	server.close()

	
if __name__ == "__main__":
	speak('hey how are you')
	wishme()
	while True:
		query = takecommand().lower()
		if 'wikipedia' in query:
			print('Searching....')
			query = query.replace('wikipedia',"")
			results = wikipedia.summary(query, sentences = 4)
			speak('According to wikipedia')
			print(results)
			speak(results)
		elif 'open youtube' in query:
			webbrowser.open('youtube.com')
			
		elif 'open google' in query:
			webbrowser.open('google.com')
			
		elif 'open facebook' in query:
			webbrowser.open('facebook.com')
			
		elif 'open stackoverflow' in query:
			webbrowser.open('stackoverflow.com')
			
		elif 'open music' in query:
			music_dir = 'E:\\Receiv. files'
			songs = os.listdir(music_dir)
			# l = len(songs)
			os.startfile(os.path.join(music_dir , random.choice(songs)))
			
		elif 'time' in query:
			str_time = datetime.datetime.now().strftime("%H%M%S")
			speak(f"The time is {str_time}")
		
		elif 'open code' in query:
			codepath = 'C:\\Users\\SKRUTI\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code'
			os.startfile(codepath)
		
		
		elif 'open notepad' in query:
			codepath = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs'
			os.startfile(codepath)
		
		elif 'email' in query:
			try:
				speak("what shall i say...")
				content = takecommand()
				to = 'reciever_email'
				sendemail(to,content)
				speak("email has been sent successfully")
			except exception as e:
				# print(e)
				speak("sorry,I'm not able to send email.")
	
