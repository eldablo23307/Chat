from flask import Flask, request
from Databasehandle import Write_In_DataBase, Return_From_DataBase


app = Flask(__name__)
all_user = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user = request.form["user"]
        all_user.append(user)
        Message = request.form["Text"]
        Write_In_DataBase(user, Message)

    return "hello"

@app.route("/chat")
def chat():
    return str(Return_From_DataBase()) # Convertire in stringa per la visualizzazione, modifica come preferisci

if __name__ == "__main__":
    app.run()
