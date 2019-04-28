from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
import re
import smtplib
import requests
from weather import Weather

def TalkToMe(audio):
    print(audio)
    tts = gTTS(text = audio, lang = 'en')
    tts.save('audio.mp3')
    os.system('mpg123 audio.mp3')

#listens for commands

def myCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('I AM READY FOR YOUR NEXT COMMAND')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print('YOU SAID:' + command + '/n')
    
    #loop back to continue to listen for command
    
    except sr.UnknownValueError:
        assistant(myCommand())
        
    return command

# is statement for executing of commands

def assistant(command):
    if 'open gmail' in command:
        chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
        url = 'https://mail.google.com/mail/u/0/#inbox'
        webbrowser.get(chrome_path).open(url)

    elif 'what\'s up' in command:
        TalkToMe('i am great, wassup with you.')

    elif "what time is it" in data:
        speak(ctime())

    elif "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on, I will show you where " + location + " is.")
        os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")

    elif 'send email' in command:
        TalkToMe('who do you want to send ?')
        recipiant = myCommand()
        if '<RECIEVER NAME>' in recipiant:
            TalkToMe('what should i say')
            content = myCommand()          
            #init gmail SMTP
            mail = smtplib.SMTP('smtp.gmail.com',587)            
            #identify to server
            mail.ehlo()            
            #encrypt session 
            mail.starttls()           
            #login using gmail
            mail.login('<SENDER'S EMAIL ID>', '<SENDER'S EMAIL PASSWORD')           
            #send mail
            mail.sendmail('<RECIEVER NAME>', '<RECIEVER EMAIL ID>'.content)           
            #close connection
            mail.colse()
            TalkToMe('EMAIL SENT')
    
    elif 'joke' in command:
        res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"}
                )
        if res.status_code == requests.codes.ok:
            talkToMe(str(res.json()['joke']))
        else:
            talkToMe('oops!I ran out of jokes')

    elif 'current weather in' in command:
        reg_ex = re.search('current weather in (.*)', command)
        if reg_ex:
            city = reg_ex.group(1)
            weather = Weather()
            location = weather.lookup_by_location(city)
            condition = location.condition()
            talkToMe('The Current weather in %s is %s The tempeture is %.1f degree' % (city, condition.text(), (int(condition.temp())-32)/1.8))

    elif 'weather forecast in' in command:
        reg_ex = re.search('weather forecast in (.*)', command)
        if reg_ex:
            city = reg_ex.group(1)
            weather = Weather()
            location = weather.lookup_by_location(city)
            forecasts = location.forecast()
            for i in range(0,3):
                talkToMe('On %s will it %s. The maximum temperture will be %.1f degree.'
                         'The lowest temperature will be %.1f degrees.' % (forecasts[i].date(), forecasts[i].text(), (int(forecasts[i].high())-32)/1.8, (int(forecasts[i].low())-32)/1.8))

TalkToMe('I am ready for your command.')

while True:
    assistant(myCommand())