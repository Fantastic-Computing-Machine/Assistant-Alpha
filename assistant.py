                                            # a.py with new weather command
from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
import re
import time
import sys
from selenium import webdriver
import smtplib
import random
import urllib
from playsound import playsound
import requests
import datetime
import wolframalpha
import pyttsx3
import connection
import wikipedia
from weather import Weather, Unit

engine = pyttsx3.init('sapi5')

app_id = "AA3V8Y-LLHLGGRLYP"
client = wolframalpha.Client(app_id)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

# FOR SPEAKING
def TalkToMe(audio):
    print(audio)
    #print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

# FOR GREETING
def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        TalkToMe('Good Morning!')

    if currentH >= 12 and currentH < 18:
        TalkToMe('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        TalkToMe('Good Evening!')

greetMe()
TalkToMe('Hi, Aditya.')
TalkToMe('How may I help you?')

#listens for commands
def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print('User:' + command + '/n')
        #TalkToMe(command)

    #loop back to continue to listen for command
    except sr.UnknownValueError:
        TalkToMe('Sorry! I didn\'t get that!')
        TalkToMe('Try Typing the command.')
        command = str(input('User: '))
    return command

#if statement for executing of commands
if __name__ == '__main__':
    while True:

        command = myCommand()
        command = command.lower()

        if 'open gmail' in command:
            TalkToMe('Opening Gmail')
            TalkToMe('Have a Productive Time..')
            webbrowser.open('www.gmail.com')

        elif 'open youtube' in command:
            TalkToMe('Opening Youtube')
            TalkToMe('Enjoy :)')
            webbrowser.open('www.youtube.com')

        elif 'open facebook' in command:
            TalkToMe('I am on it.')
            TalkToMe('Opening Facebook')
            username = 'aditya'
            password = 'ADITYA'
            url = 'https://www.facebook.com/'
            driver = webdriver.Chrome('C:\\Users\\Adiitya\\Desktop\\ASSISTANT\\chromedriver.exe')           # NEED TO CHANGE LOCATIONS
            driver.get(url)
            driver.find_element_by_id('email').send_keys(username)
            driver.find_element_by_id('pass').send_keys(password)
            driver.find_element_by_id('loginbutton').click()

        elif "what\'s up" in command or 'how are you' in command:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            TalkToMe(random.choice(stMsgs))
            
        elif 'play music' in command:
            music_folder = Your_music_folder_path
            music = [music1, music2, music3, music4, music5]
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)    
            TalkToMe('Okay, here is your music! Enjoy!')

        elif "what time is it" in command or "what is the time" in command:
            seconds = 1545925769.9618232
            local_time = time.ctime(seconds)
            #print("Local time:", local_time)
            TalkToMe('Local time:'+ local_time)

        elif "where is" in command:
            command = command.split(" ")
            location = command[2]
            chrome_path = 'C:\\Users\\Adiitya\\Desktop\\ASSISTANT\\chromedriver.exe'                    # NEED TO CHANGE LOCATIONS
            TalkToMe("Hold on Aditya, I will show you where "+ location +" is.")
            url= 'https://www.google.nl/maps/place/ + location + /&amp'
            webbrowser.get(chrome_path).open(url)
            #webbrowser.open('https://www.google.nl/maps/place/ + location + "/&amp;"')
    
        elif 'nothing' in command or 'abort' in command or 'stop' in command or 'bye' in command:
            TalkToMe('okay')
            #TalkToMe('Sayonara')
            stMsgs = ['Sayonara. Its Good Bye in Japanese.;)', 'Bye', 'Adiós. Thats GoodBye in Spanish. :)']
            TalkToMe(random.choice(stMsgs))
            exit()
    
        elif 'joke' in command:
            res = requests.get('https://icanhazdadjoke.com/',headers={"Accept":"application/json"})
            if res.status_code == res.codes.ok:
                TalkToMe(str(res.json()['joke']))
            else:
                TalkToMe('oops!I ran out of jokes')

        elif 'current weather in' in command:
            reg_ex = re.search('current weather in (.*)', command)             
            api_key = "68ccc7882541f7284444f3c4a1c29ee9"                            # Enter your API key here
            base_url = "http://api.openweathermap.org/data/2.5/weather?"            # base_url variable to store url 
            city_name = city = reg_ex.group(1)                                      # Give city name 
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name        # complete_url variable to store complete url address 
            response = requests.get(complete_url)                                   # get method of requests module return response object
            x = response.json()                                                     # json method of response object convert json format data into python format data 
            
            # Now x contains list of nested dictionaries, Check the value of "cod" key is equal to "404", means city is found otherwise, city is not found 
            if x["cod"] != "404":          
                y = x["main"]                                                       # store the value of "main" key in variable y
                current_temperature = y["temp"]-273.15                              # store the value corresponding to the "temp" key of y 
                current_pressure = y["pressure"]                                    # store the value corresponding to the "pressure" key of y 
                current_humidiy = y["humidity"]                                     # store the value corresponding to the "humidity" key of y 
                z = x["weather"]                                                    # store the value of "weather" key in variable z
                weather_description = z[0]["description"]                           # store the value corresponding to the "description" key at the 0th index of z 
                # print following values
                TalkToMe("\nCurrent Temperature in " + str(city_name) + " is " + str(current_temperature) + " degree Celcius." +
                    "\n The atmospheric pressure is " + str(current_pressure) + " hPa. " +
                    "\n The humidity is " + str(current_humidiy) + " %." 
                    "\n The Weather is " + str(weather_description))               
            else: 
                print(" City Not Found ")
                    
        else:
            command = command
            TalkToMe('Searching...')
            try:
                try:
                    res = client.command(command)
                    results = next(res.results).text
                    TalkToMe('Got it.')
                    TalkToMe('WOLFRAM-ALPHA says - ')
                    TalkToMe(results)                    
                except:
                    results = wikipedia.summary(TalkToMe, sentences=2)
                    TalkToMe('Got it.')
                    TalkToMe('WIKIPEDIA says - ')
                    TalkToMe(results)      
            except:
                webbrowser.open('www.google.com')
        
        TalkToMe('Next Command!')