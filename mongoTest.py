import pymongo
import pandas as pd
import json

client = pymongo.MongoClient("mongodb+srv://root:1234@cluster0.vjmqrjn.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
"""
# This is the first test table in the form of dictionary
d = {
    "name":"Vipul",
    "email": "vs@gmalil.com",
    "phone": 8871939189
}

db1 = client["mongotest"]
coll = db1["test"]
coll.insert_one(d)

data = pd.read_csv("Cars93.csv")
data = data.to_dict(orient="records")
"""

# This is Second table , which is the collection of data of Cars 93
# db1 = client["mongotest"]
# coll = db1["Cars93"]
# coll.insert_many(data)

## Here We are fetching that cars93.csv
readDB = client["mongotest"]

allData = readDB["Cars93"]
print(allData)

oneRow = allData.find_one()
print(oneRow)

full_Data = allData.find()

# for rows in full_Data:
#     print(rows)

CnvtList = list(full_Data)
print(CnvtList)

df = pd.DataFrame(CnvtList)
print(df.head())
