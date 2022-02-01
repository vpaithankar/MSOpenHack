from pymongo import MongoClient

conn_str = "mongodb://dbohicecreamratings:YDjwWB1PW7C4lJjKxS2s4LDY99BVocbqErOV36YKTQ56eDYI2hJg5ASV1G9qFovTzjuTE8dnWCO2JH8XEP5T9A==@dbohicecreamratings.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@dbohicecreamratings@"
db_name = 'icecreamratings'


def get_db_client():
    client = MongoClient(conn_str)
    db = client[db_name]
    return db 

def get_ratings_colilection(collection_name):
    ratings = db[collection_name]
    return ratings



