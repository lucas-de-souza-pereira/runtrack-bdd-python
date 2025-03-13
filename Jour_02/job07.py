import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv("../.env")

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = os.getenv("DB_PASSWORD"),
    database = "ressource_laplateforme"
)

if mydb.is_connected():
    db_info = mydb.get_server_info()
    print(db_info)

    cursor = mydb.cursor()


    cursor.execute("""
                    SELECT employe.id, employe.nom, employe.salaire, service.nom
                    FROM employe
                    JOIN service ON employe.id_service = service.id;
                """)
    

    employe_service = cursor.fetchall()
    print(employe_service)
    
    cursor.close()
mydb.close()


class Employe():
    """Crud. ajouter_employe / ajouter_service"""
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = os.getenv("DB_PASSWORD"),
            database = "ressource_laplateforme"
            )
        self.cursor = self.mydb.cursor()
        
    def verifier_connexion(self):
        db_info = self.mydb.get_server_info()
        print(f"la connexion est bien établie avec {db_info}")

    def fermer_bdd(self):
        self.cursor.close()
        self.mydb.close()


    def ajouter_employe(self,nom,prenom,salaire,id_service):
        """Ajouter un employer : crud.ajouter_employe ("nom","prénom",salaire,id_service)"""

        self.cursor.execute("""
                        INSERT INTO employe(nom,prenom,salaire,id_service)
                        VALUES (%s,%s,%s,%s)""",
                        (nom,prenom,salaire,id_service))

        print(f"{nom} {prenom} a bien été ajoutée avec un salaire de {salaire} et id_service {id_service}")

    def ajouter_service(self,service):

        self.cursor.execute("""
                        INSERT INTO service(nom)
                        VALUES (%s)""",
                        (service,))

        print(f"le {service} est bien ajouté à la liste")

    def voir_liste_employe(self):

        self.cursor.execute("""
                SELECT * 
                FROM employe
            """)

        employe_liste = self.cursor.fetchall()

        for employe in employe_liste:
            print(employe)


    def voir_un_employe(self,nom):

        self.cursor.execute("""
                SELECT * 
                FROM employe
                WHERE nom = %s""", 
                (nom,))

        employe = self.cursor.fetchone()

        print(employe)


    def modifier_service_id(self,id_service,nom):

        self.cursor.execute("""
        UPDATE employe
        SET id_service = %s
        WHERE nom = %s""",
        (id_service,nom))

    def supprimer_employe(self,nom):

                self.cursor.execute("""
        DELETE FROM employe
        WHERE nom = %s""",
        (nom,))


crud = Employe()
# crud.ajouter_employe("Anne","Marie",1900,2)
# crud.ajouter_service("Ressource Humaine")
crud.verifier_connexion()

crud.voir_liste_employe()
crud.voir_un_employe("Hue")

# crud.modifier_service_id(1,"Hue")

crud.supprimer_employe("Anne")

crud.mydb.commit()
crud.fermer_bdd()
