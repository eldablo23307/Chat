import mysql.connector

# Connessione al database
mydb = mysql.connector.connect(
    host="Software99.mysql.pythonanywhere-services.com",
    user="Software99",
    password="M0ttu2307",
    database="Software99$default"  # Sostituisci con il nome del tuo database
)

# Creazione del cursore
mycursor = mydb.cursor()

# Query per cancellare tutti i dati dalla tabella
sql = "DELETE FROM messaggi;"  # Sostituisci con il nome della tua tabella

# Esecuzione della query
mycursor.execute(sql)

# Commit delle modifiche
mydb.commit()

# Chiusura della connessione
mycursor.close()
mydb.close()

print("Tutti i dati sono stati cancellati dalla tabella.")
