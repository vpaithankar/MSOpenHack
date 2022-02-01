import logging

import azure.functions as func
#from db_ops import get_db_client, get_ratings_collection, get_rating_by_id
from pymongo import MongoClient

conn_str = "mongodb://dbohicecreamratings:YDjwWB1PW7C4lJjKxS2s4LDY99BVocbqErOV36YKTQ56eDYI2hJg5ASV1G9qFovTzjuTE8dnWCO2JH8XEP5T9A==@dbohicecreamratings.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@dbohicecreamratings@"
db_name = 'icecreamratings'

def get_db_client():
    client = MongoClient(conn_str)
    db = client[db_name]
    return db

def get_ratings_collection(collection_name):
    db = get_db_client()
    ratings = db[collection_name]
    return ratings


def get_rating_by_id(rating_col,ratingId):
    result = rating_col.find_one({"id":ratingId},{"_id":0})

    if result:
        return result
    else:
        return None





def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    ratingId = req.params.get('ratingId')
    if not ratingId:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            ratingId = req_body.get('ratingId')

    if ratingId:
        rc = get_ratings_collection('ratings_test')
        result = get_rating_by_id(rc,ratingId)
        if result:
             #return func.HttpResponse(f"Hello, {ratingId}. This HTTP triggered function executed successfully.")
            return func.HttpResponse(str(result),status_code=200)
        else:
            return func.HttpResponse("This rating is not found in the database. Please check the entered rating id",status_code=404)
    else:
        return func.HttpResponse(
             "Bad Reuest.Please pass a ratingId in the query string or in the request body for a response.",
             status_code=400
        )
