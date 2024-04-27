from flask import Flask, request
from Databasehandle import Write_In_DataBase, Return_From_DataBase
from LogginDB import check_db
from better_profanity import profanity


app = Flask(__name__)
all_user = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user = request.form["user"]
        all_user.append(user)
        Message = request.form["Text"]
        Message = profanity.censor(Message)
        
        Write_In_DataBase(user, Message)

    return "hello"

@app.route("/chat")
def chat():
    return str(Return_From_DataBase())

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["User"]
        psswd = request.form["Psswd"]
        return check_db(user, psswd)

    return "login"

if __name__ == "__main__":
    app.run()
