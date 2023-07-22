import pyttsx3
import speech_recognition as sr 
import webbrowser
import pywhatkit
import os


Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
print(voices)
Assistant.setProperty('voices',voices[0].id)
Assistant.setProperty('rate' ,210)

def Speak(audio):
    print("    ")
    Assistant.say(audio)
    print(f"{audio}")
    print("    ")
    Assistant.runAndWait()


def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....'")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("Recognizing.....")
            query = command.recognize_google(audio,language='en-in')
            print(f"you said :{query}")

        except Exception as Error:
            return None
        

        return query.lower()


def TaskExe():

    def Music():
        Speak("Tell me the name of the song!")
        musicName = takecommand()

        if 'o\pasoori' in musicName:
            os.startfile('E:\\songs\\Pasoori Nu - Satyaprem Ki Katha 320 Kbps.mp3') 

        else:
            pywhatkit.playonyt(musicName)
        
        Speak("your song as been started, enjoy sir")

    while True:

        query = takecommand()

        if 'hello' in query:
            Speak("Hello sir, i am jarvis ")
            Speak("your Personal AI Assistant")
            Speak("How may i help you?")

        elif 'how are you' in query:
            Speak("I AM fine sir!")
            Speak("what about you sir")

        elif 'youtube search' in query:
            Speak("ok sir, This is what i found for your search!")
            query = query.replace("jarvis","")
            query = query.replace("youtube search","")
            web = 'https://www.youtube.com/results?search_query='+ query
            webbrowser.open(web)
            Speak("Done sir")
        
        elif 'google search' in query:
            Speak("ok sir, this what i found for your search")
            query = query.replace("jarvis","")
            query = query.replace("google search","")
            pywhatkit.search(query)
            Speak("Done sir")
        
        elif 'website' in query:
            Speak("ok sir this is what i  found")
            query = query.replace("jarvis","")
            query = query.replace("website","")
            web1 = query.replace("open ","")
            web2 = 'http://www.' + web1 + '.com'
            webbrowser.open(web2)
            Speak("launched")
        
        elif 'by' in query:
            Speak("Ok Sir, Bye!")
            break

        elif 'music' in query:
            Music()
            
TaskExe()
