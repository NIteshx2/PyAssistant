#!/usr/bin/env python3
# Requires PyAudio and PySpeech.

import webbrowser as wb
import speech_recognition as sr
from tkinter import *
from time import ctime
import time
import os
from gtts import gTTS
import pygame
from pygame import mixer

def speak(audioString):
    global x
    b = audioString
    if len(b) == 0:
        #w1 = Label(root, text="No input!").pack()
        return
    tts = gTTS(text=b, lang='en-us')
    tts.save("voice%s.mp3"%(x))
    pygame.init()
    pygame.display.set_mode((2, 1))
    mixer.music.load("voice%s.mp3" % (x))
    mixer.music.play(0)

    x += 1

    clock = pygame.time.Clock()
    clock.tick(10)
    while pygame.mixer.music.get_busy():
        pygame.event.poll()
        clock.tick(10)


def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak...")
        audio = r.listen(source)
        print("heard...")
    # Speech recognition using Google Speech Recognition
    data = ""
 #    try:
 #    # for testing purposes, we're just using the default API key
 #    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
 #    # instead of `r.recognize_google(audio)`
 #    data = r.recognize_google(audio))
	#     print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
	# except sr.UnknownValueError:
 #    	print("Google Speech Recognition could not understand audio")
	# except sr.RequestError as e:
 #    	print("Could not request results from Google Speech Recognition service; {0}".format(e))



    try:
    # Uses the default API key
    # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said : " + data )
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    if "how are you" in data:
        speak("I am fine")

    elif "what time is it" in data:
        speak(ctime())

    elif "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on nitesh, I will show you where " + location + " is.")
        wb.open_new_tab("https://www.google.nl/maps/place/" + location + "/&amp;")
    else :
        speak(",,,,,,,I did not get what you said !")

    return data


def jarvis(data):
    if "how are you" in data:
        speak("I am fine")

    elif "what time is it" in data:
        speak(ctime())

    elif "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on nitesh, I will show you where " + location + " is.")
        wb.open_new_tab("https://www.google.nl/maps/place/" + location + "/&amp;")
    else :
        speak(",,,,,,,I did not get what you said !")





# initialization
root = Tk()
#a = StringVar()

root.title("Assistant")
root.geometry("400x400")
x=0

w = Label(root, text = "Hi, what can we do for you ?" , takefocus = True, font = " , 15").pack( side = LEFT)
#text = Entry(textvariable = a , bd = 8 , width = 60).pack()
but2 = Button(text = "quit" , command =root.quit , activebackground = "white", bg = "red", fg = "white", height = 2, width =10).pack(side = RIGHT)
but1 = Button(text='listen',bd = 4, command = recordAudio , height =2 , width=10, activebackground = "lightgreen").pack(side = RIGHT)

root.mainloop()






time.sleep(0.5)
# x=0
# print("start..")
# speak("Hi! Nitesh, what can I do for you?")
# data = recordAudio()
# jarvis(data)
# speak("Turning off the program.")
# print("Run complete")
