import pandas as pd
from pymongo import MongoClient
import json

def mongoimport(csv_path, db_database, coll_test, db_url='localhost', db_port=27017)
    client = MongoClient(db_url, db_port)
    db = client[db_database]
    coll = db[coll_test]
    data = pd.read_csv(C:/Users/matheus/Downloads/owid-covid-data-1)
    payload = json.loads(data.to_json(orient='records'))
    coll.remove()
    coll.insert(payload)
    return coll.count()
