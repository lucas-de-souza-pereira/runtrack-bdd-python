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
    print(f"connecté à {db_info}")

    cursor = mydb.cursor()

    cursor.execute("SELECT nom,capacite FROM salle")

    resultats = cursor.fetchall()
    print(resultats)

    cursor.close()
mydb.close()