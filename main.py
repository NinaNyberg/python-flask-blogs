from flask import Flask, render_template
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

app.run()