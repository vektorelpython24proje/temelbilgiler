import pyttsx3 #pip install pyttsx3
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr #pip install SpeechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser #pip install webbrowser
import os,sys
import smtplib #pip install smtplib
import time

man=input("What is your name: ")
engine = pyttsx3.init("sapi5")

def speak(text):
    engine.setProperty("rate",130)
    engine.say(text)
    engine.runAndWait()

speak("Write your Chrome Path here")
chrome_inp=input(r"Write your ChromePath here:")
chrome_inp=chrome_inp.replace("\\","/")

speak("Write your Firefox Path here")
firefox_inp=input(r"Write your FirefoxPath here:")
firefox_inp=firefox_inp.replace("\\","/")

speak("Write your Spotify Path here")
spotify_inp=input(r"Write your Spotify Path here:")
spotify_inp=spotify_inp.replace("\\","/")

chrome_path =chrome_inp + ' %s'
firefox_path = firefox_inp+' %s'
spotify_path= spotify_inp

browserpref=input("Your browser preference(Chrome/Firefox): ")
browser_imp=None

if browserpref=="Chrome":
    browser_imp=chrome_path
elif browserpref=="Firefox":
    browser_imp=firefox_path

def search2(*args):
    x=input("Name:")
    y=x.replace(" ","+")
    print(y.lower)
    webbrowser.get(browser_imp).open("https://www.imdb.com/find?q="+y+"&ref_=nv_sr_sm")

def search(*args):
        x=input(":")
        y=x.replace(" ","%20")
        print(y.lower)
        webbrowser.get(browser_imp).open("https://myanimelist.net/search/all?q="+y+"&cat=all")

def googleSpeak(text):
    tts=gTTS(text,lang="tr")
    tts.save("ses.mp3")
    playsound("ses.mp3")
    os.remove("ses.mp3")

def hour():
    hour=int(datetime.datetime.now().hour)
    if hour>= 0 and hour < 12:
        speak("Good Morning" + man)
    elif hour>=12 and hour<18:
        speak("Good Evening" + man)
    else:
        googleSpeak("good night" + man)

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('echoretestmail@gmail.com','test123_xx')
    server.sendmail("echoretestmail@gmail.com",to,mail)
    server.close()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening sir")
        speak("I am listenin sir")
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio,language='en-US')
        print(f"user said: {query}\n")
        print("------------------------------")
    except Exception as e:
        print("say again pls")
        query=None
    return query

def YesNoCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Yes or no")
        speak("Yes or no")
        audio = r.listen(source)
    try:
        print("recognizing...")
        query2 = r.recognize_google(audio,language='en-US')
        print(f"user said: {query}\n")

    except Exception as e:
        print("say again please i can't understand correctly")
        speak("say again please i can't understand correctly")
        query2=None
    return query2  

speak("Wait a second please , I am Initializing Jarvis")
time.sleep(1)
speak("Jarvis On,How can I help You"+man)
hour()

while True:
    try:
        query=takeCommand()
        if 'wikipedia' in query.lower():
            speak("Searching Wikipedia")
            query=query.replace("wikipedia","")
            results= wikipedia.summary(query,sentences=2)
            print(results)
            speak(results)
            print("------------------------------")

        elif 'thank you' in query.lower():
            print("You welcome"+man)
            print("------------------------------")

        elif 'open youtube' in query.lower():
            webbrowser.get(browser_imp).open("youtube.com")

        elif 'open google' in query.lower():
            webbrowser.get(browser_imp).open("google.com")

        elif 'opem reddit' in query.lower():
            webbrowser.get(browser_imp).open("reddit.com")
            time.sleep(1)

        elif 'open anime' in query.lower():
            webbrowser.get(browser_imp).open("turkanime.net")
            time.sleep(1)

        elif 'open spotify' in query.lower():
            os.system(spotify_inp)
            time.sleep(1)

        elif 'open web spotify' in query.lower():
            webbrowser.get(browser_imp).open("open.spotify.com")
            time.sleep(1)

        elif 'the time' in query.lower():
            nTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(nTime)
            speak(man+"There is the time you want"+nTime)
            time.sleep(1)

        elif 'open code' in query.lower():
            os.startfile('C:/Program Files/Microsoft VS Code/Code.exe')
            time.sleep(1)

        elif 'open myanimelist' in query.lower():
            webbrowser.get(browser_imp).open("https://myanimelist.net/")
            time.sleep(1)

        elif 'search anime' in query.lower():
            speak("Write Please")
            search()
            time.sleep(1)

        elif 'search imdb' in query.lower():
            speak("Write Please")
            search2()
            time.sleep(1)

        elif 'exit' in query.lower():
            speak("Calm Down Boy Are you sure? tell me yes or no")
            query2=YesNoCommand()
            if query2=="yes":
                speak("See you again boy ... Farewell")
                sys.exit()
            elif query2=="no":
                speak("good boy lets continue")
            time.sleep(1)

        elif 'send email to echo' in query.lower():
            try:
                speak("Okay! What shoul I sent?")
                mail=takeCommand()
                to = "dev.echore08@gmail.com"
                sendEmail(to,mail)
                speak("Email sended")
            except Exception as e:
                print(e)
            time.sleep(1)
        
        elif 'send a email please' in query.lower():
            try:
                speak("Okay! What shoul I sent?")
                mail2=takeCommand()
                speak("Write the gmail who you want to send please")
                to = input("Write the gmail who you want to send please:")
                sendEmail(to,mail2)
                speak("Email sended")
            except Exception as e:
                print(e)
            time.sleep(1)
    
    except Exception as e:
        print("Enjoying the Silence? What a drag")
        speak("Enjoying the Silence? What a drag")


