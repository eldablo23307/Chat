from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        Ip = request.form["Ip"]
        Message = request.form["Text"]
        file = open("History.txt", "r")
        backup = file.read()
        file.close()
        file = open("History.txt", "w")
        file.write(f"{backup}\n{Ip}: {Message}")
        file.close()
    return "hello"


if __name__ == "__main__":
    app.run(host="0.0.0.0")