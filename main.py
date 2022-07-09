from multiprocessing.connection import wait
import pyttsx3
import time
from pygame import mixer


while True:
    #get the text needed and convert it to mp3
    text = input('Enter your text: ')
    print('saying: ' + text)
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.save_to_file(text, 'text.mp3')
    engine.runAndWait()
    print('\n')