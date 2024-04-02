from flask import Flask, request
from Databasehandle import Write_In_DataBase, Return_From_DataBase


app = Flask(__name__)
all_user = []
swear_words = [
    "arse",
    "arsehead",
    "arsehole",
    "ass",
    "asshole",
    "bastard",
    "bitch",
    "bloody",
    "bollocks",
    "brotherfucker",
    "bugger",
    "bullshit",
    "child-fucker",
    "cock",
    "cocksucker",
    "crap",
    "cunt",
    "cyka blyat",
    "damn",
    "damn it",
    "dick",
    "dickhead",
    "dyke",
    "fatherfucker",
    "frigger",
    "fuck",
    "goddamn",
    "godsdamn",
    "hell",
    "holy shit",
    "horseshit",
    "in shit",
    "Jesus Christ",
    "Jesus fuck",
    "Jesus H. Christ",
    "Jesus Harold Christ",
    "Jesus, Mary and Joseph",
    "Jesus wept",
    "kike",
    "motherfucker",
    "nigga",
    "nigra",
    "pigfucker",
    "piss",
    "prick",
    "pussy",
    "shit",
    "shit ass",
    "shite",
    "sisterfucker",
    "slut",
    "son of a whore",
    "son of a bitch",
    "spastic",
    "sweet Jesus",
    "turd",
    "twat",
    "wanker"
]


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user = request.form["user"]
        all_user.append(user)
        Message = request.form["Text"]
        hold = Message.split()
        for i in hold:
            if i in swear_words:
                Message = Message.replace(i, "******")
        Write_In_DataBase(user, Message)

    return "hello"

@app.route("/chat")
def chat():
    return str(Return_From_DataBase()) # Convertire in stringa per la visualizzazione, modifica come preferisci

if __name__ == "__main__":
    app.run()
