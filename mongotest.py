import pymongo

uri = "mongodb+srv://teja62:varsha9304604967@tejacluster0.jnzs2nx.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(uri)
db = client.test
print(db)

d = {
    "name": "teja",
    "email": "raviteja.teja62",
    "surname": "yenukoti"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)