import mysql.connector

def Write_In_DataBase(user, Message):
    mydb = mysql.connector.connect(host="Software99.mysql.pythonanywhere-services.com", user="Software99", password="M0ttu2307", database="Software99$default")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE IF NOT EXISTS messaggi (user VARCHAR(255), messagio VARCHAR(255));")
    sql = "INSERT INTO messaggi (user, messagio) VALUES (%s, %s);"
    val = (user, Message)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()
    mydb.close()

def Return_From_DataBase():
    mydb = mysql.connector.connect(host="Software99.mysql.pythonanywhere-services.com", user="Software99", password="M0ttu2307", database="Software99$default")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM messaggi;")
    messages = mycursor.fetchall() # Ottenere tutti i messaggi
    mycursor.close()
    mydb.close()
    return messages

def Write_email(email):
    mydb = mysql.connector.connect(host="Software99.mysql.pythonanywhere-services.com", user="Software99", password="M0ttu2307", database="Software99$User_info")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE IF NOT EXISTS mail (email VARCHAR(255));")
    sql = "INSERT INTO mail (email) VALUES (%s);"
    val = (email)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()
    mydb.close()