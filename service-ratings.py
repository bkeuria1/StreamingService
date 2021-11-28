from typing import Collection
from pymongo import MongoClient
from random import randint
import matplotlib.pyplot as plt
import numpy as np

def find_average(service,rating):
    #breakpoint()
    index = 0
    sum_rating = 0

    for doc in service:
        if doc[rating] != "":
            index += 1
            num_rating = float(doc[rating].split("/")[0])
            if rating == "IMDb":
                num_rating = num_rating*10
            sum_rating += num_rating
    #need to reset cursor, so that we can use the same cursor twice
    service.rewind()
    return round(sum_rating/service.count(),2)


client = MongoClient('mongodb://localhost:27017/')
db=client.Movies
movies = db.movies
disney = movies.find({"Disney+":1})
prime = movies.find({"Prime Video":1})
hulu = movies.find({"Hulu":1})
netflix = movies.find({"Netflix":1})
#get the rotten tomato average for each streaming service

labels = ["Prime Video", "Disney+", "Hulu", "Netflix"]
rotten_tomatoes_avg = [find_average(prime,"Rotten Tomatoes"), find_average(disney,"Rotten Tomatoes"), find_average(hulu,"Rotten Tomatoes"), find_average(netflix,"Rotten Tomatoes")]
IMDb_avg = [find_average(prime,"IMDb"), find_average(disney,"IMDb"), find_average(hulu,"IMDb"), find_average(netflix,"IMDb")]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, rotten_tomatoes_avg, width, label='Rotten Tomatoes')
rects2 = ax.bar(x + width/2, IMDb_avg, width, label='IMDb')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Average Rating (out of 100)')
ax.set_title('Average ratings for Movies and Shows on Popular Streaming Services')
ax.set_xticks(x, labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()
plt.show()