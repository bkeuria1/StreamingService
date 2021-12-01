import numpy
import os
import sys
from pymongo import MongoClient
import pprint
from tkinter import *
from threading import Thread
import subprocess
window=Tk()
console_output=Text(window)

window.title("Running Python Script")
window.geometry('600x600')
textbox = Text(window)
T = Text(window)


def service_genre():

    os.system('python service-genre.py')

def service_language():
    os.system('python service-language.py')


def service_ratings():
    os.system('python service-ratings.py')

def service_family():
    os.system('python FamilyPicture.py')

def service_international():
    os.system('python International.py')

bHeight = 5
bWidth = 40
#need to use lambda so that the function doesn't execute immediatly after the button is clicked
#each of its files has GUI and each one runs on mainLoop
#to prevent the program from crashing, each gui gets its own thread
genreBtn = Button(window, text="Best Service for Prefered Genre?", bg="green", fg="white", height = bHeight, width = bWidth,command= lambda:Thread(target = service_genre).start())
genreBtn.pack(anchor='center', pady =20)

#put eac
languageBtn = Button(window, text="Best Service for your Language?", bg="blue",fg="white",height = bHeight, width = bWidth,command = lambda:Thread(target = service_language).start() )
languageBtn.pack(anchor='center',padx = 20 )

ratingsBtn = Button(window, text="Better Ratings?", bg="red", fg="white",height = bHeight, width = bWidth,command =  lambda:Thread(target = service_ratings).start())
ratingsBtn.pack(anchor='center',pady =20)

ratingsBtn = Button(window, text="Best service for Children?", bg="purple", fg="white",height = bHeight, width = bWidth,command =  lambda:Thread(target = service_family).start())
ratingsBtn.pack(anchor='center',pady = 20)

internationalBtn = Button(window, text="Best service for International Audiences?", bg="orange", fg="white",height = bHeight, width = bWidth,command =  lambda:Thread(target = service_international).start())
internationalBtn.pack(anchor='center',pady = 20)
window.mainloop()
