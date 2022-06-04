from flask import Flask, redirect, render_template, session
import json
import pyautogui as pgui
import subprocess
from flask import request
import os

app = Flask(__name__, template_folder="Template")
app.secret_key = os.urandom(24)
Config_json = json.load(open("Config.json", "r"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/btn", methods=["POST", "GET"])
def btn():
    if request.method == "POST":
        key = request.form["btn"]
        if key in Config_json:
            if "Link" in Config_json.get(key):
                subprocess.Popen(Config_json[key]["Link"])
            elif "Key" in Config_json.get(key):
                push_key(Config_json[key]["Key"])
    return render_template("index.html")

def push_key(key):
    if len(key) == 1:
        pgui.keyDown(key[0])
        pgui.keyUp(key[0])
    else:
        for i in range(len(key)):
            print(key[i])
            pgui.keyDown(key[i])
        for i in range(len(key)):
            pgui.keyUp(key[i])

@app.errorhandler(404)
def page_not_found(e):
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
