import mysql.connector

def check_db(username, password):
    # Connessione al database
    mydb = mysql.connector.connect(host="Software99.mysql.pythonanywhere-services.com", 
                                   user="Software99", 
                                   password="M0ttu2307", 
                                   database="Software99$User_info")
    mycursor = mydb.cursor()
    
    # Controllo se lo username esiste già nel database
    query = "SELECT * FROM messaggi WHERE user = %s"
    mycursor.execute(query, (username,))
    existing_user = mycursor.fetchone()

    if existing_user:
        # Se lo username esiste, controllo se la password corrisponde
        if existing_user[1] == password:
            mycursor.close()
            mydb.close()
            return True  # Le credenziali corrispondono
        else:
            mycursor.close()
            mydb.close()
            return False  # La password non corrisponde
            
    else:
        # Se lo username non esiste, lo aggiungo al database insieme alla password
        query = "INSERT INTO messaggi (user, password) VALUES (%s, %s)"
        mycursor.execute(query, (username, password))
        mydb.commit()  # Faccio il commit delle modifiche al database
        mycursor.close()
        mydb.close()
        return True  # Credenziali aggiunte con successo