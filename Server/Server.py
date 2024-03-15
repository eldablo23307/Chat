from flask import Flask, request
import requests

app = Flask(__name__)

all_ip = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        Ip = request.form["Ip"]
        all_ip.append(Ip)
        Message = request.form["Text"]
        file = open("History.txt", "r")
        backup = file.read()
        file.close()
        file = open("History.txt", "w")
        file.write(f"{backup}\n{Ip}: {Message}")
        file.close()
    return "hello"

@app.route("/chat")
def chat():
    file = open("History.txt", "r")
    current_chat = file.read()
    file.close()
    return f"current_chat"
