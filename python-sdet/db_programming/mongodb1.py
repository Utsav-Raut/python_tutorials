from pymongo import MongoClient
conn = MongoClient("mongodb://localhost:27017/")
print(conn)

db = conn['ETA']
col = db['student']
document = {'Name': 'John', 'Regd_id': '1', 'Age': 20, 'Sex': 'M'}
return_val = col.insert_one(document)

db_list = conn.list_database_names()
col_list = db.list_collection_names()

print(db_list)
print(col_list)
print(return_val)
print(return_val.inserted_id)