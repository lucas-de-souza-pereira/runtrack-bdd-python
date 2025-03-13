import os
import mysql.connector
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
    print(f"serveur info {db_info}")

    cursor = mydb.cursor()

    cursor.execute("SELECT SUM(superficie) FROM etage")

    superficie = cursor.fetchone()

    print(f"la superficie de la plateforme est de : {superficie[0]} m²")

    cursor.close()
mydb.close()