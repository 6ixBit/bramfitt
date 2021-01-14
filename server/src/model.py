from pymongo import MongoClient

client = MongoClient('mongodb://root:password@mongo:27017/')
db = client.tfl_buses

def test_db():
    print("DB connection established...")

    try:
        db.list_database_names()
    except:
        print("Failed to list database names")
    
    

def insert_record():
    #TODO: loop over array of objs returned from controller and insert to db one by one.
    pass

def get_records():
    pass