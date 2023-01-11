import speech_recognition as s
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import sched
import time
import os
import chess
import requests
import random
import wolframalpha
import pyautogui
import cv2
import winsound
import pyspeedtest
import pyautogui
import PyPDF2
import pyvolume
import pandas
import speech_recognition as s
from playsound import playsound
from bs4 import BeautifulSoup
from PIL import Image, ImageSequence
from pywikihow import *
from pycricbuzz import Cricbuzz
import smtplib
sr=s.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate', 170)
hour=int(datetime.datetime.now().hour)
if hour>=5 and hour<=12:
     engine.say('Good morning')
     engine.runAndWait()
if hour>12 and hour<=18:
     engine.say('Good afternoon')
     engine.runAndWait()
if hour>=18 and hour<=24:
     engine.say('Good evening')
     engine.runAndWait()
time=datetime.datetime.now().strftime('%H hour:%M minute')
if "0" in time:
     time=time.replace("0","O")
     engine.say("its "+ time)
     engine.runAndWait()
     print(time+" ")
else:
     engine.say("its "+ time)
     engine.runAndWait()
     print(time+" ")
engine.say('how can i help you sir')
engine.runAndWait()
sr=s.Recognizer()
def time():
     time=datetime.datetime.now().strftime('%H hour:%M minute')

def takeCommand():
     g='Online and ready' , 'Online always' ,'Ready to serve you', 'Here we go'

     with s.Microphone()as m:
          print("Initializing.............")
          app=wolframalpha.Client("JP2YWQ-77RG44KALT")
          sr.pause_threshold=1 
          audio=sr.listen(m,phrase_time_limit=7)
     try:
          print("Recognizing...........")
          query=sr.recognize_google(audio,language='eng-in')
          print(query)  
          playsound('C:\\Users\\hp\\OneDrive\\Desktop\\Jarvis\\chime.wav')
     except Exception as e:
          print (e)    
          print("Unable to Recognize your voice.")  
          return "None"
     
     
     e='how can you compair foolish alexa with me','i didnt expect these from you sir','am i not able to fulfill your desire'
     k='never bunk your school sir ','have done your homework','i know you are a puntual guy'
     return query



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
while True:
     permission = takeCommand()
     g='Online and ready' , 'Online always' ,'Ready to serve you', 'Here we go'
          
     

     if "wake up" in permission or "jarvis" in permission or "Jarvis" in permission:

          speak("Yes sir")
          while True:
               query = takeCommand()
               if 'Google' in query:
                    engine.say('opening google sir')
                    engine.runAndWait()
                    webbrowser.open("https://google.com")
               if 'check weather' in query:
                    engine.say('opening todays weather report sir')
                    engine.runAndWait()
                    webbrowser.open("https://www.accuweather.com")
               if 'Amazon' in query:
                    engine.say('sir in a mood of shopping immediately opening amazon')
                    engine.runAndWait()
                    webbrowser.open('https://www.amazon.in/')
               if 'Flipkart' in query:
                    engine.say('sir in a mood of shopping immediately opening flipkart')
                    engine.runAndWait()
                    webbrowser.open('https://flipkart.com')
               if 'Gmail' in query:
                    engine.say('opening gmail sir')
                    engine.runAndWait()
                    webbrowser.open('https://mail.google.com/mail/u/0/#inbox')
               if 'meet' in query or 'meeting' in query:
                    engine.say('want to get into meeting sir ok here it is')
                    engine.runAndWait()
                    webbrowser.open('https://meet.google.com')
               if 'Vivo web share' in query:
                    engine.say('opening vivo web share')
                    engine.runAndWait()
                    webbrowser.open('http://bs.vivo.com')
               if 'Instagram' in query:
                    engine.say('opening sir')
                    engine.runAndWait()
                    webbrowser.open('https://instagram.com')
               if 'Reddit' in query:
                    engine.say('opening sir')
                    engine.runAndWait()
                    webbrowser.open('https://www.reddit.com')
               if 'Quora' in query:
                    engine.say('opening sir')
                    engine.runAndWait()
                    webbrowser.open('https://www.quora.com')
               if 'play'in query:
                    video=query.replace('play', '')
                    engine.say('playing'+ video)
                    engine.runAndWait()
                    pywhatkit.playonyt(query)
               if 'time' in query:
                    time=datetime.datetime.now().strftime('%H hour:%M minute:%S second')
                    if "0" in time:
                         time=time.replace("0","O")
                         engine.say("sir current time"+ time)
                         engine.runAndWait()
                         print(time)
               if 'who is' in query:
                    person=query
                    info=wikipedia.summary(person,1)
                    engine.say(info)
                    engine.runAndWait()
                    print(info)
               if 'are you single' in query:
                    engine.say('i am in relation with Wifi')
                    engine.runAndWait()
                    print("\U0001F618")
               if "version" in query:
                    speak("I am JARVIS one point O")
               if 'jokes' in query:
                    engine.say(pyjokes.get_joke())
                    engine.runAndWait()
                    print(pyjokes.get_joke())
               if 'what is' in query:
                    saman=query.replace('what is ', '')
                    info=wikipedia.summary(saman,2)
                    engine.say(info)
                    engine.runAndWait()
                    print(info)
               if 'how are you' in query:
                    engine.say('i am completely fine and full of energy')
                    engine.runAndWait()
               if 'do you eat' in query:
                    engine.say('i eat WIFI and i excrete DATA')
                    engine.runAndWait()
               if 'birthday' in query:
                    speak("one two three start")
                    playsound("C:\\Users\\hp\\OneDrive\\Desktop\\Jarvis\\mark.mp3")
               if 'you are a foolish' in query:
                    engine.say('i am reflection of you is that enough to insult you ')
                    engine.runAndWait()
               if 'future' in query:
                    engine.say('sir in two thousand ninty six i will make a time machine and gift to you then go to Albert eiensten and ask him')
                    engine.runAndWait()
               if 'ghost' in query:
                    engine.say('there is only science in these world')
                    engine.runAndWait()
               if 'date' in query:
                    now=datetime.datetime.now()
                    l=now.strftime("%y-%m-%D")
                    engine.say(l)
                    engine.runAndWait()
                    print(l)
               if 'Alexa' in query or 'home' in query:
                    engine.say('sorry sir there is no sence of comparision i am better and smarter than them')
                    engine.say(random.choice(e))
                    engine.runAndWait()
               if 'Maps' in query:
                    engine.say('opening maps')
                    engine.runAndWait()
                    webbrowser.open('https://www.google.com/maps/@26.7157504,88.4015104,13z')
               if 'Anubhab' in query:
                    engine.say('sir Anubhab is my creator')
                    engine.runAndWait()
               if 'Focus' in query:
                    engine.say('sir i know its little hard but you can do it dont lose hope sir')
                    engine.runAndWait()
                    webbrowser.open('https://www.youtube.com/watch?v=RwxC5J8LI4Q')
               if 'Chrome web store' in query:
                    engine.say('opening chrome webstore sir')
                    engine.runAndWait()
                    webbrowser.open('https://chrome.google.com/webstore/category/extensions?utm_source=chrome-ntp-icon')
               if 'classroom' in query:
                    engine.say('go to your school sir')
                    engine.runAndWait()
                    webbrowser.open('https://classroom.google.com/u/1/h')
               if 'exam' in query:
                    engine.say('opening JEE MAINS MOCK TEST')
                    engine.runAndWait()
                    webbrowser.open('https://www.vedantu.com/test/PUBLIC/5dbd7cb0844b380beae8d15f')
               if 'talk with me' in query or 'speak' in query:
                    engine.say('sure sir i will never let you feel lonely')
                    engine.runAndWait()
                    engine.say('So boss how was your day')
                    engine.runAndWait()
                    with s.Microphone()as m:

                         print("i am listening you ...............................")
                         app=wolframalpha.Client("JP2YWQ-77RG44KALT")
                         sr.pause_threshold=1 
                         audio=sr.listen(m,timeout=4,phrase_time_limit=7)
                         query=sr.recognize_google(audio,language='eng-in')
                         print(query)
                         if 'good' in query or 'Good' in query:
                              engine.say('Awesome  , thats why i love you so much sir')
                              engine.runAndWait()
                         if 'aweful' in query or 'bad' in query or 'bed' in query:
                              o=pyjokes.get_joke()
                              engine.say('No matter sir i will make out your day better with few jokes.')
                              engine.say(o)
                              engine.runAndWait()
                    engine.say("Are you hungry")
                    engine.runAndWait()
                    engine.say("i think you need to get a protein diet with few carb")
                    engine.say("In general you need 52 grams of protein per day,")
                    engine.runAndWait()
                    import time
                    time.sleep(5)#....................
                    #...............................#..................
                    #.........................................
                    engine.say("Sir can i ask you one question")
                    engine.runAndWait()
                    import time
                    time.sleep(2)#...................
                    #..................
                    engine.say("What is your favorite food")
                    engine.runAndWait()
                    with s.Microphone()as m:
                         print("i am listening you ...............................")
                         app=wolframalpha.Client("JP2YWQ-77RG44KALT")
                         sr.pause_threshold=1 
                         audio=sr.listen(m,timeout=4,phrase_time_limit=7)
                         query=sr.recognize_google(audio,language='eng-in')
                         print(query)
                         engine.say(query)
                         engine.say("it is a quet interesting food lots of indian eats")
                         engine.runAndWait()
               if "collision" in query or "Collision" in query or "coalition" in query:
                    engine.say("collision is a event in which two bodies strike each other applying large force for a very small time")
                    engine.runAndWait()
                    import time
                    time.sleep(3)
                    engine.say("when collision happen there might be change 1 change in momentum or 2 there change in velocity")
                    engine.runAndWait()
                    import time
                    time.sleep(2)
                    engine.say("the ratio of relative velocity of separation to relative velocity of approach is called Coefficient of Restitution")
                    engine.runAndWait()    
               if 'where are we ' in query or 'where I am' in query:
                    engine.say('make sure that your Mobile data is connected not the WIFI ones')
                    engine.say('wait sir searching')
                    engine.runAndWait()
                    res=requests.get('https://ipinfo.io/')
                    data=res.json()
                    city=data['city']

                    location=data['loc'].split(',')
                    latitude=location[0]
                    longitude=location[1]  

                    print("latitude: " , latitude)
                    print("longitude: " , longitude)
                    print("city: " , city)
                    engine.say(city)
                    engine.runAndWait()  
               if 'are you ok' in query:
                    engine.say('i am always ok  what about you sir')
                    engine.runAndWait()
                    sr=s.Recognizer()
                    print("i am listening you ...............................")
                    with s.Microphone()as m:

                         audio=sr.listen(m)
                         query=sr.recognize_google(audio,language='eng-in')
                         print(query)

                    if 'I am fine 'in query or ' i am fine' in query:
                         engine.say('thats i have never seen such coolest boss over the world')
                         engine.runAndWait()

                              
               if 'shut down' in query:

                    engine.say('shutting the system go and get some rest sir')
                    engine.runAndWait()
                    os.system('shutdown /s /t 2')




               if 'restart my system' in query:
                    engine.say('restarting the system now i am lonely')
                    engine.runAndWait()
                    os.system('restart /r /t 5') 
               if 'temperature' in query: 
                    app=wolframalpha.Client("JP2YWQ-77RG44KALT")
                    r=app.query(query)
                    h=(next(r.results).text)
                    engine.say("sir the current temperature is " +h)
                    engine.runAndWait()
                    if "h" > "20":
                         speak("sir it is a sunny day")
                    if "h" < "20":
                         speak("its a cold day")         
                    print(h)
               if 'calculate' in query or 'calculator' in query:
                    engine.say('what should i calculate sir')
                    engine.runAndWait()
                    sr=s.Recognizer()
                    print("i am listening you ...............................")
                    with s.Microphone()as m:

                         audio=sr.listen(m)
                         query=sr.recognize_google(audio,language='eng-in')
                         print(query)
                         app=wolframalpha.Client("JP2YWQ-77RG44KALT")
                         q=query 
                         res=app.query(q)
                         b=(next(res.results).text)
                         engine.say(b)
                         engine.runAndWait()
                         print(b)
               if 'open LinkedIn' in query:
                    engine.say('sure opening sir')
                    engine.runAndWait()
                    webbrowser.open('https://www.linkedin.com/in/anubhab-chowdhury-517549204/')
               if 'window' in query:
                    pyautogui.keyDown("alt")
                    pyautogui.press("tab")
                    time.sleep(1)
                    pyautogui.keyup("alt")
               if 'news' in query or 'read news' in query:
                    main_url='https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=61c35f9010d544859e1c1f63e51cbe67'
                    main_page=requests.get(main_url).json()
                    article=main_page["articles"]
                    head=[]
                    day=["first","second","third","fourth","fifth","sixth","seventh","eight","ninth","tenth"]
                    for ar in article:
                         head.append(ar["title"])
                    for i in range(len(day)):
                         engine.say(f"today's {day[i]} news is :{head[i]}")
                         engine.runAndWait()
                         print(f"today's {day[i]} news is :{head[i]}")
               if 'camera'in query or 'Tamara' in query or 'Gamera' in query:
                    engine.say('opening sir')
                    engine.runAndWait()
                    cam=cv2.VideoCapture(0)
                    while cam.isOpened():
                         ret, frame1=cam.read()
                         ret, frame2=cam.read()
                         diff=cv2.absdiff(frame1,frame2)
                         gray=cv2.cvtColor(diff,cv2.COLOR_RGB2GRAY)
                         blur=cv2.GaussianBlur(gray,(5,5), 0)
                         _, thresh=cv2.threshold(blur,20,255, cv2.THRESH_BINARY)
                         dilated=cv2.dilate(thresh,None,iterations=3)
                         Contours,_=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
                         #cv2.drawContours(frame1,Contours,-1,(0,255,0) , 2)
                         for c in Contours:
                              if cv2.contourArea(c) < 5000:
                                   continue
                              x,y,w,h=cv2.boundingRect(c)
                              cv2.rectangle(frame1 , (x,y) , (x+w,y+h) ,(0,255,0) , 2)
                              winsound.PlaySound('C:\\Users\\hp\\OneDrive\\Desktop\\Jarvis\\alert.wav', winsound.SND_LOOP)
                         if cv2.waitKey(10)==ord('q'):
                              break
                         cv2.imshow('smile', frame1)
               if 'greet' in query or 'beat' in query or 'Greek' in query or 'greed' in query or 'Greet' in query or 'Greet' in query or ' my friend ' in query or 'friend' in query or 'greet my friend' in query:
                    engine.say('Welcome friend')
                    engine.say('Its too cold so feel free to grab a cup of cofee')
                    engine.say('be comfortable and take a seat')
                    engine.runAndWait()
                    engine.say(' So what is your name ')
                    engine.runAndWait()
                    print('i am listening to you sir........................')
                    with s.Microphone()as m:
                         audio=sr.listen(m,timeout=4,phrase_time_limit=7)
                         sr.pause_threshold=1 
                         query=sr.recognize_google(audio,language='eng-in')
                         a=query
                         print(query)
                         engine.say(a)
                         engine.say(' i think you are a quiet interesting person')
                         engine.say('have a nice day')
                         engine.runAndWait()
               if 'introduce' in query:
                    engine.say('I am JARVIS, just a rather intellegent system created by Sir Anubhab Chowdhury')
                    engine.say('I can perform various kinds of task')
                    engine.say('I am even your besty')
                    engine.runAndWait()
               if "open command prompt" in query or "command prompt" in query:
                    speak ("opening command prompt")
                    os.system("start cmd")              
               if "reflection" in query:
                    cap=cv2.VideoCapture(0)
                    while True:
                         ret,img=cap.read()
                         cv2.imshow('webcam',img)
                         k=cv2.waitKey(10)
                         if k==ord('t'):
                              break
                    cap.release()
                    cv2.destroyAllWindows()
               if "Notepad" in query:
                    speak("opening notepad")
                    os.system("start notepad")
               if "Excel" in query:
                    speak("opening Excel file")
                    os.system("start Excel")
               if "hello" in query:
                    speak("Hi sir good to know u care me a lot")
               if "good morning" in query:
                    speak("morning sir")
               if "good night" in query:
                    speak("good night sir")
               if "good afternoon" in query:
                    speak("good afternoon sir")
               if "good evening" in query:
                    speak("and a good evening to you as well")
               if "Happy Holi" in query:
                    speak("happy holi, its a feastival of colors")
               if "Happy Diwali" in query:
                    speak("A feastival of lights happy diwali sir")
               if "open YouTube" in query:
                    speak("opening youtube")
                    webbrowser.open("https://www.youtube.com/")
               if "Spotify" in query:
                    os.system("start Spotify")
               if "Windows security" in query:
                    os.system("start Window Security")
               if "covid-19" in query:
                    speak("no analysis now sir")
                    import bar_chart_race as bcr
                    df=bcr.load_dataset('covid19_tutorial')
                    df.head()
               if "search" in query:
                    speak("what would i search")
                    search=takeCommand()
                    url='https://google.com/search?q=' +search
                    webbrowser.get().open(url)
                    speak("here is what i found" +search)
               if "word" in query:
                    speak("Opening Microsoft Word")
                    os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD")
               if "PowerPoint" in query:
                    speak("opening MS powerpoint")
                    os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT")
               if "WhatsApp" in query:
                    speak("opening whatsapp")
                    os.startfile("C:\\Users\\hp\\AppData\\Local\\WhatsApp\\WhatsApp")
               if "Brave" in query:
                    speak("opening sir")
                    os.startfile("C:\\Users\\hp\\AppData\\Local\\BraveSoftware\\Brave-Browser\\Application\\brave")
               if "Telegram" in query or "telegram" in query:
                    speak("initiating sir")
                    os.startfile("C:\\Users\\hp\\AppData\\Roaming\\Telegram Desktop\\Telegram")  
               if "Discord" in query or "discord" in query:
                    speak("opening sir")
                    os.startfile("C:\\Users\\hp\\AppData\\Local\\Discord\\app-0.0.309\\Discord")
               if "control panel" in query:
                    os.system("start Control Panel")
               if "recycle bin" in query:
                    os.system("start Recycle Bin")
               



                    



               if 'ping' in query or 'beings' in query or 'pink' in query or 'latency' in query:
                    speed=pyspeedtest.SpeedTest("www.google.com")
                    a=speed.ping()
                    print("your ping is " , a)
                    engine.say('your ping is')
                    engine.say(a)
                    engine.runAndWait()
               if 'auto' in query:
                    pyautogui.FAILSAFE=False
                    engine.say('tuning auto mode')
                    engine.runAndWait()
                    while True:
                         time.sleep(20)
                         for i in range (0,100):
                              pyautogui.moveTo(0 , i * 5)
                         for i in range(0,3):
                              pyautogui.press('shift')
                              engine.say(' auto mode off')
                              engine.runAndWait()
                              if 'break' in query or'brick' in query:
                                   break
               if 'read book' in query or 'elitebook' in query or 'book' in query or 'books' in query or 'read' in query or 'lead' in query or 'study' in query:
                    book=open('C:\\Users\\hp\\OneDrive\\Desktop\\Jarvis\\kehb101.pdf' , 'rb')
                    pdfreader=PyPDF2.PdfFileReader(book)
                    pages=pdfreader.numPages
                    print(pages)
                    page=pdfreader.getPage(0)
                    text=page.extractText()
                    for num in range(0,1):
                         print(text)
                         engine.say(text)
                         engine.runAndWait()

               if 'spam' in query:

                    while True:
                         pyautogui.typewrite('Please reply me sir please')
                         pyautogui.typewrite("sir you made my childhood so specialPlease reply me sir pleasesir you made my childhood so special")
                         import time
                         time.sleep(2)
                         pyautogui.press('enter')
               if 'election' in query or 'electrician' in query:
                    wiki=pandas.read_html('https://en.wikipedia.org/wiki/2021_elections_in_India')
                    election=wiki[6]
                    print(election)
               if 'type' in query or ' Type' in query or 'write' in query:
                    engine.say('what should i type siir....')
                    engine.runAndWait()
                    with s.Microphone()as m:
                         print("i am listening you ...............................")
                         app=wolframalpha.Client("JP2YWQ-77RG44KALT")
                         sr.pause_threshold=1 
                         audio=sr.listen(m,timeout=4,phrase_time_limit=7)
                         query=sr.recognize_google(audio,language='eng-in')
                         pyautogui.typewrite(query)
                         pyautogui.press('enter')
                         time.sleep(1)
               if 'generate password' in query or 'generator' in query or 'password' in query:
                    import string
                    import random
                    engine.say('generating a cool password i  am sure no security Breach can break it')
                    engine.runAndWait()

                    if __name__ == "__main__":
                         s1 = string.ascii_lowercase
                         # print(s1)
                         s2 = string.ascii_uppercase
                         # print(s2)
                         s3 = string.digits
                         # print(s3)
                         s4 = string.punctuation
                         # print(s4)
                         plen = int(input("Enter password length\n")) #Todo1: Handle Gibberish
                         s = []
                         s.extend(list(s1))
                         s.extend(list(s2))
                         s.extend(list(s3))
                         s.extend(list(s4))
                         # print(s)
                         # random.shuffle(s)
                         # print(s)
                         print("Your password is: ")
                         print("".join(random.sample(s, plen)))
                         # print("".join(s[0:plen]))
               if 'scroll' in query or 'move' in query or 'moo' in query:
                    a='sir negative speed means scroll down and positive speed means scroll up'
                    engine.say(a)
                    engine.runAndWait()
                    print(a)

                    speed=input('how fast should i type sir')
                    sleepTime=input('how long should scroll')
                    pyautogui.time.sleep(5)
                    engine.say('Ready')
                    engine.runAndWait()
                    while 0 < 10 :
                         pyautogui.scroll(int(speed))
                         pyautogui.time.sleep(int(sleepTime))
               if "qr code" in query or "QR code" in query or "code" in query:

                    import pyqrcode
                    from pyqrcode import QRCode
                    link="https://www.youtube.com/"
                    url=pyqrcode.create(link)
                    url.svg("ak.svg",scale=8)



               if 'dialog' in query:
                    engine.say('to whome you want to listen sir')
                    engine.runAndWait()
                    print('sharuk khan=srk, proshunjeet=File,5')
                    print("i am listening you ...............................")
                    with s.Microphone()as m:
                         audio=sr.listen(m,timeout=4,phrase_time_limit=7)
                         sr.pause_threshold=1 
                         query=sr.recognize_google(audio,language='eng-in')
                         a=query
                         print(query)
                         if 'srk' in query or 'SRT' in query:
                              playsound('C:\\Users\\hp\\OneDrive\\Desktop\\Jarvis\\sample.mp3')
                         if 'Amitabh Bachchan' in query or 'ab' in query or 'AB' in query or 'EB ' in query:
                              playsound('C:\\Users\\hp\OneDrive\\Desktop\\Jarvis\\AB.mp3')
                         if 'Mithun chakraborty' in query or 'Mithun' in query or 'me too' in query or 'Mattoon' in query:
                              playsound('C:\\Users\\hp\\OneDrive\\Desktop\\Jarvis\\kt.mp3')
                         if 'Tony stark'in query or 'Tony Stark' in query:
                              playsound('C:\\Users\\hp\\OneDrive\\Desktop\\Jarvis\\TS.mp3')
                         if 'Modi' in query:
                              playsound('C:\\Users\\hp\\OneDrive\\Desktop\\Jarvis\\M.mp3')
                         if 'romantic' in query:
                              playsound('C:\\Users\\hp\\OneDrive\\Desktop\\Jarvis\\BS.mp3')
                         if 'File' in query or '5' in query:
                              playsound('C:\\Users\\hp\\OneDrive\\Desktop\\Jarvis\\PT.mp3')
                         if 'captain america' in query or 'Captain America' in query:
                              playsound('C:\\Users\\hp\\OneDrive\\Desktop\\Jarvis\\CAP.mp3')
                    import time          
                    time.sleep(4)
                    engine.say('Enjoyed sir')
                    engine.runAndWait()
               if 'solve' in query or 'Maths' in query or 'maths' in query or 'sum' in query or 'Saul' in query or 'question' in query:
                    query=input('Enter your question\n')
                    app=wolframalpha.Client("JP2YWQ-77RG44KALT")
                    q=query
                    res=app.query(q)
                    b=(next(res.results).text)
                    print(b)
               if 'laugh' in query or 'smile' in query:
                    playsound('C:\\Users\\hp\\OneDrive\\Desktop\\Jarvis\\zam.mp3')
                    time.sleep(2)
                    engine.say('That was a interesting jokes, i cant control my laughter')
                    engine.runAndWait()
               if 'face' in query or 'show me yourself' in query or 'show me yours' in query or 'show me yard sale' in query:
                    filename="C:\\Users\\hp\\OneDrive\\Desktop\\Jarvis\\jarvis.gui.gif"
                    img= Image.open(filename)
                    img.show()
               if 'year' in query or 'month' in query or 'days ' in query or 'week' in query:
                    days=int(input("Enter the NO. of days"))
                    year=days//365
                    days=days%365
                    month=days//12
                    days=days%30
                    weeks=days//7
                    days=days%7
                    print(year,"Years")
                    print(month,"Month")
                    print(weeks,"Weeks")
                    print(days,"Days")
               if "Alarm" in  query or "Allah" in query or 'alarm' in query:
                    import playsound
                    from datetime import datetime
                    engine.say('SIR enter the alarm time')
                    engine.runAndWait()
                    alarmtime=input("Enter Alarm time\n")
                    engine.say("Alarm time is set for")
                    engine.say(alarmtime)
                    engine.runAndWait()
                    while True:
                         lcltime=datetime.now().strftime("%H:%M")
                         if lcltime==alarmtime:
                              winsound.PlaySound('C:\\Users\\hp\\OneDrive\\Desktop\\Jarvis\\alert.wav', winsound.SND_LOOP)
                              import time
                              time.sleep(8)
                              speak("wake up sir")
                              speak("wake up sir")
                              speak("You have lot of work to do")
                              break
               if "Activate how to do mode" in query or "activate how to do mode" in query:
                    engine.say("How to do mode is activated")
                    engine.runAndWait()
                    print("i am listening you ...............................")
                    with s.Microphone()as m:
                         audio=sr.listen(m,timeout=4,phrase_time_limit=7)
                         sr.pause_threshold=1 
                         query=sr.recognize_google(audio,language='eng-in')
                         a=query
                         print(query)
                         how =a
                         max_results=1
                         how_to = search_wikihow(query, max_results)
                         assert len(how_to) == 1
                         how_to[0].print()
                         engine.say(how_to[0].summary)
                         engine.runAndWait()
               if "how much power left" in query or "battery" in query or "how much power we have" in query or "how much power lift" in query or "how much power" in query:
                    import psutil
                    battery=psutil.sensors_battery()
                    percentage=battery.percent
                    engine.say(f"sir our system has {percentage} percent battery")
                    engine.runAndWait()
                    print(percentage )

                    if percentage==100:
                         engine.say("Our system is fully charged")
                         engine.runAndWait()
                    if percentage>=75:
                         engine.say("we have enough power continue to work")
                         engine.runAndWait()
                    if percentage>=40 and percentage<=75:
                         engine.say(" we have less power connect to charging")
                         engine.runAndWait()
                    if percentage<=15:
                         engine.say(" please connect to charging or your system will be shut down soon")
                         engine.runAndWait()
               if "rain" in query or "Rain" in query:
                    playsound("C:\\Users\\hp\\OneDrive\\Desktop\\Jarvis\\rain.mp3")
                    playsound("C:\\Users\\hp\\OneDrive\\Desktop\\Jarvis\\wind.mp3")
                    playsound("C:\\Users\\hp\\OneDrive\\Desktop\\Jarvis\\thunder.mp3")
                    playsound("C:\\Users\\hp\\OneDrive\\Desktop\\Jarvis\\koyal.mp3")
               if "bird" in query:
                    for i in range(5):
                         playsound("C:\\Users\\hp\\OneDrive\\Desktop\\Jarvis\\koyal.mp3")
               if "internet speed" in query:
                    import speedtest
                    st = speedtest.Speedtest()
                    dl = st.download()
                    up = st.upload()
                    engine.say(f"sir we have {dl} bit per second downloadling speed and {up} bit per second uploading speed ")
                    engine.runAndWait()
               if "show note" in query:
                    speak("Showing Notes")
                    file = open("jarvis.txt", "r") 
                    print(file.read())
                    speak(file.read(6))    
               if "don't listen" in query or "stop listening" in query:
                    engine.say("for how much time you want to stop jarvis from listening commands")
                    engine.runAndWait()
                    a = int(takeCommand())
                    import time
                    time.sleep(a)
                    print(a)
               if "mind" in query or "think yourself" in query or "use your mind " in query:
                    speak("what do you want sir")
                    ask=takeCommand()
                    if ask=="Food" or ask=="food":
                         speak("sir are you hungry")
                         say=takeCommand()
                         if say=="no":
                              quit
                         if say=="yes":
                              a=time()
                              if a==9:
                                   speak("sir have your breakfast")
                              if a==14:
                                   speak("Grab your lunch sir")
                              if a==20:
                                   speak("Supper time sir")
                              else:
                                   j="sir you can have a light meal or snackes"
                                   speak(j)
               if "tranlate" in query or "Translate" in query:
                    import googletrans
                    print(googletrans.LANGUAGES)
                    translator=googletrans.Translator()
                    speak("what should i translate")
                    a=takeCommand()
                    speak("Input the language you want to translate")
                    j=input("enter the language")

                    T=translator.translate(a,dest=j)
                    print(T)
                    import gtts
                    audio=gtts.gTTS(T.text,lang=j)
                    audio.save('doremon.mp3')
                    playsound('doremon.mp3')
               if "volume up" in query:
                    pyautogui.press("volumeup")
               if "volume down" in query:
                    pyautogui.press("volumedown")
               if "mute" in query:
                    pyautogui.press("volumemute")
               if "ip address" in query or "IP address" in query:
                    from requests import get
                    ip=get('https://api.ipify.org').text
                    speak("your ip address is")
                    speak(ip)
                    print(ip)
               if "Caps on" in query or "caps on" in query or "capital" in query or "Capital" in query:
                    pyautogui.press("capslock")
               if "Caps off" in query or "caps off" in query:
                    pyautogui.press("capslock")
               if "copy" in query or "Copy" in query or "copy the whole page" in query:
                    import pyautogui as pya
                    pya.hotkey('ctrl','A')
                    pya.hotkey('ctrl', 'c')
               if "Brightness up" in query or "brightness up" in query:
                    pyautogui.press("f3")
               if "Brightness down" in query or "brightness down" in query:
                    pyautogui.press("f2")
               if "Airplane mode" in query:
                    pyautogui.press("Airplane mode")
               if "facts" in query or "tell me some fact" in query or "tell me some pack" in query:
                    from requests import get
                    fact=get("https://www.savit.in/unknown-facts.asp")
                    print(fact)
                    speak(fact)






                    
                    
                              
                    
   





      
               if "sleep" in query:
                    speak("you can call me anytime")
                    break
               import time
               time.sleep(1)
               

               
               


# This is my Change.










     elif "goodbye" in permission:
          speak("Thank you")
          exit()
