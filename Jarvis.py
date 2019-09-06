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
from audio import record
from jarvis_core import jarvis

x = 0


def speak(audioString):
    global x
    b = audioString
    if len(b) == 0:
        # w1 = Label(root, text="No input!").pack()
        return
    tts = gTTS(text=b, lang='en-us')
    tts.save("voice%s.mp3" % (x))
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


def welcome():
    message = """ Hi! I'm Jarvis, you personal assistant."
                  To improve our interactions, I just need to know your name."
                  Could you please tell me your name? """
    speak(message)


def get_user_name():
    name = input("Tell Jarvis your name : ")
    speak("Excellent " + str(name) + "! So, how can I help you? :)")
    return name


def main():
    print("Jarvis booting...")
    welcome()
    name = get_user_name()
    data = record()
    jarvis(data, name, speak)
    speak("Ok, I'm going for now. Bye.")
    print("Jarvis ended.")

    # initialization
'''root = Tk()
# a = StringVar()

root.title("Assistant")
root.geometry("400x120")
x=0

w = Label(root, text = "Hi, what can we do for you ?" , takefocus = True, font = " , 15").pack( side = LEFT)
# text = Entry(textvariable = a , bd = 8 , width = 60).pack()
but2 = Button(text = "quit" , command =root.quit , activebackground = "white", bg = "red", fg = "white", height = 2, width =10).pack(side = RIGHT)
but1 = Button(text='listen',bd = 4, command = recordAudio , height =2 , width=10, activebackground = "lightgreen").pack(side = RIGHT)

root.mainloop()
'''

if __name__ == "__main__":
    main()
