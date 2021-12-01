from typing import Collection
from pymongo import MongoClient
from random import randint
import matplotlib.pyplot as plt
import numpy as np

from tkinter import * 
import tkinter.font as font

from tkinter import ttk
import threading
#Step 1: Connect to MongoDB - Note: Change connection string as needed
#mongodb+srv://bkeuria1:%40BingBong3779@cluster0.oa5dd.mongodb.net/Project3?retryWrites=true&w=majority
client = MongoClient('mongodb://localhost:27017/')
db=client.Movies
movies = db.movies

win=Tk()
win.title('Select a Language')
win.geometry("1000x800")

#This section helps to create a scrollbar for the entire gui
#https://stackoverflow.com/questions/19860047/python-tkinter-scrollbar-for-entire-window

main_frame = Frame(win)
main_frame.pack(fill=BOTH,expand=1)

canvas = Canvas(main_frame)
canvas.pack(pady = 20, side=LEFT,fill=BOTH, expand=1)

scrollbar = ttk.Scrollbar(main_frame,orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill = Y)
scrollbar.pack(side=RIGHT, fill = Y)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))


frame2 = Frame(canvas,pady = 40, padx = 350)

title_label = Label(canvas, text= "Please select one of the Following Languages")

title_label['font'] = ("Arial", 20)
title_label.pack(anchor='center')


canvas.create_window((0,0),window=frame2,anchor="nw")
language_services  = movies.aggregate(
    [   
    
         { "$project" : { "Split_Language" : { "$split": ["$Language", ","] },
           
         "Hulu": {
             "$cond": [{"$eq":["$Hulu",1]},1,0]
         },
          "Netflix": {
             "$cond": [{"$eq":["$Netflix",1]},1,0]
         },
           "Prime Video": {
             "$cond": [{"$eq":["$Prime Video",1]},1,0]
         },
          "Disney+": {
             "$cond": [{"$eq":["$Disney+",1]},1,0]
         }
         }
         },
        {"$unwind": "$Split_Language"},

          { "$group" : 
             { "_id":
                 { "Language" : "$Split_Language" }, "count":{"$sum":1} ,
          "Hulu" :{"$sum": "$Hulu"},
          "Netflix" : {"$sum": "$Netflix"},
          "Prime Video":{"$sum":"$Prime Video"},
          "Disney+":{"$sum":"$Disney+"}
          }
          },

        {"$sort":{'Language':1, '_id':1}}
       
         

    ]

)

language_dict= {}
def select_language(language_choice):
    language = language_dict[int(language_choice)]  
    print(language)
    prime = language['Prime Video']
    hulu = language['Hulu']
    netflix = language['Netflix']
    disney = language['Disney+']
    service_count_array = []
    #remove services with no support for a language
    service_dict = {"Prime Video": prime, "Hulu": hulu, "Netflix": netflix, "Disney+":disney}
    #remove values for the chart that have 
    service_lables = np.array([key for key,value in service_dict.items() if value!=0])
    service_result = np.array([value for value in service_dict.values() if value!=0])
    plot_title = "Movies and Shows in " + language['_id']['Language'] +" On Prime Video, Hulu, Netflix and Disney+"
    plt.title(plot_title.format(plot_title))
    plt.pie(service_result, labels = service_lables, autopct='%1.1f%%', shadow = True)
    plt.show()


print("Please Choose the following Languages")

for index, language in enumerate(language_services):
   
    language_dict[index] = language
    #need to use a lambda expression for passing in language
    #need to use index = index for lambda because when lambda select_language(index) is called, it 
    #looks for the value of index when it is called, so index would always be the last index (it ran through the for loop when it was called)
    #doing lambda index = index: select_language (index) means that the function will store the current value of index, instead of waiting
    #source:https://stackoverflow.com/questions/10865116/tkinter-creating-buttons-in-for-loop-passing-command-arguments
    temp_button = Button(frame2, text = str(index) + "." + language['_id']['Language'],command= lambda index = index: select_language (index), bg = "red", 
    padx= 15, pady=15)
    temp_button['font']  = font.Font(family='Arial')
    temp_button['fg'] =  '#ffffff'
    temp_button.grid(row = index, column = 1, padx=5, pady=5)
    
   

    print(str(index) + ". " + language['_id']['Language'])

win.mainloop()



