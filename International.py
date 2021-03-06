from pymongo import MongoClient
import pprint
import matplotlib.pyplot as plt

client = MongoClient(
    'mongodb+srv://eezor1:P%40lkij123@cluster0.oa5dd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client.Project3
collection = db.MovieStuff
net_cursor = collection.find({"$and": [{'Netflix': '1'}, {"$and": [{"Country": {"$not": {"$regex": "United States"}}},
                                                                  {"Language": {"$not": {"$regex": "English"}}}]}]})
hul_cursor = collection.find({"$and": [{'Hulu': '1'}, {"$and": [{"Country": {"$not": {"$regex": "United States"}}},
                                                               {"Language": {"$not": {"$regex": "English"}}}]}]})
dis_cursor = collection.find({"$and": [{'Disney+': '1'}, {"$and": [{"Country": {"$not": {"$regex": "United States"}}},
                                                                  {"Language": {"$not": {"$regex": "English"}}}]}]})
prime_cursor = collection.find({"$and": [{'Prime Video': '1'}, {"$and":
                                                                    [{"Country": {"$not": {"$regex": "United States"}}},
                                                                     {"Language": {"$not": {"$regex": "English"}}}]}]})
streaming_cursors = [net_cursor, hul_cursor, dis_cursor, prime_cursor]
streaming_names = ["Netflix", "Hulu", "Disney+", "Prime Video"]



"""
Query: Find the streaming service which has the best movies for kids
Appropriate Ages: 7+ and All
Sort by Streaming Services
Find which one has the most which fit that category

Steps/Pseudo Code
For X in Streaming Services:
    Find all movies with Ages of 7+ or All
    store results in tuple
    add tuple to array Results
Return Max results 
"""

streaming_results = []
values = []
labels =  []
results = []
for x in range(4):
    stream_list = list(streaming_cursors[x])
    num_items = len(stream_list)
    #streaming_results.append((streaming_names[x], num_items))
    labels.append(streaming_names[x])
    results.append(num_items)
    print(num_items)
barColors= ['red', 'green','blue','orange']
plt.bar(labels, results, color= barColors)
plt.title('Streaming Services with Most International Outreach')
plt.xlabel("Service Name")
plt.ylabel("Number of Films and Shows")
plt.show()
