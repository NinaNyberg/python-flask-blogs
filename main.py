from flask import Flask, render_template, request, redirect, flash
from db import *

app = Flask("flask-blogit")

app.secret_key = b'_5#y'

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
        flash("BLOG CREATED!")
        return redirect("/")


@app.route("/blogs/<id>") # <string:id> <int:id>
def show_blog(id):
    single_blog = get_blog_by_id(id)
    return render_template("blog.html", blog=single_blog, title="BLOG")


@app.route("/blogs/delete/<id>")
def delete_blog(id):
    delete_blog_by_id(id)
    flash(f"Blog {id} deleted")
    return redirect("/")

@app.route("/blogs/update/<id>", methods=["POST", "GET"])
def update_blog(id):
    if request.method == "GET":
        blog_by_id=get_blog_by_id(id)
        return render_template("update.html", form = blog_by_id, id=id, title="UPDATE BLOG")
    elif request.method == "POST":
        update_blog_by_id(request.form, id)
        flash("BLOG UPDATED!")
        return redirect("/")


@app.route("/about")
def info():
    return render_template("about.html", title="ABOUT")

app.run()