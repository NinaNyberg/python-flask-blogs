from pymongo import MongoClient
from bson.objectid import ObjectId

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

def save_blog(form):
    blogs_collection = db["blogs"]
    title = form["title"]
    snippet = form["snippet"]
    body = form["body"]

    new_blog = {"title": title, "snippet": snippet, "body": body}
    blogs_collection.insert_one(new_blog)

def get_blog_by_id(id):
    blogs_collection = db["blogs"]
    blog = blogs_collection.find_one({"_id": ObjectId(id)})
    return blog

def delete_blog_by_id(id):
    blogs_collection = db["blogs"]
    blogs_collection.find_one_and_delete({"_id": ObjectId(id)})

def update_blog_by_id(form, id):
    blogs_collection = db["blogs"]
    
    new_title = form["title"]
    new_snippet = form["snippet"]
    new_body = form["body"]
    blogs_collection.find_one_and_update({"_id": ObjectId(id)}, { "$set": {"title": new_title, "snippet": new_snippet, "body": new_body}})

    


db = connect_to_mongo()