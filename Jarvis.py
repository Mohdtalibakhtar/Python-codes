import pyttsx3
import datetime
import speech_recognition as sr
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour= int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening")

    speak("Hello I'm Jarvis, How may i help you")

def takecommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query= r.recognize_google(audio, language='en-in')
        print(f"user said {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again Please")
        return "None"
    return query


if __name__ == '__main__':
    wishme()
    takecommand()