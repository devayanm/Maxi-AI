import pyttsx3  #pip install pyttsx3
import datetime  #module
import speech_recognition as sr  #pip install speech_recognition
import wikipedia  #pip install wikipedia
import smtplib
import webbrowser as wb
import os  #inbuilt
import pyautogui  #pip install pyautogui
import psutil  #pip install psutil
import pyjokes  # pip install pyjokes
import soundfile as sf
import noisereduce as nr
import numpy as np
import requests
import json
import googletrans

# Initializing the speech synthesis engine
engine = pyttsx3.init()
engine.setProperty('rate', 190)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('volume', 1)

# Function to change the voice of the assistant


def voice_change(v):
    x = int(v)
    engine.setProperty('voice', voices[x].id)
    speak("done sir")

# Function to speak the given text


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to get the current time


def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("The current time is")
    speak(Time)

# Function to get the current date


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

# Function to determine the appropriate greeting based on the time of day


def checktime(tt):
    hour = datetime.datetime.now().hour
    if ("morning" in tt):
        if (hour >= 6 and hour < 12):
            speak("Good morning sir")
        else:
            if (hour >= 12 and hour < 18):
                speak("it's Good afternoon sir")
            elif (hour >= 18 and hour < 24):
                speak("it's Good Evening sir")
            else:
                speak("it's Goodnight sir")
    elif ("afternoon" in tt):
        if (hour >= 12 and hour < 18):
            speak("it's Good afternoon sir")
        else:
            if (hour >= 6 and hour < 12):
                speak("Good morning sir")
            elif (hour >= 18 and hour < 24):
                speak("it's Good Evening sir")
            else:
                speak("it's Goodnight sir")
    else:
        speak("it's night sir!")

# Function to greet the user based on the time of day


def wishme():
    speak("Welcome Back")
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak("Good Morning sir!")
    elif (hour >= 12 and hour < 18):
        speak("Good afternoon sir")
    elif (hour >= 18 and hour < 24):
        speak("Good Evening sir")
    else:
        speak("Goodnight sir")

    speak("Hii, I am Maxi ")

# Function to bid farewell to the user


def wishme_end():
    speak("signing off")
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak("Good Morning")
    elif (hour >= 12 and hour < 18):
        speak("Good afternoon")
    elif (hour >= 18 and hour < 24):
        speak("Good Evening")
    else:
        speak("Goodnight.. Sweet dreams")
    quit()

# Function to capture audio from the microphone
def capture_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    return audio


# Function to reduce noise in audio
def reduce_noise(audio_data, sample_rate):
    reduced_noise = nr.reduce_noise(audio_clip=audio_data, noise_clip=audio_data)
    return reduced_noise, sample_rate


# Function to perform speech recognition on audio
def recognize_speech(audio):
    try:
        recognized_text = sr.recognize_google(audio, language="en-in")
        return recognized_text
    except Exception as e:
        print(e)
        return None

# Function to send an email


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("user-name@xyz.com", "pwd")
    server.sendmail("user-name@xyz.com", to, content)
    server.close()

# Function to take a screenshot


def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\Maxi-AI-using-python3-\\screenshots\\ss.png")

# Function to get CPU and battery usage


def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU usage is at ' + usage)
    print('CPU usage is at ' + usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)
    print("battery is at:" + str(battery.percent))

# Function to tell a joke


def jokes():
    j = pyjokes.get_joke()
    print(j)
    speak(j)
    

# Function to get weather information


def weather():
    api_key = "YOUR-API_KEY"  # generate your own api key from open weather
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    speak("tell me which city")
    city_name = capture_audio()
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        r = ("in " + city_name + " Temperature is " +
             str(int(current_temperature - 273.15)) + " degree celsius " +
             ", atmospheric pressure " + str(current_pressure) + " hpa unit" +
             ", humidity is " + str(current_humidiy) + " percent"
             " and " + str(weather_description))
        print(r)
        speak(r)
    else:
        speak(" City Not Found ")

# Function to provide information about Maxi


def personal():
    speak("I am Maxi, version 1.0, I am an AI voice assistent, I am developed by Devayan on 01 June 2023 in INDIA")
    speak("Now i hope you know me")


# Function to search for images using Bing Image Search API
def image_search(query):
    api_key = "YOUR_BING_API_KEY"  # Replace with your Bing API key
    endpoint = "https://api.bing.microsoft.com/v7.0/images/search"
    headers = {"Ocp-Apim-Subscription-Key": api_key}
    params = {"q": query, "count": 5}  # Adjust the count as per your requirement

    try:
        response = requests.get(endpoint, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        if "value" in data:
            images = data["value"]
            for image in images:
                image_url = image["contentUrl"]
                print(image_url)
                # You can perform further actions with the image URLs, such as displaying or downloading them
        else:
            print("No images found.")

    except requests.exceptions.RequestException as e:
        print("Error occurred during image search:", str(e))
    except json.JSONDecodeError:
        print("Error parsing the API response.")
    except KeyError:
        print("Unexpected response from the API.")


# Function to translate text
def translate_text(text, src_lang, dest_lang):
    translator = googletrans.Translator()
    translated = translator.translate(text, src=src_lang, dest=dest_lang)
    return translated.text

# Function to translate text with exception handling
def translate():
    try:
        speak("What text would you like to translate?")
        text = capture_audio()
        speak("Which language is the text in?")
        src_lang = capture_audio()
        speak("Which language would you like to translate it to?")
        dest_lang = capture_audio()
        translated_text = translate_text(text, src_lang, dest_lang)
        if translated_text:
            speak("The translated text is:")
            speak(translated_text)
        else:
            speak("Sorry, I couldn't translate the text.")
    except Exception as e:
        print(e)
        speak("Sorry, there was an error in translating the text.")



if __name__ == "__main__":
    wishme()
    while (True):
        query = capture_audio().lower()

        # Handling various user commands

        # Time
        if ('time' in query):
            time()

        # Date
        elif ('date' in query):
            date()

        # Personal info
        elif ("tell me about yourself" in query):
            personal()
        elif ("about you" in query):
            personal()
        elif ("who are you" in query):
            personal()
        elif ("yourself" in query):
            personal()

        # Developer info
        elif ("developer" in query or "tell me about your developer" in query
              or "father" in query or "who develop you" in query
              or "developer" in query):
            res = open("about.txt", 'r')
            speak("here is the details: " + res.read())

        # Searching on Wikipedia
        elif ('wikipedia' in query or 'what' in query or 'who' in query
              or 'when' in query or 'where' in query):
            speak("searching...")
            query = query.replace("wikipedia", "")
            query = query.replace("search", "")
            query = query.replace("what", "")
            query = query.replace("when", "")
            query = query.replace("where", "")
            query = query.replace("who", "")
            query = query.replace("is", "")
            result = wikipedia.summary(query, sentences=2)
            print(query)
            print(result)
            speak(result)

        # Sending email
        elif ("send email" in query):
            try:
                speak("What is the message for the email")
                content = capture_audio()
                to = 'reciever@xyz.com'
                sendEmail(to, content)
                speak("Email has sent")
            except Exception as e:
                print(e)
                speak("Unable to send email check the address of the recipient")

        # Searching on Google or opening a website
        elif ("search on google" in query or "open website" in query):
            speak("What should i search or open?")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = capture_audio().lower()
            wb.get(chromepath).open_new_tab(search + '.com')

        # System actions - logout, restart, shut down
        elif ("logout" in query):
            os.system("shutdown -1")
        elif ("restart" in query):
            os.system("shutdown /r /t 1")
        elif ("shut down" in query):
            os.system("shutdown /r /t 1")

        # Play songs
        elif ("play songs" in query):
            speak("Playing...")
            songs_dir = "C:\\Music"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[1]))
            quit()

        # Reminder function
        elif ("create a reminder list" in query or "reminder" in query):
            speak("What is the reminder?")
            data = capture_audio()
            speak("You said to remember that" + data)
            reminder_file = open("data.txt", 'a')
            reminder_file.write('\n')
            reminder_file.write(data)
            reminder_file.close()

        # Reading reminder list
        elif ("do you know anything" in query or "remember" in query):
            reminder_file = open("data.txt", 'r')
            speak("You said me to remember that: " + reminder_file.read())

        # Taking a screenshot
        elif ("screenshot" in query):
            screenshot()
            speak("Done!")

        # CPU and battery usage
        elif ("cpu and battery" in query or "battery" in query
              or "cpu" in query):
            cpu()

        # Jokes
        elif ("tell me a joke" in query or "joke" in query):
            jokes()

        # Weather
        elif ("weather" in query or "temperature" in query):
            weather()
            
        # Image search
        elif ("search images" in query or "find images" in query):
            speak("What images would you like to search for?")
            search_query = capture_audio()
            speak("Searching images...")
            image_search(search_query)

        # Maxi features
        elif ("tell me your features" in query or "help" in query
              or "features" in query):
            features = ''' i can help to do lot many things like..
            i can tell you the current time and date,
            i can tell you the current weather,
            i can tell you battery and cpu usage,
            i can create the reminder list,
            i can take screenshots,
            i can search images,
            i can send email to your boss or family or your friend,
            i can shut down or logout or hibernate your system,
            i can tell you non funny jokes,
            i can open any website,
            i can search the thing on wikipedia,
            i can change my voice from male to female and vice-versa
            And yes one more thing, My boss is working on this system to add more features...,
            tell me what can i do for you??
            '''
            print(features)
            speak(features)

        # Greetings and voice change
        elif ("hii" in query or "hello" in query or "goodmorning" in query
              or "goodafternoon" in query or "goodnight" in query
              or "morning" in query or "noon" in query or "night" in query):
            query = query.replace("Maxi", "")
            query = query.replace("hi", "")
            query = query.replace("hello", "")
            if ("morning" in query or "night" in query or "goodnight" in query
                    or "afternoon" in query or "noon" in query):
                checktime(query)
            else:
                speak("what can i do for you")

        # Changing voice
        elif ("voice" in query):
            speak("for female say female and, for male say male")
            q = capture_audio()
            if ("female" in q):
                voice_change(1)
            elif ("male" in q):
                voice_change(0)
        elif ("male" in query or "female" in query):
            if ("female" in query):
                voice_change(1)
            elif ("male" in query):
                voice_change(0)

        # Translation
        elif 'translate' in query or 'translation' in query:
            translate()
            
        # Exit function
        elif ('i am done' in query or 'bye bye Maxi' in query
              or 'go offline Maxi' in query or 'bye' in query
              or 'nothing' in query):
            wishme_end()
