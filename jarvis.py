import cv2
import winsound
import datetime
import time
import os
import re
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import wikipedia  # pip install wikipedia
import webbrowser
import requests

from os import sys, path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from gtts import gTTS

from playsound import playsound

now = datetime.datetime.now()

dateStr = now.strftime("%Y-%m-%d  %H:%M:%S")

qn = input('Your name please!')
if qn.upper() == ('SUYOG'):
    def play_audio(path_of_audio):
        playsound(path_of_audio)


    def convert_to_audio(text):
        a = gTTS(text)
        a.save('h.mp3')
        play_audio('h.mp3')


    convert_to_audio("Oh! Really? I will check you !")

    pwws = int(input("Please enter your Password!"))

    if pwws == 787898:
        def play_audioo(path_of_audio):
            playsound(path_of_audio)


        def convert_to_audioo(text):
            ab = gTTS(text)
            ab.save('hh.mp3')
            play_audioo('hh.mp3')


        convert_to_audioo("You are welcome Here," + qn + ". I am switching into jarvis now.")
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        # print(voices[1].id)
        engine.setProperty('voice', voices[0].id)


        def speak(audio):
            engine.say(audio)
            engine.runAndWait()


        def wishMe():
            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour < 12:
                speak("Good Morning!" + qn)

            elif hour >= 12 and hour < 18:
                speak("Good Afternoon!" + qn)

            else:
                speak("Good Evening!" + qn)

            speak("Hey" + qn + "I am Jarvis Here. Please tell me how may I help you")


        def takeCommand():
            # It takes microphone input from the user and returns string output

            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                r.pause_threshold = 1
                audio = r.listen(source)

            try:
                print("Recognizing...")
                query = r.recognize_google(audio, language='en-in')
                print(f"User said: {query}\n")

            except Exception as e:
                # print(e)
                print("Say that again please...")
                return "None"
            return query


        if __name__ == "__main__":
            wishMe()
            while True:
                # if 1:
                query = takeCommand().lower()

                # Logic for executing tasks based on query
                if 'wikipedia' in query:
                    speak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)



                elif 'open youtube' in query:
                    webbrowser.open("youtube.com")

                elif 'open google' in query:
                    webbrowser.open("google.com")

                elif 'open facebook' in query:
                    webbrowser.open("facebook.com")


                elif 'open website' in query:
                    reg_ex = re.search('open website (.+)', query)
                    if reg_ex:
                        domain = reg_ex.group(1)
                        url = 'https://www.' + domain
                        webbrowser.open(url)
                        print('Done!')
                    else:
                        pass


                elif 'play music' in query:
                    music_dir = 'F:\\New folder'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir, songs[0]))

                elif 'the time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"Sir, the time is {strTime}")

                elif 'open english movie' in query:
                    codePath = "E:\\English Movies"
                    os.startfile(codePath)
                elif 'my name' in query:
                    speak("Your name is" + qn)
                elif 'who are you' in query:
                    speak("I am Jarvis(the computer program) and your personal asistance")
                elif 'what is your name' in query:
                    speak("I am Jarvis(the computer program) and your personal asistance")
                elif 'day today' in query:
                    speak(f"Sir, the time is {dateStr}")

                elif 'goodbye system' in query:
                    speak("Have a good day !" + qn)
                    exit()
                elif 'joke' in query:
                    res = requests.get(
                        'https://icanhazdadjoke.com/',
                        headers={"Accept": "application/json"}
                    )
                    if res.status_code == requests.codes.ok:
                        speak(str(res.json()['joke']))
                    else:
                        speak('oops!I ran out of jokes')








    else:
        def play_audiooo(path_of_audio):
            playsound(path_of_audio)


        def convert_to_audiooo(text):
            abc = gTTS(text)
            abc.save('hhh.mp3')
            play_audiooo('hhh.mp3')


        convert_to_audiooo(
            "You are a thief, I captured your face. " + qn + " .You tried to enter our system on" + dateStr)

        save = 'F:\Suyog Course\First Project'

        camera_port = 0
        camera = cv2.VideoCapture(camera_port)
        time.sleep(0.1)
        return_value, image = camera.read()
        cv2.imwrite(os.path.join(save, "Thief.png"), image)
        del camera

        winsound.PlaySound("alert", winsound.SND_FILENAME)



else:
    def play_audioooo(path_of_audio):
        playsound(path_of_audio)


    def convert_to_audioooo(text):
        abcd = gTTS(text)
        abcd.save('hhhh.mp3')
        play_audioooo('hhhh.mp3')


    convert_to_audioooo('Sorry ' + qn + ', you are not allowed here!')
    qnn = input('Who sent you though? ')
    if qnn.upper() == 'SUYOG':
        pws = int(input('Enter the password Khanal Sir said:'))
        if pws == 787898:
            def play_audiooooo(path_of_audio):
                playsound(path_of_audio)


            def convert_to_audiooooo(text):
                abcde = gTTS(text)
                abcde.save('hhhhh.mp3')
                play_audiooooo('hhhhh.mp3')


            convert_to_audiooooo("You are welcome Here " + qn)
            engine = pyttsx3.init('sapi5')
            voices = engine.getProperty('voices')
            # print(voices[1].id)
            engine.setProperty('voice', voices[1].id)


            def speak(audio):
                engine.say(audio)
                engine.runAndWait()


            def wishMe():
                hour = int(datetime.datetime.now().hour)
                if hour >= 0 and hour < 12:
                    speak("Good Morning!")

                elif hour >= 12 and hour < 18:
                    speak("Good Afternoon!")

                else:
                    speak("Good Evening!")

                speak("Hey" + qn + " I am Jarvis" + " Tell me how may I help you")


            def takeCommand():
                # It takes microphone input from the user and returns string output

                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Listening...")
                    r.pause_threshold = 3
                    audio = r.listen(source)

                try:
                    print("Recognizing...")
                    query = r.recognize_google(audio, language='en-in')
                    print(f"User said: {query}\n")

                except Exception as e:
                    # print(e)
                    print("Say that again please...")
                    return "None"
                return query


            if __name__ == "__main__":
                wishMe()
                while True:
                    # if 1:
                    query = takeCommand().lower()

                    # Logic for executing tasks based on query
                    if 'wikipedia' in query:
                        speak('Searching Wikipedia...')
                        query = query.replace("wikipedia", "")
                        results = wikipedia.summary(query, sentences=3)
                        speak("According to Wikipedia")
                        print(results)
                        speak(results)

                    elif 'open youtube' in query:
                        webbrowser.open("youtube.com")

                    elif 'open google' in query:
                        webbrowser.open("google.com")

                    elif 'open facebook' in query:
                        webbrowser.open("facebook.com")


                    elif 'play music' in query:
                        music_dir = 'F:\\New folder'
                        songs = os.listdir(music_dir)
                        print(songs)
                        os.startfile(os.path.join(music_dir, songs[0]))

                    elif 'the time' in query:
                        strTime = datetime.datetime.now().strftime("%H:%M:%S")
                        speak(f"Sir, the time is {strTime}")

                    elif 'open english movie' in query:
                        codePath = "E:\\English Movies"
                        os.startfile(codePath)

                    elif 'open website' in query:
                        reg_ex = re.search('open website (.+)', query)
                        if reg_ex:
                            domain = reg_ex.group(1)
                            url = 'https://www.' + domain
                            webbrowser.open(url)
                            print('Done!')
                        else:
                            pass


                    elif 'my name' in query:
                        speak("Your name is" + qn)
                    elif 'who are you' in query:
                        speak("I am Jarvis(the computer program) and Suyog's personal asistance")
                    elif 'what is your name' in query:
                        speak("I am Jarvis(the computer program) and your Suyog's asistance")
                    elif 'day today' in query:
                        speak(f"Sir, the time is {dateStr}")


                    elif 'goodbye system' in query:
                        speak("Have a good day " + qn)
                        exit()

                    elif 'joke' in query:
                        res = requests.get(
                            'https://icanhazdadjoke.com/',
                            headers={"Accept": "application/json"}
                        )
                        if res.status_code == requests.codes.ok:
                            speak(str(res.json()['joke']))
                        else:
                            speak('oops!I ran out of jokes')

        else:
            def play_audioooooo(path_of_audio):
                playsound(path_of_audio)


            def convert_to_audioooooo(text):
                abcdef = gTTS(text)
                abcdef.save('hhhhhh.mp3')
                play_audioooooo('hhhhhh.mp3')


            convert_to_audioooooo(
                "You are a thief, I captured your face" + qn + " You tried to enter our system on" + dateStr)
            save = 'F:\Suyog Course\First Project'

            camera_port = 0
            camera = cv2.VideoCapture(camera_port)
            time.sleep(0.1)
            return_value, image = camera.read()
            cv2.imwrite(os.path.join(save, "Thief.png"), image)
            del camera

            winsound.PlaySound("alert", winsound.SND_FILENAME)


    else:
        def play_audip(path_of_audio):
            playsound(path_of_audio)


        def convert_to_audip(text):
            abcdefg = gTTS(text)
            abcdefg.save('p.mp3')
            play_audip('p.mp3')


        convert_to_audip('Sorry ' + qnn + ' is not authorized person to send you here! ')

now = datetime.datetime.now()

dateStr = now.strftime("%Y-%m-%d  %H:%M:%S")
print(f"Date and Time: {dateStr} ")

