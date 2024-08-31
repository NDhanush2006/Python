import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
        speak("Opening Youtube!...")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
        speak(f"Openin{song}")
        
if __name__ == "__main__":
    speak("Starting Jarvis....")
    while True:
        r = sr.Recognizer()
        
        print("recognizing....")
        try:
            with sr.Microphone() as source:
                print("Listening......")
                audio = r.listen(source, timeout=1,phrase_time_limit=3)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Yes sir!..")
                with sr.Microphone() as source:
                    print("Jarvis Activated......")
                    audio = r.listen(source, timeout=1,phrase_time_limit=3)
                    command = r.recognize_google(audio)

                    processcommand(command)

                # Listen for command
        except Exception as e:
            print("Error; {0}".format(e))


