from flask import Flask, request
import mysql.connector

app = Flask(__name__)
mydb = mysql.connector.connect(host="eldablo81.mysql.pythonanywhere-services.com", user="eldablo81", password="M0ttu2307")
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE messaggi (user VARCHAR(255), messagio VARCHAR(255));")
all_user = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user = request.form["user"]
        all_user.append(user)
        Message = request.form["Text"]
        sql = "INSERT INTO messaggi (user, messagio) VALUES (%s, %s);"
        val = (user, Message)
        mycursor.execute(sql, val)
        mydb.commit()
    return "hello"

@app.route("/chat")
def chat():
    file = open("History.txt", "r")
    current_chat = file.read()
    file.close()
    return current_chat


if __name__ == "__main__":
    app.run(host="0.0.0.0")