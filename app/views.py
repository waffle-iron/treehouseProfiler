from flask import render_template
from flask import request
import requests
from app import app
import json

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/data", methods=['POST'])
def entry_post():
    query = request.form["search"]
    url = "http://www.teamtreehouse.com/"+query+".json"
    r = requests.get(url)
    parsed_json = json.loads(r.text)
    username = parsed_json["name"]
    profile_url = parsed_json["profile_url"]
    gravatar = parsed_json["gravatar_url"]
    topics = parsed_json["points"]
    total_points = parsed_json["points"]["total"]
    return render_template("data.html" , search = request.form['search'],
                                         profile_url = profile_url,
                                         name = username,
                                         gravatar = gravatar,
                                         total = total_points,
                                         topics = topics)

