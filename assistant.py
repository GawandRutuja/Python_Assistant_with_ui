#import Librabries
import pyttsx3 as p
import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from yt import *
from news import *
import randfacts
from jokes import *
import datetime


# Initialize text-to-speech engine
engine = p.init()
rate=engine.getProperty('rate')
engine.setProperty('rate',130)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to wish based on the time of day
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        return("morning")
    elif hour>=12 and hour<16:
        return("afternoon")
    else:
        return("night")


# Get current date and time
today_date=datetime.datetime.now()
r=sr.Recognizer()


# Greet the user and provide current date and time
speak("Hello ladied and gentleman, good" + wishme() + "i am your voice assistant ruvi.")
speak("Today is" + today_date.strftime("%d") + "of" + today_date.strftime("%B") + today_date.strftime("%Y") + "And its currently" + (today_date.strftime("%I")) + (today_date.strftime("%M")) + (today_date.strftime("%p")))
speak("How are you??")

# Use speech recognition to capture user's response
with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("Listening...")
    audio=r.listen(source)
    text=r.recognize_google(audio)
    print(text)
# Check if the user mentioned "what about you" and respond accordingly
if "what" and "about" and "you" in text:
    speak("i am also having a good day")
speak("what can i do for you?")


# Capture the user's next command
with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("Listening...")
    audio=r.listen(source)
    text2=r.recognize_google(audio)
    print(text2)

# Check the user's command and execute corresponding actions
if 'information' in text2:
    speak("you need information related to which topic??")

     # Capture the user's input for the topic they want information on
    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("Listening...")
        audio=r.listen(source)
        infor=r.recognize_google(audio)
        print(infor)

         # Class to handle information retrieval from Wikipedia
        class infow():
            def __init__(self):
                # Provide the path to the ChromeDriver executable, not the Chrome browser executable 
                s=Service("C:\\chromedriver.exe")
                self.driver = webdriver.Chrome(service=s)
            
            def get_info(self, query):
                self.query = query
                self.driver.get(url="https://www.wikipedia.org/")
                # Find the search input field and send keys
                search_input = self.driver.find_element("xpath", '//*[@id="searchInput"]')
                search_input.send_keys(query)
                enter_input = self.driver.find_element("xpath", '//*[@id="search-form"]/fieldset/button')
                enter_input.send_keys(query)
                #search=self.driver.find_element_by_xpath('//*[@id="search-input"]')
                #search.click()
                #search.send_keys(query)
                #enter.click()

    speak("searching {} in wikipedia".format(infor))
    print("searching {} in wikipedia".format(infor))

    assist = infow()
    assist.get_info(infor)

elif 'play' and 'video' in text2:
    speak("you want me to play which video??")

    # Capture the user's input for the video they want to play
    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("Listening...")
        audio=r.listen(source)
        vid=r.recognize_google(audio)
        print(vid)

    speak("playing {} on youtube".format(vid))
    print("playing {} on youtube".format(vid))

     # fetching the data from yt.py file with the class "music".
    assist = music()
    assist.play(vid)


elif 'news' in text2:
    speak("Sure. Now i will read news for you.")
    # fetching the data from news.py file with the class "news".
    arr=news()
    for i in range(len(arr)):
        print(arr[i])
        speak(arr[i])


elif "facts" or "fact" in text2:
    speak("Sure.")
    x=randfacts.get_fact()
    print(x)
    speak("Did you know that,"+x)


elif "joke" in text2:
    speak("Sure. get ready for some chukles.")
    # fetching the data from jokes.py file with the class "joke".
    arr=joke()
    print(arr[0])
    speak(arr[0])
    print(arr[1])
    speak(arr[1])
    
    
        
