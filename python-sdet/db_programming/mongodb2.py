from pymongo import MongoClient
conn = MongoClient("mongodb://localhost:27017/")
print(conn)

db = conn['ETA']
col = db['student']
mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]

return_val = col.insert_many(mylist)

print("Find One:")
doc = col.find_one()
print(doc)

print("Find All")
doc_cursor = col.find()
for doc in doc_cursor:
    print(doc)

# condition based search
curs=col.find({'Sex':'M'})
for doc in curs:
    print(doc)

# search using regex
print("Regex expression")
curs=col.find({'Name':{'$regex':'^R'}})
for row in curs:
    print(row)