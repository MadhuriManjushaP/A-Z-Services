import pymongo
connection = pymongo.MongoClient('localhost',27017)
database = connection["chat"]
collection = database["stu"]
print("database connected")
data = {'Name':"",'age':'','Email':"",'height':'','weight':'','Gender':""}
collection.insert_one(data)
connection.close()
