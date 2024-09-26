import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyjokes
import datetime
import pyautogui
import requests
# init pyttsx
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty('voice', voices[1].id)  # 1 for female and 0 for male voice


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said: " + query + "\n")
    except Exception as e:
        print(e)
        speak("I didnt understand")
        return "None"
    return query

def get_random_fact():
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    
    try:
        response = requests.get(url)
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            return data['text']  # Extract and return the fact
        else:
            return f"Error: Unable to retrieve fact. Status code {response.status_code}"
    
    except Exception as e:
        return f"An error occurred: {e}"
def get_quote():
    try:
        response = requests.get("https://zenquotes.io/api/random")
        if response.status_code == 200:
            quote = response.json()[0].get('q', "Sorry, I couldn't find a quote.")
            return quote
        else:
            return "Sorry, I couldn't fetch a quote at the moment."
    except Exception as e:
        return f"An error occurred: {e}"




if __name__ == '__main__':

    speak("I hope you can tolerate mishearing")
    speak("How can i help")
    while True:
        query = take_command().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia ...")
            query = query.replace("wikipedia", '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif 'are you' in query:
            speak("I AM YOUR FATHER")
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")
        elif 'open github' in query:
            speak("opening github")
            webbrowser.open("github.com")
        elif 'open stackoverflow' in query:
            speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com")
        elif 'open spotify' in query:
            speak("opening spotify")
            webbrowser.open("spotify.com")
        #elif 'open whatsapp' in query:
        #    speak("opening whatsapp")
        #     loc = "C:\\Users\\Zanny\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
        #     os.startfile(loc)'''
        elif 'play music' in query:
            speak("opening music")
            webbrowser.open("spotify.com")
        elif 'local disk e' in query:
            speak("opening local disk E")
            webbrowser.open("E://")
        elif 'weather' in query:
            speak("Opening weather information")
            webbrowser.open("https://www.google.com/search?q=weather")   
        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)
        elif 'time' in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {current_time}")
        elif 'take a screenshot' in query:
            screenshot = pyautogui.screenshot()
            screenshot.save("screenshot.png")
            speak("Screenshot taken and saved as screenshot.png")
        elif 'give me a fact' in query:
            fact = get_random_fact()
            print(fact)
            speak(f"Here's a fact: {fact}")
        elif 'give me a quote' in query:
            quote = get_quote()
            print(quote)
            speak(f"Here's a quote: {quote}")
        elif 'sleep' in query:
            exit(0)