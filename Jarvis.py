import speech_recognition as sr 
from time import ctime
import time
import random
import wikipedia 
import wolframalpha 
import webbrowser
import pyttsx3
import datetime
import sys

my_name = "Ishank" 
app_id = "9AVAQW-H939EUQVK4" 
ai_name = "Jarvis"

client = wolframalpha.Client(app_id)

def speak(audio):
 print(audio)
 engine = pyttsx3.init()
 engine.say(audio)
 engine.runAndWait()


def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
         speak("What can i do for you?") 
         r.adjust_for_ambient_noise(source,duration=1)   #calibrate the energy threshold for ambient noise levels             
         audio = r.listen(source)    #listen for the first phrase and extract it into audio data

    # Speech recognition using Google Speech Recognition
    data = ""

    try:
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)   #returns string
        print("You said: " + data)
    except sr.UnknownValueError:
        print("I am still listening")
    except sr.RequestError as e:
        print("Could not request results from web; {0}".format(e))

    return data

#this is to greet you everytime you open this ai based on current timings
def greetMe():
    current_tH=datetime.datetime.fromtimestamp(time.time())
    currentH = current_tH.hour
    if currentH >= 0 and currentH < 12:
        speak('Good Morning')

    if currentH >= 12 and currentH < 17:
        speak('Good Afternoon!')

    if currentH >= 17 and currentH < 20:
        speak('Good Evening!')

    if currentH >= 20 and currentH !=0:  
        speak("Good Night!")   

def jarvis(data):

    if "how are you" in data:
        speak("I am fine")

    elif "open Google" in data:
        speak("ya, i am trying")
        webbrowser.open('www.google.co.in')
        
    elif "open Youtube" in data:
        speak("ya, i am trying")
        webbrowser.open('https://www.youtube.com/')   
        
    elif "open Gmail" in data:
        speak("ya, i am trying")
        webbrowser.open('www.gmail.com/')  

    elif "what are you doing" in data:
        l=["Talking with you","just chilling","browsing the internet"]            
        speak(random.choice(l))
        
    elif "where is" in data:
        data = data.split(" ")
        if len(data)==3:
            location = data[2]
            speak("Hold on " + my_name + ", I will show you where " + location + " is.")
            webbrowser.open('https://www.google.com/maps/place/' + location)
        else:
            data=data[2:]
            location=""
            for words in data:
                location+=words
                location+=" "
            speak("Hold on " + my_name + ", I will show you where " + location + " is.")
            webbrowser.open('https://www.google.com/maps/place/' + location)
 
    elif "what time is it" in data:
        speak(ctime())

    elif "how are you" in data:
        Msgs = ['I am fine!', 'Nice!', 'I am good and full of energy']
        speak(random.choice(Msgs))
           
    elif "hello" in data:
        speak("Hello Ishank") 
        
    elif "nothing" in data or "stop" in data or "bye" in data:
        speak("okay")
        speak("Bye Sir, have a good day")
        sys.exit()

    else:
        data = data
        speak('Searching...')
        try:
            try:
                res = client.query(data)      #next is used for iteration
                results = next(res.results).text      #to make sure wolramalpha gives answer in text and not in graph and all
                speak('Got it.')                    #“pod”: Is a list containing the different results. This can also contain “subpods”
                speak(results)
                    
            except:
                results = wikipedia.summary(data, sentences=2)
                speak('Got it.')
                speak('WIKIPEDIA says - ')
                speak(results)
                
        
        except:
            speak("Something else Sir")
        
        
greetMe()
# initialization
time.sleep(1)
speak("Hey this is " + ai_name + " your personal Assistant how may i help you?")
while 1:
    data = recordAudio()   #string
    jarvis(data)