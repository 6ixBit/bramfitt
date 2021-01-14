from pymongo import MongoClient
from flask import jsonify

client = MongoClient("mongodb+srv://admin:bramfitt@cluster0.sz4ej.mongodb.net/tfl_db?retryWrites=true&w=majority")
db = client["tfl_db"]
collection = db["buses"]

def insert_records(records: list):
    try:
        for record in records:
            collection.insert_one(record)
            del record["_id"]
    except:
        print("Failed to insert records")

def get_all_records():
    records = collection.find({})

    result = []
    for record in records:
        del record['_id']
        result.append(record)
    
    return jsonify(result)


    