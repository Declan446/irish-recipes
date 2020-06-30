import os
import json
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env

app = Flask(__name__)


app.config['MONGO_URI'] = os.environ.get("MONGO_URI")
DATABASE = "irish_recipes"

mongo = PyMongo(app)


@app.route('/')
@app.route("/get_recipes")
def base():
    return render_template("base.html", recipes=mongo.db.recipes.find())


@app.route('/add')
def add():
    return render_template("add.html")


@app.route('/map')
def map():
    return render_template("map.html")


@app.route('/top')
def top():
    data = []
    with open("data/restaurants.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("top.html", restaurants=data)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
