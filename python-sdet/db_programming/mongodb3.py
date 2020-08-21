from pymongo import MongoClient
conn=MongoClient('mongodb://localhost:27017/')
db=conn['ETA']
col=db['student']
# curs=col.find({},{'_id':0,'Name':1,'Age':1})
curs=col.find({},{'_id':0,'name':1})
for row in curs:
    print(row)


# sorting records... sort(key, order)..
# from pymongo import MongoClient
# conn=MongoClient('mongodb://localhost:27017/')
# db=conn['ETA']
# col=db['student']
# curs=col.find({}).sort('Age',1)
# for row in curs:
#     print(row)

# limiting no of records displayed
# from pymongo import MongoClient
# conn=MongoClient('mongodb://localhost:27017/')
# db=conn['ETA']
# col=db['student']
# curs=col.find({},{'_id':0,'Regd_id':1,'Age':1}).limit(2)
# for row in curs:
#     print(row)


# deleting
# from pymongo import MongoClient
# conn=MongoClient('mongodb://localhost:27017/')
# db=conn['ETA']
# col=db['student']
# col.delete_one({'Regd_id':'1'})
# col.delete_many({'Regd_id':'2'})
# curs=col.find({})
# for row in curs:
#     print(row)

# Delete_many will return a delete object.
# Delete object has an attribute deleted_count which holds the number of records deleted.


# updating
# from pymongo import MongoClient
# conn=MongoClient('mongodb://localhost:27017/')
# db=conn['ETA']
# col=db['student']
# col.update_one({'Regd_id':'3'},{'$set':{'Age':25}})
# col.update_many({'Regd_id':{'$gt':'4'}},{'$set':{'Age':24}})
# curs=col.find({},{'_id':0,'Regd_id':1,'Age':1})
# for row in curs:
#     print(row)

# update_many will return a update object.
# update object has an attribute modified_count which holds the number of records updated.


# dropping collection
# from pymongo import MongoClient
# conn=MongoClient('mongodb://localhost:27017/')
# db=conn['ETA']
# col=db['student']
# print('Before Dropping the collection:')
# for doc in col.find():
#     print(doc)
# col.drop()
# print('After Dropping the collection:')
# for doc in col.find():
#     print(doc)
