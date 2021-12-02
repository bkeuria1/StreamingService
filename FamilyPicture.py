from pymongo import MongoClient
import pprint
import matplotlib.pyplot as plt

client = MongoClient(
    'mongodb+srv://eezor1:P%40lkij123@cluster0.oa5dd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client.Project3
collection = db.MovieStuff
net_cursor = collection.find({"$and": [{'Netflix': '1'}, {"$or": [{"Age": "7+"}, {"Age": "all"}]}]})
hul_cursor = collection.find({"$and": [{'Hulu': '1'}, {"$or": [{"Age": "7+"}, {"Age": "all"}]}]})
dis_cursor = collection.find({"$and": [{'Disney+': '1'}, {"$or": [{"Age": "7+"}, {"Age": "all"}]}]})
prime_cursor = collection.find({"$and": [{'Prime Video': '1'}, {"$or": [{"Age": "7+"}, {"Age": "all"}]}]})
streaming_cursors = [net_cursor, hul_cursor, dis_cursor, prime_cursor]
streaming_names = ["Netflix", "Hulu", "Disney+", "Prime Video"]


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
plt.title('Films and Shows for Children Available on Netflix, Hulu, Disney, and Prime Video')
plt.xlabel("Service Name")
plt.ylabel("Number of Films and Shows")
plt.show()



