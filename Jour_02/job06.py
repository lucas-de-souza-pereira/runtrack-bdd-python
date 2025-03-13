import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv("../.env")

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = os.getenv("DB_PASSWORD"),
    database = "laplateforme"
)

if mydb.is_connected():
    db_info = mydb.get_server_info()
    print(db_info)

    cursor = mydb.cursor()

    cursor.execute("""SELECT SUM(capacite)
                                FROM salle
                                """)

    capacite = cursor.fetchone()

    print(f"La capacité de toutes les salles est de : {capacite[0]}")

    cursor.close()
mydb.close()
