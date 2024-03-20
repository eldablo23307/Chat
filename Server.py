from flask import Flask, request
import requests

app = Flask(__name__)

all_user = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user = request.form["user"]
        all_user.append(user)
        Message = request.form["Text"]
        file = open("History.txt", "r")
        backup = file.read()
        file.close()
        file = open("History.txt", "w")
        file.write(f"{backup}\n{user}: {Message}")
        file.close()
    return "hello"

@app.route("/chat")
def chat():
    file = open("History.txt", "r")
    current_chat = file.read()
    file.close()
    return current_chat


if __name__ == "__main__":
    app.run(host="0.0.0.0")