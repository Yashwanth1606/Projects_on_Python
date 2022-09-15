from time import strftime
import pyttsx3   # this package is used to give the computer speak command
import datetime # this package is used to get time and date  
import speech_recognition as sr
import wikipedia
import webbrowser
import os 
import random

engine  = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id )
engine.setProperty('voice',voices[0].id)

# task1 : create speak function that speaks the command given to the personal assistent
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# task 2 : create wishme function that greet you based on the time 
def wishme():
    hour_now = int(datetime.datetime.now().hour)

    if hour_now >= 0 and hour_now < 12:
        speak("Good Morning Sir!")

    elif hour_now >= 12 and hour_now < 18:
        speak("Good Afternoon Sir!")

    elif hour_now >= 18 and hour_now < 20:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")

    speak("My name is robo ,Your personal assistant, Welcome to the my space, How can i help You")

# Task 3 : create a function that takes command from the user
def take_command():
    listen1 = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        listen1.pause_threshold = 1
        audio = listen1.listen(source)
    
    try:
        print("Recognizing.....")
        query1 = listen1.recognize_google(audio,language='en-in')
        print(f"user said: {query1}\n")
    except Exception as e:
        # print(e) uncomment this when you what to what is the exception  that is accuring during recognizing speech
        print("Did not able to recognizie can u please say that agian........ ")
        return "None"
    return query1

if __name__ == "__main__":
    wishme() # do not take this inside while or else your ziva assistance will always be wishing you

    while True:
        query = take_command().lower()
            # this below code is to used to get info from wikipedia
        if "wikipedia" in query:
            speak("searching wikipedia.....")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia")
            print(result)
            speak(result)

            # this below code is to open youtube 
        elif "open youtube" in query:
            speak("opening youtube....")
            webbrowser.open("youtube.com")

            # this below code is to open google 
        elif "open google" in query:
            speak("opening google....")
            webbrowser.open("google.com")
        
        # this below code is to open stackoverflow 
        elif "open stackoverflow" in query:
            speak("opening stackoverflow....")
            webbrowser.open("stackoverflow.com")

        # this below code is to paly music from your folder
        elif "play music" in query:
            music_dir = "D:\\music" # here paste the path of your music folder use \\
            songs = os.listdir(music_dir)
            print(songs)
            length_of_list = int(len(songs))
            ran = random.randint(0, (length_of_list - 1))
            os.startfile(os.path.join(music_dir,songs[ran]))

        # this below code is to check the time 
        elif "time" in query:
            current_time = datetime.datetime.now().strftime('%H:%M:%S')
            print(f"Sir the current time is{current_time}")
            speak(f"Sir the current time is{current_time}")

            # this below code is to open any app provided
        elif "open code" in query:
            code_path = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" # here paste the path of your any app location from properties
            os.startfile(code_path)

        # this below code is used to exit the while loop
        elif "exit" in query:
            speak("exiting the listening mode...... hope i was helpfull sir")
            exit()