from flask import Flask, render_template, request, redirect
from db import *

app = Flask("flask-blogit")

get_all_blogs()

# page_title="HOME PAGE"
# page_content=["First", "Second", "Third"]

@app.route("/")
def home():
    all_blogs = get_all_blogs()
    return render_template("index.html", 
    blogs=all_blogs,
    title="HOME")

@app.route("/blogs/create", methods=["POST", "GET"])
def create():
    if request.method == "GET":
        return render_template("create.html", title="CREATE BLOG")
    elif request.method == "POST":
        save_blog(request.form)
        return redirect("/")



@app.route("/about")
def info():
    return render_template("about.html", title="ABOUT")

app.run()