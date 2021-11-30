import numpy
import os
import sys
from pymongo import MongoClient
import pprint
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from tkinter import *


window=Tk()
console_output=Text(window)

window.title("Running Python Script")
window.geometry('550x200')
textbox = Text(window)
T = Text(window)


def service_genre():
    os.system('python service-genre.py')

def service_language():

    os.system('python service-language.py')

def service_rating():
    os.system('python service-ratings.py')


genreBtn = Button(window, text="Prefered Genre?", bg="black", fg="white",command=service_genre)
genreBtn.grid(column=0, row=0)

languageBtn = Button(window, text="Language Spoken?", bg="black", fg="white",command=service_language)
languageBtn.grid(column=0, row=4)

ratingsBtn = Button(window, text="Better Ratings?", bg="black", fg="white",command=service_language)
ratingsBtn.grid(column=0, row=6)
window.mainloop()
