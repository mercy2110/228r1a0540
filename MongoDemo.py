import pymongo
myclient=pymongo.MongoClient("mongodb://localhost:27017/")
print(myclient.list_database_names())
mydb=myclient["cmrec"]
'''mydblist=myclient.list_database_names()
if "cmrec" in mydblist:
    print("database is exists")
else:
    print("database does not exist")
'''
mycol=mydb["csea"]
'''
mylist=mydb.list_collection_names()
if "csea" in mylist:
    print("is exist")
else:
    print("does not exist")'''
mydict={"name":"mercy","Rollno":"228R1A0540"}
x=mycol.insert_one(mydict)
x=mycol.insert