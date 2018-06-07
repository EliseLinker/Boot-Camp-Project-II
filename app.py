from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
# from flask_pymongo import PyMongo
import pymongo 

app = Flask(__name__)

# mongo = PyMongo(app)

conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)
db = client.wine_store_db
collection = db.items


@app.route("/")
def index():
    # winelist = list(db.items.find().sort('title', pymongo.ASCENDING))
    # print(winelist)
    return render_template("index.html")


@app.route("/finder", methods=["GET","POST"])
def finder():
    if request.method=="POST":
        name = request.form["wineName"]
        winelist = list(db.items.find({'title': {'$regex': ''+ name +''}}))
        print(winelist)
                        
        # winelist = list(db.items.find({'title': {'$regex': ''+ name +''}}))
        # return redirect("http://localhost:5000/", code=302)
        return render_template("ws-index.html", winelist=winelist)

    if request.method=="GET":
        winelist = list(db.items.find().sort('title', pymongo.ASCENDING).limit(10))
        return render_template("ws-index.html", winelist=winelist)

    return render_template("ws-index.html", winelist=winelist)

# # Query the database and send the jsonified results
# @app.route("/send", methods=["GET", "POST"])
# def send():
#     if request.method == "GET":
#         name = request.form["wineName"]
                
#         winelist = list(db.items.find({'title': {'$regex': ''+ name +''}}))
#         return redirect("http://localhost:5000/", code=302)

#     # return render_template("form.html")
#     return render_template("ws-index.html", winelist=winelist)
#     # winelist = list(db.items.find().sort('title', pymongo.ASCENDING))
#     # return render_template("index.html", winelist=winelist)


if __name__ == "__main__":
    app.run(debug=True)
