from pymongo import MongoClient
import sys
import random


# MENU = [
#   "Lancer Jeu",
#   "Afficher les scores",
#   "Quitter",
# ]
MENU = [
    "Lancer Jeu",
    "Afficher les scores",
    "Quitter",
]

client = MongoClient("mongodb://localhost:27017/")

# Menu
#   Boucle sur tout element de MENU
#       afficher numero element et texte element
def afficher_menu():
    for i in range(len(MENU)):
        print(i + 1, "-", MENU[i])


# Choix (options, erreur)
#    while True:
#        Recuperer choix utilisateur
#        Verifier si choix est valide
#        Si valide
#             return choix
#        Sinon
#             Lancer fonction erreur

 
 
def choix(options, erreur):
    while True:
        saisie = input("Votre choix : ")
        if saisie.isdigit() and 1 <= int(saisie) <= len(options):
            return int(saisie)
        else:
            erreur()
            
def erreur():
    print("Erreur : saisie invalide")

# Recuperer heros DB
#       ouvrir base
#       acceder a la collection heros
#       find
#       convertir le curseur en liste
#       heros_dispo = liste
def recuperer_heros():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["game_db"]
    collection = db["characters"]
    curseur = collection.find()
    liste = list(curseur)
    heros_dispo = liste
    return heros_dispo

# Afficher heros dispo
#       Boucle sur tout element de heros_dispo
#           afficher nom, pv, attaque, defense
def afficher_heros_dispo(heros_dispo):
    for hero in heros_dispo:
        print(hero["name"], "| PV :", hero["hp"], "| Attaque :", hero["attack"], "| Défense :", hero["defense"])


# Récupérer 3 noms valides
#       noms = []
#       tant que len(noms) < 3 :
#           Recuperer nom utilisateur
#           Verifier si nom est valide
#               nom existe dans heros_dispo (sans tenir compte majuscules)
#               pas deja dans noms
#           Si valide
#               ajouter nom a noms
#           Sinon
#               Lancer fonction erreur
#       return noms
def recuperer_3_noms_valides(heros_dispo):
    noms = []
    while len(noms) < 3:
        nom = input("Nom du héros : ").lower()
        existe = False
        for hero in heros_dispo:
            if hero["name"].lower() == nom:
                existe = True
        deja_dans_noms = nom in noms
        if existe and not deja_dans_noms:
            noms.append(nom)
        else:
            erreur()
    return noms



# Construire l'equipe
#       equipe = []
#       for nom in noms :
#           hero = element de heros_dispo dont le nom == nom
#           hero.estEnVie = True
#           ajouter hero a equipe
#   return equipe
def construire_equipe(noms , heros_dispo):
    equipe = []
    for nom in noms:
        for element in heros_dispo :
            if element ["name"].lower() == nom :
                hero = element
        hero["estEnVie"] = True
        equipe.append(hero)
    return equipe 


# nouveau.monstre
#     recup monstres DB
#         ouvrir base
#         acceder a la collection monstre
#         find
#         convertir le curseur en liste
#     monstre = random dans la liste
#     monstre.estEnVie = True

def nouveau_monstre():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["game_db"]
    collection = db["monsters"]
    curseur = collection.find()
    liste = list(curseur)
    monstre = random.choice(liste)
    monstre["estEnVie"] = True
    return monstre


# estEnVie :
#     si les pv > 0 : return True
#     sinon : return False

def estEnVie( personnage): 
    if personnage["hp"] > 0 :
        return True
    else :
        return False

# afficher_stats_hero : afficher les stats hero

def afficher_stats_hero (equipe):
    for hero in equipe :
        print (hero["name"] , " PV : ", hero["hp"], " Attaque : " , hero["attack"] , "defense : ", hero["defense"])

# afficher_stats_monstre : afficher les stats monstre

def afficher_stats_monstre (monstre) :
        print (monstre["name"] , " PV : ", monstre["hp"], " Attaque : " , monstre["attack"] , "defense : ", monstre["defense"])


# hero_attaque
#     recuperer attaque hero
#     recuperer hp et defense monstre
#     degats_hero = attaqueHero - defense.monstre
#     pv_monstre = pv_monstre - degats_hero
#     return degats_hero

def hero_attaque(hero, monstre):
    attaque_hero = hero["attack"]
    defense_monstre = monstre["defense"]
    degats_hero = max(attaque_hero - defense_monstre, 0)  
    monstre["hp"] = monstre["hp"] - degats_hero
    monstre["estEnVie"] = estEnVie(monstre)
    return degats_hero


# attaquer_monstre
#     recuperer attaque monstre
#     recuperer defense hp hero
#     degats_monstre = attaqueMonstre - defense.hero
#     pv_hero = pv_hero - degats_monstre
#     return degats_monstre

def monstre_attaque(monstre , hero) :
    attaque_monstre = monstre["attack"]
    defense_hero = hero["defense"]
    degats_monstre = max(attaque_monstre - defense_hero, 0)  
    hero["hp"] = hero["hp"] - degats_monstre 
    hero["estEnVie"] = estEnVie(hero)             

    return degats_monstre


def au_moins_un_hero_en_vie(equipe):
    for hero in equipe:
        if hero["estEnVie"] == True:
            return True
    return False



# JEU
def jeu():
    # Récupérer 3 noms valides (création de l'équipe)
    # tant que au moins un hero est en vie 
    # for heros in choix 
    # for monstre in choix 
    # le monstre attaque le premier héros en vie



    heros_dispo = recuperer_heros()
    afficher_heros_dispo(heros_dispo)
    noms = recuperer_3_noms_valides(heros_dispo)
    equipe = construire_equipe(noms, heros_dispo)
    vague = 0
    monstre = nouveau_monstre()
    while au_moins_un_hero_en_vie(equipe):
        afficher_stats_hero(equipe)
        afficher_stats_monstre(monstre)

        for hero in equipe:
            if hero["estEnVie"] == True:
                degats_hero = hero_attaque(hero, monstre)
                print(hero["name"], "inflige", degats_hero, "dégâts à" , hero["name"] )
                if monstre["estEnVie"] == False:
                    print("Le monstre", monstre["name"], "est mort")
                    vague += 1
                    monstre = nouveau_monstre()
                    break

        if monstre["estEnVie"] == True:
            for hero in equipe:
                if hero["estEnVie"] == True:
                    degats_monstre = monstre_attaque(monstre, hero)
                    print(monstre["name"], "inflige", degats_monstre, "dégâts")
                    break
        else:
            print("Le monstre", monstre["name"], "est mort")


# Fin de partie 
# ajouter le score dans la db
    print("Game over - vagues :", vague)
    client = MongoClient("mongodb://localhost:27017/")
    client["jeu"]["score"].insert_one({"waves": vague})


# Afficher les scores
#    Recuperer scores base
#        ouvrir base
#        acceder a collection score
#        find
#        convertir curseur en list
#    filtrer les 3 meilleurs
#         trie le tableau sur element.waves
#         prendre 3 derniers elements
#                array[-3:]
#    Affiche les score

def trier_par_vague(element):
    return element["waves"]

def afficher_scores():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["jeu"]
    collection = db["score"]
    curseur = collection.find()
    scores = list(curseur)

    scores.sort(key=trier_par_vague)
    meilleurs = scores[-3:]

    for score in meilleurs:
        print(score["waves"], "vagues")


#Quitter 

def quitter():
    sys.exit()

def main():
    while True:
        afficher_menu()
        option = choix(MENU, erreur)
        if option == 1:
            jeu()
        elif option == 2:
            afficher_scores()
        elif option == 3:
            quitter()

main()