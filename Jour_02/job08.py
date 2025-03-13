import mysql.connector
import os
from dotenv import load_dotenv
from tabulate import tabulate

load_dotenv("../.env")



class Directeur():
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = os.getenv("DB_PASSWORD"),
            database = "zoo"
            )
        self.cursor = self.mydb.cursor()

    def fermer_bdd (self):
        self.cursor.close()
        self.mydb.close()

    def ajouter_animal(self):
        
        nom = input("""Nom de l'animal : """).strip()
        date_de_naissance = input("""Date de naissance (format : YYYY-MM-YY) : """).strip()
        pays_origine = input("""Pays d'origine : """).strip()

        querry = """INSERT INTO animal (nom,date_de_naissance,pays_origine) 
                    VALUES (%s,%s,%s)
                    """
        valeurs = (nom,date_de_naissance,pays_origine)

        self.cursor.execute(querry,valeurs)

        self.mydb.commit()
        self.fermer_bdd()

        print("L'animal à bien été ajouter à la base de donnée")

    def supprimer_animal(self):

        id_animal = input("Id de l'animal : ")

        querry = ("DELETE FROM animal WHERE id = %s")
        
        self.cursor.execute(querry,(id_animal,))
        self.mydb.commit()
        self.fermer_bdd()

        print("L'animal à bien été enlevé de la base de donnée")

    def ajouter_cage(self):
        
        superficie = input("superficie de la cage : ")
        capacite = input("capacité de la cage")
    
        querry = """INSERT INTO cage (superficie,capacite) 
                    VALUES (%s,%s)
                    """
        valeurs = (superficie,capacite)

        self.cursor.execute(querry,valeurs)

        self.mydb.commit()
        self.fermer_bdd()

        print("La cage est ajoutée a la BDD")

    def supprimer_cage(self):
    
        id_cage = input("Id de la cage : ")

        querry = ("DELETE FROM cage WHERE id = %s")
        
        self.cursor.execute(querry,(id_cage,))
        self.mydb.commit()
        self.fermer_bdd()

        print("la cage est bien supprimé de la bdd")

    def modifier_cage(self):

        id_cage = input("id de la cage a modifier : ")
        nouvelle_superficie = input("superficie de la nouvelle cage : ")
        nouvelle_capacite = input("capacité de la nouvelle cage : ")

        querry = ("""
                UPDATE cage
                SET superficie = %s, capacite = %s
                WHERE id = %s""")
        valeurs = (nouvelle_superficie,nouvelle_capacite,id_cage)

        self.cursor.execute(querry,valeurs)
        self.mydb.commit()
        self.fermer_bdd()

    def modifier_animal(self):
    
        id_animal = input("id de l'animal : ")
        id_nouvelle_cage = input("id de la nouvelle cage de l'animal : ")

        querry = ("""
                UPDATE animal
                SET id_cage = %s
                WHERE id = %s""")
        valeurs = (id_nouvelle_cage,id_animal)

        self.cursor.execute(querry,valeurs)
        self.mydb.commit()
        self.fermer_bdd()

        print("Affectation à jour")

    def liste_animaux(self):
        
        querry = ("""
                SELECT id,nom,date_de_naissance,pays_origine
                FROM animal""")


        self.cursor.execute(querry)
        resulta = self.cursor.fetchall()
        self.fermer_bdd()

        colonnes = [desc[0] for desc in self.cursor.description]

        print(tabulate(resulta, headers=colonnes, tablefmt= "grid"))



    def liste_cage(self):
        
        querry = ("""
        SELECT id,superficie,capacite
        FROM cage""")

        self.cursor.execute(querry)
        resultat = self.cursor.fetchall()
        self.fermer_bdd()

        colonnes = [desc[0] for desc in self.cursor.description]

        print(tabulate(resultat, headers=colonnes, tablefmt= "grid"))


    def liste_animaux_cage(self):
        
        querry = (""" 
                SELECT animal.id,animal.nom,animal.date_de_naissance,animal.pays_origine,animal.id_cage,
                cage.superficie, cage.capacite
                FROM animal
                JOIN cage ON animal.id_cage = cage.id
                ORDER BY animal.id_cage ASC
            """)

        self.cursor.execute(querry)        
        resultat = self.cursor.fetchall()
        self.fermer_bdd()

        colonnes = [desc[0] for desc in self.cursor.description]

        print(tabulate(resultat, headers= colonnes, tablefmt= "grid"))

    def liste_animaux_sans_cage(self):

        querry = ("""
            SELECT id,nom
            FROM animal
            WHERE id_cage IS NULL
            ORDER BY id ASC
        """)

        self.cursor.execute(querry)        
        resultat = self.cursor.fetchall()
        self.fermer_bdd()

        colonnes = [desc[0] for desc in self.cursor.description]

        print(tabulate(resultat, headers= colonnes, tablefmt= "grid"))

    def surperficie_total_cage(self):
        
        querry = ("SELECT SUM(superficie) FROM cage")

        self.cursor.execute(querry)
        resultat = self.cursor.fetchone()

        print(f"la surficie de ces cages est de : {resultat[0]} m²")

def afficher_menu():
    print("""
    Que souhaitez vous faire ?
    1. Lister les annimaux du zoo 
    2. Lister les annimaux en cage
    3. Lister les annimaux sans cage
    4. Lister les cages
    5. Superficie des cages
    6. Accès directeur
    7. Quitter
""")
    
def menu_directeur():
    print(""""
    Bonjour M. Le directeur
    Que souhaitez vous faire ? 
        1. ajouter un animal
        2. Ajouter une cage
        3. supprimer un animal
        4. Supprimer une cage 
        5. Modifier emplacement cage d'un animal
        6. Modifier une cage
        7. Retour menu
""")

directeur = Directeur()

while True:

    afficher_menu()

    choix = input(" ") 

    if choix == "1":
        directeur.liste_animaux()

    if choix == "2":
        directeur.liste_animaux_cage()

    if choix == "3":
        directeur.liste_animaux_sans_cage()

    if choix == "4":
        directeur.liste_cage()

    if choix == "5":
        directeur.surperficie_total_cage()

    if choix == "6":
        menu_directeur()

        choix = input(" ") 

        if choix == "1":
            directeur.ajouter_animal()

        if choix == "2":
            directeur.ajouter_cage()

        if choix == "3":
            directeur.supprimer_animal()

        if choix == "4":
            directeur.supprimer_cage()

        if choix == "5":
            directeur.modifier_animal()

        if choix == "6":
            directeur.modifier_cage()

        if choix == "7":
            continue

    if choix == "7":
        break