import numpy
from pymongo import MongoClient
import pprint
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from tkinter import *



def compare_maximum(s_r):
    values = []
    comp_max = 0
    winner = None
    for item, _tuple in enumerate(s_r):
        title = _tuple[0]
        num = _tuple[1]
        values.append(num)
        if num > comp_max:
            comp_max = _tuple[1]
            winner = _tuple
    return winner, values


client = MongoClient(
    'mongodb+srv://eezor1:P%40lkij123@cluster0.oa5dd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client.Project3
collection = db.MovieStuff

net_cursor = collection.find({"$and": [{'Netflix': '1'}, {"$or": [{"Country": {"$not": {"$regex": "United States"}}},
                                                                  {"Language": {"$not": {"$regex": "English"}}}]}]})
hul_cursor = collection.find({"$and": [{'Hulu': '1'}, {"$or": [{"Country": {"$not": {"$regex": "United States"}}},
                                                               {"Language": {"$not": {"$regex": "English"}}}]}]})
dis_cursor = collection.find({"$and": [{'Disney+': '1'}, {"$or": [{"Country": {"$not": {"$regex": "United States"}}},
                                                                  {"Language": {"$not": {"$regex": "English"}}}]}]})
prime_cursor = collection.find({"$and": [{'Prime Video': '1'}, {"$or":
                                                                    [{"Country": {"$not": {"$regex": "United States"}}},
                                                                     {"Language": {"$not": {"$regex": "English"}}}]}]})
streaming_cursors = [net_cursor, hul_cursor, dis_cursor, prime_cursor]
streaming_names = ["Netflix", "Hulu", "Disney+", "Prime Video"]

streaming_results = []
for x in range(4):
    stream_list = list(streaming_cursors[x])
    num_items = len(stream_list)
    streaming_results.append((streaming_names[x], num_items))
output = compare_maximum(streaming_results)
pprint.pprint(output[0])

window = Tk()
window.title('Streaming Service Query Manager')
window.geometry("1000x800")
fp_button = Button(master=window, height=2, width=10, text="Plot")
fp_button.pack()
fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)
width = .5
temp = compare_maximum(streaming_results)
values = temp[1]
rects = ax.bar(streaming_names, values, width)
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.draw()
canvas.get_tk_widget().pack(side='top', fill='both', expand=1)
# runs the gui
window.mainloop()
