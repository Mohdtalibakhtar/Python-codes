def speak(str):
    from win32com.client import Dispatch
    speak= Dispatch("SAPI.SpVoice")
    speak.Speak(str)

import json
import requests
if __name__ == '__main__':
    url=("http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=8f0956fb36524e9297c692fb56d610a1")
    response= requests.get(url)
    text= response.text
    js=json.loads(text)
    for i in range(0,11):
         speak(js['articles'][i]['title'])