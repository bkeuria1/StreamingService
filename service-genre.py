from typing import Collection
from pymongo import MongoClient, collection
from random import randint
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
import tkinter.font as font
from tkinter import ttk
import pprint
#Step 1: Connect to MongoDB - Note: Change connection string as needed
client = MongoClient('mongodb+srv://eezor1:P%40lkij123@cluster0.oa5dd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db=client.Project3
movie_collection = db.MovieStuff


win=Tk()
win.title('Select a Genres')
win.geometry("1000x800")

#This section helps to create a scrollbar for the entire gui
#https://stackoverflow.com/questions/19860047/python-tkinter-scrollbar-for-entire-window

main_frame = Frame(win)
main_frame.pack(fill=BOTH,expand=1)

canvas = Canvas(main_frame)
canvas.pack(pady = 20, side=LEFT,fill=BOTH, expand=1)

scrollbar = ttk.Scrollbar(main_frame,orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill = Y)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))


frame2 = Frame(canvas,pady = 40, padx = 350)

title_label = Label(canvas, text= "Please select one of the Following Genress")

title_label['font'] = ("Arial", 20)
title_label.pack(anchor='center')


canvas.create_window((0,0),window=frame2,anchor="nw")
Genres_services  = movie_collection.aggregate(
    [   
    
         { "$project" : { "Split_Genres" : { "$split": ["$Genres", ","] },
           
         "Hulu": {
             "$cond": [{"$eq":["$Hulu",'1']},1,0]
         },
          "Netflix": {
             "$cond": [{"$eq":["$Netflix",'1']},1,0]
         },
           "Prime Video": {
             "$cond": [{"$eq":["$Prime Video",'1']},1,0]
         },
          "Disney+": {
             "$cond": [{"$eq":["$Disney+",'1']},1,0]
         }
         }
         },
        {"$unwind": "$Split_Genres"},

          { "$group" : 
             { "_id":
                 { "Genres" : "$Split_Genres" }, "count":{"$sum":1} ,
          "Hulu" :{"$sum": "$Hulu"},
          "Netflix" : {"$sum": "$Netflix"},
          "Prime Video":{"$sum":"$Prime Video"},
          "Disney+":{"$sum":"$Disney+"}
          }
          },

        {"$sort":{'Genres':1, '_id':1}}
            
    ]
)

Genres_dict= {}
def select_Genres(Genres_choice):
    Genres = Genres_dict[int(Genres_choice)]  
    print(Genres)
    prime = Genres['Prime Video']
    hulu = Genres['Hulu']
    netflix = Genres['Netflix']
    disney = Genres['Disney+']
    service_count_array = []
    #remove services with no support for a Genres
    service_dict = {"Prime Video": prime, "Hulu": hulu, "Netflix": netflix, "Disney+":disney}
    #remove values for the chart that have 
    service_lables = np.array([key for key,value in service_dict.items() if value!=0])
    service_result = np.array([value for value in service_dict.values() if value!=0])
    plot_title = Genres['_id']['Genres']+ " Movies and Shows"  +" On Prime Video, Hulu, Netflix and Disney+"
    plt.title(plot_title.format(plot_title))
    plt.pie(service_result, labels = service_lables, autopct='%1.1f%%')
    plt.show()


print("Please Choose the following Genress")

for index, Genres in enumerate(Genres_services):
   
    Genres_dict[index] = Genres
    #need to use a lambda expression for passing in Genres
    #need to use index = index for lambda because when lambda select_Genres(index) is called, it 
    #looks for the value of index when it is called, so index would always be the last index (it ran through the for loop when it was called)
    #doing lambda index = index: select_Genres (index) means that the function will store the current value of index, instead of waiting
    #source:https://stackoverflow.com/questions/10865116/tkinter-creating-buttons-in-for-loop-passing-command-arguments
    temp_button = Button(frame2, text = str(index) + "." + Genres['_id']['Genres'],command= lambda index = index: select_Genres (index), bg = "red", 
    padx= 15, pady=15)
    temp_button['font']  = font.Font(family='Arial')
    temp_button['fg'] =  '#ffffff'
    temp_button.grid(row = index, column = 1, padx=5, pady=5)
    
   

    #print(str(index) + ". " + Genres['_id']['Genres'])


win.mainloop()