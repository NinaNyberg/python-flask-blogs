from pymongo import MongoClient

def connect_to_mongo():
    try:
        CONNECTION_STRING="mongodb+srv://ninan:python@cluster0.gg8mj9q.mongodb.net/?retryWrites=true&w=majority"
        connection= MongoClient(CONNECTION_STRING)
        print("conection ok")
        return connection["blogsDB"]
    except Exception as e: 
        print("cannot connect")
        raise e

def get_all_blogs():
    blogs_collection = db["blogs"]
    blogs = len(list(blogs_collection.find()))

    if blogs==0:
        all_blogs=[{"title": "No documents found"}]
        return all_blogs
    else:
        all_blogs = blogs_collection.find()
        return all_blogs

db = connect_to_mongo()