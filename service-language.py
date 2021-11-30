from typing import Collection
from pymongo import MongoClient
from random import randint
import matplotlib.pyplot as plt
import numpy as np
#Step 1: Connect to MongoDB - Note: Change connection string as needed
#mongodb+srv://bkeuria1:%40BingBong3779@cluster0.oa5dd.mongodb.net/Project3?retryWrites=true&w=majority
client = MongoClient('mongodb://localhost:27017/')
db=client.Movies
movies = db.movies


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
          }
       
         

    ]

)

language_dict= {}
print("Please Choose the following Languages")
for index, language in enumerate(language_services):
    language_dict[index] = language
    print(str(index) + ". " + language['_id']['Language'])

language_choice = input("Your Language choice: ") #number for language
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
plot_title = "Number of Movies and Shows in " + language['_id']['Language'] +" On Prime Video, Hulu, Netflix and Disney+"
plt.title(plot_title.format(plot_title))
plt.pie(service_result, labels = service_lables, autopct='%1.1f%%', shadow = True)
plt.show()

