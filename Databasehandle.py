from tinydb import TinyDB, Query

def Write_In_DataBase(user, message):
    db = TinyDB('database.json')
    db.insert({"user": user, "message": message})

def Return_From_DataBase():
    db = TinyDB('datatbase.json')
    messages = db.all()
    return messages

