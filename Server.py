from flask import Flask, request
import mysql.connector

app = Flask(__name__)
mydb = mysql.connector.connect(host="Software99.mysql.pythonanywhere-services.com", user="Software99", password="M0ttu2307", database="Software99$default") # Assicurati di sostituire 'nome_del_tuo_database' con il nome effettivo del tuo database
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS messaggi (user VARCHAR(255), messagio VARCHAR(255));")
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
    mycursor.execute("SELECT * FROM messaggi;")
    messages = mycursor.fetchall() # Ottenere tutti i messaggi
    return str(f"{messages}") # Convertire in stringa per la visualizzazione, modifica come preferisci

if __name__ == "__main__":
    app.run()
