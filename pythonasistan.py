"""
@author: Grasiand
"""
from datetime import datetime
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import webbrowser
import random
import os
import datetime
import pywhatkit
import pyautogui

r = sr.Recognizer()

def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice = ''
        try:
            voice = r.recognize_google(audio, language='tr-TR')
        except sr.UnknownValueError:
            speak('anlayamadım')
        except sr.Recognizer:
            speak('sistem çalışmıyor')
        return voice

os.system("clear")

def response(voice):
    if 'nasılsın' in voice:
        speak('İyiyim, siz nasılsınız?')

    if 'saat kaç' in voice:
        speak(datetime.now().strftime('%H:%M:%S'))

    if 'arama yap' in voice:
        search = record('ne aramak istiyorsunuz?')
        url = 'https://www.google.com/search?q=' + search
        webbrowser.get().open(url)
        speak(search + ' için bulduklarım')

    if 'müzik' in voice:
        os.system("spotify")
        
    if 'seni kim yaptı' in voice:
        speak('Grasiand,Kerem')

    if 'YouTube' in voice:
        url = 'youtube.com'
        webbrowser.get().open(url)
        speak('bekle')

    if 'binary nedir' in voice:
       speak("İkili Kod (Binary),iki sayıdan oluşan bir sayı sistemidir.")

    if 'Mister robot' in voice:
       url = 'https://www.tekfullfilmizle2.com/mr-robot-4-sezon-3-bolum-turkce-dublaj-izle.html'
       webbrowser.get().open(url)
       speak('iyi seyirler')

    if 'Instagram' in voice:
       url = 'instagram.com'
       webbrowser.get().open(url)
       speak('Hoşgeldin')


       pyautogui.press('enter')


    if 'kapan' in voice:
        speak('Görüşürüz ')
        pyautogui.hotkey('alt', 'f4')
        pyautogui.hotkey('enter')
        
        exit()

def speak(string):
    tts = gTTS(string, lang='tr')
    rand = random.randint(1, 10000)
    file = 'audio-' + str(rand) + '.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)

speak('Nasıl yardımcı olabilirim?, Kerem')
while True:
    voice = record()
    print(voice)
    response(voice)
