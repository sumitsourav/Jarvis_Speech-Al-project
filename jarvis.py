import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import sys
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    speak("I am Jarvis. Please tell me how may i help you.")


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening . . .")
        r.pause_threshold = 1
        r.energy_threshold = 100
        audio = r.listen(source)

    try:
        print("Recognizing . . ")
        query = r.recognize_google(audio, language='en-in')
        print("User said: ", query)

    except Exception as e:
        # print(e)
        print("Say that again please")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('su5mitsourav@gmail.com', '#b130053410#')
    server.sendmail('su5mitsourav@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while (1):
        query = takeCommand().lower()
        # Logic for executing tasks
        if 'wikipedia' in query:
            speak("Searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open geeks for geeks' in query:
            webbrowser.open("geeksforgeeks.com")
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")
        elif 'play music' in query:
            music_dir = 'D:\\WEED HITS\\HITS'
            songs = os.listdir(music_dir)
            # print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'go to sleep' in query:
            speak("Good Bye, Sir!")
            sys.exit()
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, The time is {strTime}")
        elif 'you are awesome' in query:
            speak("Well, that is because you built me Sir")
        elif 'haha' in query:
            speak("L O L")
        elif 'open code' in query:
            codePath = "C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'send email' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "su5mitsourav@gmail.com"
                sendEmail(to, content)
                speak("Your email has been sent successfully sir.")
            except Exception as e:
                print(e)
                speak("Sorry Sir! Some Error Occured. Please Try again.")